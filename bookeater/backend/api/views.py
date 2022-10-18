from .models import *
from . import models
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated 
from django.shortcuts import get_object_or_404 
from rest_framework import status
from rest_framework.response import Response
from . import serializers
from rest_framework.permissions import IsAuthenticated 
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
from .permission import IsAuthor
from jalali_date import datetime2jalali, date2jalali
from django.db.models import Q



base_url = 'https://bookeater.ir/' 




class ShowAllNews(APIView):

    def get(self, request):

        news = News.objects.filter(status='p')

        data = []
        for n in news:
            data.append({
                'title': n.title,
                'description': n.description,
                'slug': n.slug,
                'image': n.image.url,
                'date': datetime2jalali(n.date).strftime('14%y/%m/%d _ %H:%M'),
            })
        
        return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)



class ShowQuotes(APIView):
    
    def get(self, request):

        quotes = Quote.objects.filter(status='p')

        data = []
        for quote in quotes:
            data.append({
                'author': quote.author,
                'description': quote.description,
                'thumbnail': quote.thumbnail.url,
            })

        return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)
    


class ShowBestBooks(APIView):

    def get(self, request):

        id = self.request.user.id

        books = Book.objects.filter(status='p').order_by('-score')

        data = []
        for book in books:
            
            # check : this book exit in readlist or not
            in_readlist = False
            if(self.request.user.is_authenticated):
                user = get_object_or_404(User, id=id)
                if(user.readlist.filter(slug=book.slug)):
                    in_readlist = True

            # user score
            user_score_queryset = Score.objects.filter(book=book.id).filter(user=id)
            user_score = ''
            for user in user_score_queryset:
                user_score = user.user_score

            data.append({
                'title': book.title,
                'description': book.description,
                'score': book.score,
                'user_score': user_score,
                'rates': book.rates,
                'slug': book.slug,
                'thumbnail': book.thumbnail.url,
                'in_readlist': in_readlist,
                'category': [a.title for a in book.category.filter(status='p')],
                'author': [a.full_name for a in book.author.filter(status='p')],
            })
            user_score = ''
        
        return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)



class ShowPopularCategories(APIView):

    def get(self, request):

        categories = Category.objects.filter(status='p', popular_category=True)

        data = []
        for category in categories:
            data.append({
                'title': category.title,
                'slug': category.slug,
                'thumbnail': category.thumbnail.url,
            })
        
        return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)



class ShowMostRatedBooks(APIView):

    def get(self, request):

        id = self.request.user.id

        books = Book.objects.filter(status='p').order_by('-rates')

        data = []
        for book in books:

            # check : this book exit in readlist or not
            in_readlist = False
            if(self.request.user.is_authenticated):
                user = get_object_or_404(User, id=id)
                if(user.readlist.filter(slug=book.slug)):
                    in_readlist = True

            # user score
            user_score_queryset = Score.objects.filter(book=book.id).filter(user=id)
            user_score = ''
            for user in user_score_queryset:
                user_score = user.user_score
            
            
            data.append({
                'title': book.title,
                'description': book.description,
                'score': book.score,
                'user_score': user_score,
                'rates': book.rates,
                'slug': book.slug,
                'thumbnail': book.thumbnail.url,
                'in_readlist': in_readlist,
            })
            user_score = ''
        
        return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)



class ShowPopularAuthors(APIView):

    def get(self, request):

        authors = Author.objects.filter(status='p', popular_author=True)

        data = []
        for author in authors:
            data.append({
                'full_name': author.full_name,
                'slug': author.slug,
                'thumbnail': author.thumbnail.url,
            })
        
        return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)



class ShowAllCategories(APIView):

    def get(self, request):

        categories = Category.objects.filter(status='p')

        data = []
        for category in categories:
            data.append({
                'title': category.title,
                'description': category.description,
                'slug': category.slug,
                'related_author': [[a.full_name, a.slug] for a in category.related_author.filter(status='p')],
                'thumbnail': category.thumbnail.url,
                'id': category.id,
            })
        

        return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)



class ShowAllAuthors(APIView):

    def get(self, request):

        authors = Author.objects.filter(status='p')

        data = []
        for author in authors:
            data.append({
                'full_name': author.full_name,
                'description': author.description,
                'slug': author.slug,
                'related_category': [[a.title, a.slug] for a in author.related_category.filter(status='p')],
                'thumbnail': author.thumbnail.url,
                'id': author.id,
            })
        

        return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)



class ShowAllReviewedBooks(APIView):
    
    def get(self, request):

        books = Reviewed_Book.objects.filter(status='p').order_by('-date')

        data = []
        for book in books:
            data.append({
                'title': book.title,
                'description': book.description,
                'content': book.content,
                'author': [[a.full_name, a.slug] for a in book.author.filter(status='p')],
                'category': [[a.title, a.slug] for a in book.category.filter(status='p')],
                'slug': book.slug,
                'thumbnail': book.thumbnail.url,
                'critic': book.critic.get_full_name() if book.critic.get_full_name() else book.critic.username,
                'critic_username': book.critic.username,
            })
        

        return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)



class ShowSingleNews(APIView):

    def post(self, request):

        serializer = serializers.SlugSerializer(data=request.data)
        if serializer.is_valid():
            slug = serializer.data.get('slug')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        # just check for existing
        get_object_or_404(News, slug=slug, status='p')

        news = News.objects.filter(status='p', slug=slug)

        data = []
        for n in news:
            data.append({
                'title': n.title,
                'content': n.content,
                'image': n.image.url,
                'date': datetime2jalali(n.date).strftime('14%y/%m/%d _ %H:%M'),
            })
        
        # another news
        another_news = News.objects.filter(status='p')[:5]
        another_news_data = []
        for n in another_news:
            another_news_data.append({
                'title': n.title,
                'slug': n.slug,
            })
        
        # delete duplicate news from another news
        index = 0
        for a in another_news_data:
            if len(data) > 0:
                if a.get('title') == data[0].get('title'):
                    del another_news_data[index]
            
            index += 1

        return Response({'status': 'ok', 'data': data, 'another_news_data': another_news_data}, status=status.HTTP_200_OK)



class ShowSingleBook(APIView):

    def post(self, request):

        serializer = serializers.SlugSerializer(data=request.data)
        if serializer.is_valid():
            slug = serializer.data.get('slug')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

        id = self.request.user.id

        # just check for existing
        get_object_or_404(Book, slug=slug, status='p')   

        books = Book.objects.filter(status='p', slug=slug)

        data = []
        for book in books:

            # check : this book exit in readlist or not
            in_readlist1 = False
            if(self.request.user.is_authenticated):
                user = get_object_or_404(User, id=id)
                if(user.readlist.filter(status='p', slug=book.slug)):
                    in_readlist1 = True

            # user score
            user_score_queryset = Score.objects.filter(book=book.id).filter(user=id)
            user_score = ''
            for user in user_score_queryset:
                user_score = user.user_score

            data.append({
                'title': book.title,
                'content': book.content,
                'image': book.image.url,
                'category': [[a.title, a.slug] for a in book.category.filter(status='p')],
                'author': [[a.full_name, a.slug] for a in book.author.filter(status='p')],
                'score': book.score,
                'rates': book.rates,
                'user_score': user_score,
                'in_readlist': in_readlist1,
                'slug': book.slug,
                'date': datetime2jalali(book.date).strftime('14%y/%m/%d _ %H:%M'),
            })
            user_score = ''
        # end book_detail
        
        # related_book
        category_slug = data[0]['category'][0][1]

        category = get_object_or_404(Category, slug=category_slug, status='p')

        books = category.books.filter(status='p')

        related_books_data = []
        for book in books:

            # check : this book exit in readlist or not
            in_readlist2 = False
            if(self.request.user.is_authenticated):
                user = get_object_or_404(User, id=id)
                if(user.readlist.filter(status='p', slug=book.slug)):
                    in_readlist2 = True

            # user score
            user_score_queryset = Score.objects.filter(book=book.id).filter(user=id)
            user_score = ''
            for user in user_score_queryset:
                user_score = user.user_score
            
            related_books_data.append({
                'title': book.title,
                'score': book.score,
                'user_score': user_score,
                'slug': book.slug,
                'thumbnail': book.thumbnail.url,
                'in_readlist': in_readlist2
            })
            user_score = ''
        
        # delete duplicate book from related book
        index = 0
        for a in related_books_data:
            if len(data) > 0:
                if a.get('title') == data[0].get('title'):
                    del related_books_data[index]
            
            index += 1
        # end related_book

        # another book from this author
        author_slug = data[0]['author'][0][1]

        author = get_object_or_404(Author, slug=author_slug, status='p')

        author_books = author.books.filter(status='p')

        author_books_data = []
        for book in author_books:
            author_books_data.append({
                'title': book.title,
                'slug': book.slug,
                'thumbnail': book.thumbnail.url,
            })
        
        # delete duplicate book from another book from this author
        index = 0
        for a in author_books_data:
            if len(data) > 0:
                if a.get('title') == data[0].get('title'):
                    del author_books_data[index]
            
            index += 1
        # end of another book from this author

        return Response({'status': 'ok', 'data': data, 'related_books_data': related_books_data, 'author_books_data': author_books_data}, status=status.HTTP_200_OK)



class ShowSingleCategory(APIView):

    def post(self, request):

        serializer = serializers.SlugSerializer(data=request.data)
        if serializer.is_valid():
            slug = serializer.data.get('slug')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        id = self.request.user.id
            
        category = get_object_or_404(Category, slug=slug, status='p')

        # book with this specific category
        books = category.books.filter(status='p')

        books_data = []
        for book in books:

            # check : this book exit in readlist or not
            in_readlist = False
            if(self.request.user.is_authenticated):
                user = get_object_or_404(User, id=id)
                if(user.readlist.filter(status='p', slug=book.slug)):
                    in_readlist = True
            
            # user score
            user_score_queryset = Score.objects.filter(book=book.id).filter(user=id)
            user_score = ''
            for user in user_score_queryset:
                user_score = user.user_score
            

            books_data.append({
                'title': book.title,
                'description': book.description,
                'score': book.score,
                'user_score': user_score,
                'slug': book.slug,
                'thumbnail': book.thumbnail.url,
                'in_readlist': in_readlist,
            })
            user_score = ''

        # category information
        category_data = [{
            'title': category.title,
            'content': category.content,
            'related_author': [[a.full_name, a.slug, a.thumbnail.url] for a in category.related_author.filter(status='p')],
            'image': category.image.url,
        }]
        
        return Response({'status': 'ok', 'category_data': category_data, 'books_data': books_data,}, status=status.HTTP_200_OK)



class ShowSingleAuthor(APIView):

    def post(self, request):

        serializer = serializers.SlugSerializer(data=request.data)
        if serializer.is_valid():
            slug = serializer.data.get('slug')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        id = self.request.user.id

        author = get_object_or_404(Author, status='p', slug=slug)

        # book that it author is this author
        books = author.books.filter(status='p')

        books_data = []
        for book in books:    
            books_data.append({
                'title': book.title,
                'slug': book.slug,
                'thumbnail': book.thumbnail.url,
            })
        
        # author information
        author_data = [{
            'full_name': author.full_name,
            'content': author.content,
            'image': author.image.url,
            'date': datetime2jalali(author.date).strftime('14%y/%m/%d _ %H:%M'),
        }]

        return Response({'status': 'ok', 'books_data': books_data, 'author_data': author_data,}, status=status.HTTP_200_OK)



class ShowSingleReviewedBook(APIView):

    def post(self, request):

        serializer = serializers.SlugSerializer(data=request.data)
        if serializer.is_valid():
            slug = serializer.data.get('slug')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        # just check for existing
        get_object_or_404(Reviewed_Book, slug=slug, status='p')

        books = Reviewed_Book.objects.filter(status='p', slug=slug)

        reviewed_books_data = []
        for book in books:
            reviewed_books_data.append({
                'title': book.title,
                'content': book.content,
                'image': book.image.url,
                'author': [[a.full_name, a.slug] for a in book.author.filter(status='p')],
                'date': datetime2jalali(book.date).strftime('14%y/%m/%d _ %H:%M'),
                'critic': book.critic.get_full_name() if book.critic.get_full_name() else book.critic.username,
                'critic_username': book.critic.username,
            })

        # some reviewed book for suggest
        reviewed = Reviewed_Book.objects.filter(status='p')
        
        related_reviewed_data = []
        for r in reviewed:
            related_reviewed_data.append({
                'title': r.title,
                'slug': r.slug,
            })
        
        # delete duplicate reviewed book from another reviewed book
        index = 0
        for a in related_reviewed_data:
            if len(reviewed_books_data) > 0:
                if a.get('title') == reviewed_books_data[0].get('title'):
                    del related_reviewed_data[index]
            
            index += 1

        return Response({'status': 'ok', 'reviewed_books_data': reviewed_books_data, 'related_reviewed_data': related_reviewed_data}, status=status.HTTP_200_OK)



class ShowProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        username = self.request.user.username
        
        users = User.objects.filter(username=username)

        data = []
        for user in users:
            data.append({
                'username': user.username,
                'full_name': user.first_name + ' ' + user.last_name,
                'sex': user.sex,
                'age': user.age,
                'public_score': user.public_score,
                'email': user.email,
                'is_author': user.is_author,
            })

        return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)



class UpdateProfileInformation(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):

        serializer = serializers.GetProfileInformationSerializer(data=request.data)
        if serializer.is_valid():
            first_name = serializer.data.get('first_name')
            last_name = serializer.data.get('last_name')
            age = serializer.data.get('age')
            sex = serializer.data.get('sex')
            public_score = serializer.data.get('public_score')
            image = request.FILES.get('image')
            thumbnail = request.FILES.get('thumbnail')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

        username = self.request.user.username

        # set all information exept image and thumbnail
        User.objects.filter(username=username).update(first_name=first_name, last_name=last_name,age=age, sex=sex, public_score=public_score)

        b = get_object_or_404(User, username=username)

        # image and thumbnail is optional so we check then set them
        if(image == None):
            pass
        else:
            b.image.save(image.name, image)

        if(thumbnail == None):
            pass
        else:
            b.thumbnail.save(thumbnail.name, thumbnail)
            

        return Response({'status': 'ok'}, status=status.HTTP_200_OK)



class ShowReadList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        id = self.request.user.id

        username = self.request.user.username
        
        users = User.objects.filter(username=username)

        data = []
        for user in users:
            for book in user.readlist.filter(status='p'):

                # check : this book exit in readlist or not
                in_readlist = False
                if(self.request.user.is_authenticated):
                    user = get_object_or_404(User, id=id)
                    if(user.readlist.filter(status='p', slug=book.slug)):
                        in_readlist = True

                # user score
                user_score_queryset = Score.objects.filter(book=book.id).filter(user=id)
                user_score = ''
                for user in user_score_queryset:
                    user_score = user.user_score

                data.append({
                    'title': book.title,
                    'description': book.description,
                    'slug': book.slug,
                    'thumbnail': book.thumbnail.url,
                    'user_score': user_score,
                    'score': book.score,
                    'rates': book.rates,
                    'in_readlist': in_readlist,
                })
                user_score = ''

        return Response({'status': 'ok', 'data': data, 'username': username}, status=status.HTTP_200_OK)



class ContactUs(APIView):

    def post(self, request):

        serializer = serializers.ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            full_name = serializer.data.get('full_name')
            email = serializer.data.get('email')
            subject = serializer.data.get('subject')
            content = serializer.data.get('content')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        models.ContactUs.objects.create(full_name=full_name, email=email,subject=subject,  content=content)

        return Response({'status': 'OK'}, status=status.HTTP_200_OK)



class MakeRate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = serializers.MakeRateSerializer(data=request.data)
        if serializer.is_valid():
            user_score = serializer.data.get('user_score')
            slug = serializer.data.get('slug')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        id = self.request.user
        book = get_object_or_404(Book, status='p', slug=slug)
        
        # check for existing score by this user for this book
        if(models.Score.objects.filter(user=id).filter(book=book)):

            # update user score
            models.Score.objects.filter(user=id).filter(book=book).update(user=id, book=book, user_score=user_score)
        else:
            # make user score
            models.Score.objects.create(user=id, book=book, user_score=user_score)
        
        books = Book.objects.filter(status='p', slug=slug)

        for book in books:
            userScore = Score.objects.filter(book=book.id)

            # update book rates and book score 

            score_data = [] 
            for score in userScore:
                score_data.append({
                    'user_score': score.user_score
                })
            
            total_score = 0
            number_of_score = 0
            for score in score_data:
                total_score = total_score + score['user_score']
                number_of_score = number_of_score + 1
            
            if(number_of_score == 0):
                average_score = 'N/A'
            else:
                average_score = total_score / number_of_score
                average_score = "{:.1f}".format(average_score)

            # update book score
            Book.objects.filter(status='p', slug=book.slug).update(score=average_score)

            # update rates
            rates = Score.objects.filter(book=book.id).count()
            Book.objects.filter(status='p', slug=book.slug).update(rates=rates)

        return Response({'status': 'OK'}, status=status.HTTP_200_OK)



class AddOrRemoveFromReadlist(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = serializers.SlugSerializer(data=request.data)
        if serializer.is_valid():
            slug = serializer.data.get('slug')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        username = self.request.user.username

        user = get_object_or_404(User, username=username)

        book = get_object_or_404(Book, status='p', slug=slug)

        # check : add if book isn't exist and remove when it exist.
        readlist_book = user.readlist.filter(status='p')
        data = []
        for b in readlist_book:
            data.append(b.slug)

        add_to_readlist = False
        if(len(data)):
            for a in data:
                if(a == book.slug):
                    user.readlist.remove(book.id)
                    add_to_readlist = False
                    break
                else:
                    add_to_readlist = True
        else:
            add_to_readlist = True
        
        if(add_to_readlist):
            user.readlist.add(book.id)
    
        return Response({'status': 'OK'}, status=status.HTTP_200_OK)



class MakeComment(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):

        serializer = serializers.MakeCommentSerializer(data=request.data)
        if serializer.is_valid():
            content = serializer.data.get('content')
            slug = serializer.data.get('slug')
            id = serializer.data.get('id')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = self.request.user
        book = get_object_or_404(Book, status='p', slug=slug)

        # id is for reply comment (reply to comment with that id). if id was 0 then the comment is not a reply comment.
        if(id):
            reply_to = get_object_or_404(Comment, id=id)
            cum = Comment.objects.create(user=user, book=book, content=content, reply_to=reply_to)
            reply_to.comments_reply.add(cum.id)
        else:
            Comment.objects.create(user=user, book=book, content=content)

        return Response({'status': 'OK'}, status=status.HTTP_200_OK)



class ShowComment(APIView): 

    def post(self, request):

        serializer = serializers.SlugSerializer(data=request.data)
        if serializer.is_valid():
            slug = serializer.data.get('slug')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        book = get_object_or_404(Book, status='p', slug=slug)
        
        comments = Comment.objects.filter(book=book).order_by('-like', 'dis_like')

        data = []
        for comment in comments:
            data.append({
                'username': comment.user.get_full_name() if comment.user.get_full_name() else comment.user.username,
                'username_slug': comment.user.username,
                'content': comment.content,
                'comments_reply': [{
                    
                    'username': cum.user.get_full_name() if cum.user.get_full_name() else cum.user.username, 
                    'username_slug': cum.user.username,
                    'content': cum.content,
                    'like': cum.like,
                    'dis_like': cum.dis_like,
                    'date': datetime2jalali(cum.date).strftime('14%y/%m/%d _ %H:%M'),

                } for cum in comment.comments_reply.all()],
                'reply_to': comment.reply_to.id if comment.reply_to else 'null',
                'id': comment.id,
                'like': comment.like,
                'dis_like': comment.dis_like,
                'date': datetime2jalali(comment.date).strftime('14%y/%m/%d _ %H:%M'),
                'date_for_filter': datetime2jalali(comment.date).strftime('14%y%m%d%H%M'),
            })
        
        return Response({'status': 'OK', 'data': data}, status=status.HTTP_200_OK)



class LikeComment(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = serializers.LikeCommentSerializer(data=request.data)
        if serializer.is_valid():
            id = serializer.data.get('id')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = self.request.user

        comment = get_object_or_404(Comment, id=id)

        # check user like or dislike this comment before or not
        if(Like.objects.filter(user=user).filter(comment=comment)):

            # check user like this comment before or dislike it
            if(Like.objects.filter(user=user).filter(comment=comment).filter(status='l')):

                return Response({'status': 'you like this comment before'})

            else:

                Like.objects.filter(user=user, comment=comment).update(status='l')

                # set total likes and dislikes for this comment
                likes = Like.objects.filter(comment=comment).filter(status='l').count()
                dis_likes = Like.objects.filter(comment=comment).filter(status='d').count()
                Comment.objects.filter(id=id).update(like=likes, dis_like=dis_likes)

                return Response({'status': 'you changed your status from dis_like to like'})

        else:       
            Like.objects.create(user=user, comment=comment, status='l')
        
        # set total likes for this comment
        likes = Like.objects.filter(comment=comment).filter(status='l').count()
        Comment.objects.filter(id=id).update(like=likes)

        return Response({'status': 'OK'}, status=status.HTTP_200_OK) 



class DisLikeComment(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = serializers.LikeCommentSerializer(data=request.data)
        if serializer.is_valid():
            id = serializer.data.get('id')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = self.request.user

        comment = get_object_or_404(Comment, id=id)

        # check user like or dislike this comment before or not
        if(Like.objects.filter(user=user).filter(comment=comment)):

            # check user like this comment before or dislike it
            if(Like.objects.filter(user=user).filter(comment=comment).filter(status='d')):

                return Response({'status': 'you dis_like this comment before'})

            else:
                
                Like.objects.filter(user=user, comment=comment).update(status='d')

                # set total likes and dislikes for this comment
                likes = Like.objects.filter(comment=comment).filter(status='l').count()
                dis_likes = Like.objects.filter(comment=comment).filter(status='d').count()
                Comment.objects.filter(id=id).update(like=likes, dis_like=dis_likes)

                return Response({'status': 'you changed your status from like to dis_like'})

        else:
            Like.objects.create(user=user, comment=comment, status='d')
        
        # set total dislikes for this comment
        dis_likes = Like.objects.filter(comment=comment).filter(status='d').count()
        Comment.objects.filter(id=id).update(dis_like=dis_likes)

        return Response({'status': 'OK'}, status=status.HTTP_200_OK) 



class ShowUserComment(APIView):

    def post(self, request):

        serializer = serializers.SlugSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('slug')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = get_object_or_404(User, username=username)
        
        comments = Comment.objects.filter(user=user.id)

        data = []
        for comment in comments:
            data.append({
                'username': comment.user.get_full_name() if comment.user.get_full_name() else comment.user.username,
                'book_title': comment.book.title,
                'book_slug': comment.book.slug,
                'content': comment.content,
                'like': comment.like,
                'dis_like': comment.dis_like,
                'date': datetime2jalali(comment.date).strftime('14%y/%m/%d _ %H:%M'),
                'date_for_filter': datetime2jalali(comment.date).strftime('14%y%m%d%H%M'),
            })
        
        user_images_data = [{
            'image': user.image.url if user.image else 'null',
            'thumbnail': user.thumbnail.url if user.thumbnail else 'null',
            'full_name': user.get_full_name() if user.get_full_name() else user.username
        }]

        return Response({'status': 'OK', 'data': data, 'user_images_data': user_images_data}, status=status.HTTP_200_OK) 



class ShowUserVotes(APIView):

    def post(self, request):

        serializer = serializers.SlugSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('slug')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        id = self.request.user.id

        user = get_object_or_404(User, username=username, public_score=True)

        scores = Score.objects.filter(user=user).order_by('-id')

        data = []
        for score in scores:

            # check : this book exit in readlist or not
            in_readlist = False
            if(self.request.user.is_authenticated):
                user = get_object_or_404(User, id=id)
                if(user.readlist.filter(status='p', slug=score.book.slug)):
                    in_readlist = True

            # user score
            user_score_queryset = Score.objects.filter(book=score.book.id).filter(user=id)
            user_score = ''
            for user in user_score_queryset:
                user_score = user.user_score


            data.append({
                'title': score.book.title,
                'description': score.book.description,
                'slug': score.book.slug,
                'thumbnail': score.book.thumbnail.url,
                'user_score': user_score,
                'score': score.book.score,
                'rates': score.book.rates,
                'in_readlist': in_readlist,
                'target_user_score': score.user_score
            })
            user_score = ''

        return Response({'status': 'OK', 'data': data}, status=status.HTTP_200_OK) 



class AddReport(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = serializers.ReportSerializer(data=request.data)
        if serializer.is_valid():
            id = serializer.data.get('id')
            cause = serializer.data.get('cause')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = request.user

        comment = get_object_or_404(Comment, id=id)

        Report.objects.create(user=user, comment=comment, cause=cause)

        return Response({'status': 'ok'}, status=status.HTTP_200_OK)



class Search(APIView):
    def post(self, request):

        serializer = serializers.SlugSerializer(data=request.data)
        if serializer.is_valid():
            query_search = serializer.data.get('slug')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        # search in author and book and reviewed book
        results_book = Book.objects.filter(Q(title__icontains=query_search))[:3]
        results_author = Author.objects.filter(Q(full_name__icontains=query_search))[:3]
        results_reviewed_book = Reviewed_Book.objects.filter(Q(title__icontains=query_search))[:3]

        data_book = []
        for book in results_book:
            data_book.append({
                'title': book.title,
                'slug': '/book/{}'.format(book.slug),
                'badge': 'کتاب',
                'author': [a.full_name for a in book.author.filter(status='p')]
            })

        data_author = []
        for author in results_author:
            data_author.append({
                'title': author.full_name,
                'slug': '/author/{}'.format(author.slug),
                'badge': 'نویسنده'
            })

        data_reviewed_book = []
        for reviewed_book in results_reviewed_book:
            data_reviewed_book.append({
                'title': reviewed_book.title,
                'slug': '/reviewed-book/{}'.format(reviewed_book.slug),
                'badge': 'نقد و بررسی'
            })
        
        data = {
            'results_book': data_book,
            'results_author': data_author,
            'results_reviewed_book': data_reviewed_book,
        }


        return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)



class SendEmail(APIView):

    def post(self, request):

        serializer = serializers.SendEmailSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            email = serializer.data.get('email')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        # generate a token
        unique_id = get_random_string(length=32)

        # check for existing user
        if(User.objects.filter(username=username)):
            User.objects.filter(username=username).update(is_active=False, token=unique_id)
        else:
            return Response({'status': 'User is not exist'}, status=status.HTTP_404_NOT_FOUND)
            
        subject = 'تایید ایمیل در کتاب خوار'
        message = 'برای تایید حساب در سایت کتاب خوار خود روی لینک زیر کلیک کنید <br> {}email-verify/{}'.format(base_url, unique_id)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, '', email_from, recipient_list , html_message=message)

        return Response({'status': 'OK'}, status=status.HTTP_200_OK) 



class VerifyEmail(APIView):

    def post(self, request):

        serializer = serializers.SlugSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.data.get('slug')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

        
        if(User.objects.filter(token=token)):
            User.objects.filter(token=token).update(is_active=True, token='')
        else:
            return Response({'status': 'token is not exist or expired'}, status=status.HTTP_404_NOT_FOUND)
        

        return Response({'status': 'OK'}, status=status.HTTP_200_OK) 
    


# ========================
# author panel views
# ========================

class ShowBooksPanel(APIView):
    permission_classes = [IsAuthenticated&IsAuthor]

    def get(self, request):

        username = request.user.username

        books = Book.objects.all().order_by('-date')

        data = []
        for book in books:

            # for show book to author, he is must be the writer of the book or book status should be publish
            if book.status == 'd' or book.status == 's':
                if book.written_by.username != username:
                    continue


            data.append({
                'title': book.title,
                'score': book.score,
                'rates': book.rates,
                'slug': book.slug,
                'category': [a.title for a in book.category.all()],
                'author': [a.full_name for a in book.author.all()],
                'status': book.status,
                'written_by': book.written_by.get_full_name() if book.written_by.get_full_name() else book.written_by.username,
                'written_by_username': book.written_by.username,
            })
        
        return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)



class ShowNewsPanel(APIView):
    permission_classes = [IsAuthenticated&IsAuthor]

    def get(self, request):

        username = request.user.username

        news = News.objects.all().order_by('-date')

        data = []
        for n in news:

            # for show book to author, he is must be the writer of the book or book status should be publish
            if n.status == 'd' or n.status == 's':
                if n.written_by.username != username:
                    continue

            data.append({
                'title': n.title,
                'description': n.description,
                'slug': n.slug,
                'date': datetime2jalali(n.date).strftime('14%y/%m/%d _ %H:%M'),
                'status': n.status,
                'written_by': n.written_by.get_full_name() if n.written_by.get_full_name() else n.written_by.username,
                'written_by_username': n.written_by.username,
            })
        
        return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)



class ShowQuotesPanel(APIView):
    permission_classes = [IsAuthenticated&IsAuthor]
    
    def get(self, request):

        username = request.user.username

        quotes = Quote.objects.all().order_by('-date')

        data = []
        for quote in quotes:

            # for show book to author, he is must be the writer of the book or book status should be publish
            if quote.status == 'd' or quote.status == 's':
                if quote.written_by.username != username:
                    continue

            data.append({
                'author': quote.author,
                'description': quote.description,
                'status': quote.status,
                'written_by': quote.written_by.get_full_name() if quote.written_by.get_full_name() else quote.written_by.username,
                'written_by_username': quote.written_by.username,
            })

        return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)



class ShowCategoriesPanel(APIView):
    permission_classes = [IsAuthenticated&IsAuthor]

    def get(self, request):

        username = request.user.username

        categories = Category.objects.all().order_by('-date')

        data = []
        for category in categories:

            # for show book to author, he is must be the writer of the book or book status should be publish
            if category.status == 'd' or category.status == 's':
                if category.written_by.username != username:
                    continue

            data.append({
                'title': category.title,
                'slug': category.slug,
                'status': category.status,
                'written_by': category.written_by.get_full_name() if category.written_by.get_full_name() else category.written_by.username,
                'written_by_username': category.written_by.username,
            })
        

        return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)



class ShowAuthorsPanel(APIView):
    permission_classes = [IsAuthenticated&IsAuthor]

    def get(self, request):

        username = request.user.username

        authors = Author.objects.all().order_by('-date')

        data = []
        for author in authors:

            # for show book to author, he is must be the writer of the book or book status should be publish
            if author.status == 'd' or author.status == 's':
                if author.written_by.username != username:
                    continue

            data.append({
                'full_name': author.full_name,
                'slug': author.slug,
                'related_category': [[a.title, a.slug] for a in author.related_category.all()],
                'status': author.status,
                'written_by': author.written_by.get_full_name() if author.written_by.get_full_name() else author.written_by.username,
                'written_by_username': author.written_by.username,
            })
        

        return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)



class ShowReviewedBooksPanel(APIView):
    permission_classes = [IsAuthenticated&IsAuthor]
    
    def get(self, request):

        username = request.user.username

        books = Reviewed_Book.objects.all().order_by('-date')

        data = []
        for book in books:

            # for show book to author, he is must be the writer of the book or book status should be publish
            if book.status == 'd' or book.status == 's':
                if book.critic.username != username:
                    continue

            data.append({
                'title': book.title,
                'author': [[a.full_name, a.slug] for a in book.author.all()],
                'category': [[a.title, a.slug] for a in book.category.all()],
                'slug': book.slug,
                'status': book.status,
                'critic': book.critic.get_full_name() if book.critic.get_full_name() else book.critic.username,
                'critic_username': book.critic.username,
            })
        

        return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)



#########################
# create panel views
#########################

class AddBookPanel(APIView):
    permission_classes = [IsAuthenticated&IsAuthor]

    def post(self, request):

        serializer = serializers.AddBookPanelSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.data.get('title')
            slug = serializer.data.get('slug')
            description = serializer.data.get('description')
            content = serializer.data.get('content')
            stat = serializer.data.get('status')
            author = serializer.data.get('author')
            category = serializer.data.get('category')
            thumbnail = request.FILES.get('thumbnail')
            image = request.FILES.get('image')

            # check for correct author & category
            if author[0] == 'undefined' or category[0] == 'undefined' or author[0] == '' or category[0] == '':
                return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
            
            # check for correct status. the writer can't choose the publish status
            if stat != 'd':
                if stat != 's':
                    return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
                
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
                
        user = self.request.user

        # check for existing book with this slug
        if Book.objects.filter(slug=slug):

            # if book status would be draft, the writer can update the information
            if Book.objects.filter(written_by=user).filter(status='d'):

                Book.objects.filter(slug=slug).update(title=title, slug=slug, description=description ,content=content ,written_by=user, status=stat)
                sample = get_object_or_404(Book, slug=slug)
                sample.thumbnail.save(thumbnail.name, thumbnail)
                sample.image.save(image.name, image)

                for a in author[0].split(','):
                    sample.author.add(a)
            
                for a in category[0].split(','):
                    sample.category.add(a)

            else:
                return Response({'status': 'this slug already exist'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:

            # create new book 
            b = Book(title=title, slug=slug, description=description ,content=content ,written_by=user, status=stat)
            b.thumbnail.save(thumbnail.name, thumbnail)
            b.image.save(image.name, image)
            for a in author[0].split(','):
                b.author.add(a)
        
            for a in category[0].split(','):
                b.category.add(a)

        return Response({'status': 'ok'}, status=status.HTTP_200_OK)



class AddAuthorPanel(APIView):
    permission_classes = [IsAuthenticated&IsAuthor]

    def post(self, request):

        serializer = serializers.AddAuthorPanelSerializer(data=request.data)
        if serializer.is_valid():
            full_name = serializer.data.get('fullName')
            slug = serializer.data.get('slug')
            description = serializer.data.get('description')
            content = serializer.data.get('content')
            stat = serializer.data.get('status')
            category = serializer.data.get('category')
            thumbnail = request.FILES.get('thumbnail')
            image = request.FILES.get('image')

            # check for correct category
            if category[0] == 'undefined' or category[0] == '':
                return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
            
            # check for correct status. the writer can't choose the publish status
            if stat != 'd':
                if stat != 's':
                    return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = self.request.user

        # check for existing author with this slug
        if Author.objects.filter(slug=slug):

            # if book status would be draft, the writer can update the information
            if Author.objects.filter(written_by=user).filter(status='d'):

                Author.objects.filter(slug=slug).update(full_name=full_name, slug=slug, description=description ,content=content ,written_by=user, status=stat)
                sample = get_object_or_404(Author, slug=slug)
                sample.thumbnail.save(thumbnail.name, thumbnail)
                sample.image.save(image.name, image)

                for a in category[0].split(','):
                    sample.related_category.add(a)

            else:
                return Response({'status': 'this slug already exist'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:

            # create new author 
            b = Author(full_name=full_name, slug=slug, description=description ,content=content ,written_by=user, status=stat)
            b.thumbnail.save(thumbnail.name, thumbnail)
            b.image.save(image.name, image)
            for a in category[0].split(','):
                b.related_category.add(a)

        return Response({'status': 'ok'}, status=status.HTTP_200_OK)



class AddCategoryPanel(APIView):
    permission_classes = [IsAuthenticated&IsAuthor]

    def post(self, request):

        serializer = serializers.AddCategoryPanelSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.data.get('title')
            slug = serializer.data.get('slug')
            description = serializer.data.get('description')
            content = serializer.data.get('content')
            stat = serializer.data.get('status')
            author = serializer.data.get('author')
            thumbnail = request.FILES.get('thumbnail')
            image = request.FILES.get('image')

            # check for correct author
            if author[0] == 'undefined' or author[0] == '':
                return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
            
            # check for correct status. the writer can't choose publish status
            if stat != 'd':
                if stat != 's':
                    return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = self.request.user

        # check for existing category with this slug
        if Category.objects.filter(slug=slug):

            # if category status would be draft, the writer can update the information
            if Category.objects.filter(written_by=user).filter(status='d'):

                Category.objects.filter(slug=slug).update(title=title, slug=slug, description=description ,content=content ,written_by=user, status=stat)
                sample = get_object_or_404(Category, slug=slug)
                sample.thumbnail.save(thumbnail.name, thumbnail)
                sample.image.save(image.name, image)

                for a in author[0].split(','):
                    sample.related_author.add(a)

            else:
                return Response({'status': 'this slug already exist'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:

            # create new category 
            b = Category(title=title, slug=slug, description=description ,content=content ,written_by=user, status=stat)
            b.thumbnail.save(thumbnail.name, thumbnail)
            b.image.save(image.name, image)
            for a in author[0].split(','):
                b.related_author.add(a)

        return Response({'status': 'ok'}, status=status.HTTP_200_OK)



class AddReviewedBookPanel(APIView):
    permission_classes = [IsAuthenticated&IsAuthor]

    def post(self, request):

        serializer = serializers.AddBookPanelSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.data.get('title')
            slug = serializer.data.get('slug')
            description = serializer.data.get('description')
            content = serializer.data.get('content')
            stat = serializer.data.get('status')
            thumbnail = request.FILES.get('thumbnail')
            image = request.FILES.get('image')
            author = serializer.data.get('author')
            category = serializer.data.get('category')

            # check for correct author & category
            if author[0] == 'undefined' or category[0] == 'undefined' or author[0] == '' or category[0] == '':
                return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
            
            # check for correct status. the writer can't choose publish status
            if stat != 'd':
                if stat != 's':
                    return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
                
        user = self.request.user

        # check for existing reviewed book with this slug
        if Reviewed_Book.objects.filter(slug=slug):

            # if reviewed book status would be draft, the writer can update the information
            if Reviewed_Book.objects.filter(critic=user).filter(status='d'):

                Reviewed_Book.objects.filter(slug=slug).update(title=title, slug=slug, description=description ,content=content ,critic=user, status=stat)
                sample = get_object_or_404(Reviewed_Book, slug=slug)
                sample.thumbnail.save(thumbnail.name, thumbnail)
                sample.image.save(image.name, image)

                for a in author[0].split(','):
                    sample.author.add(a)
            
                for a in category[0].split(','):
                    sample.category.add(a)

            else:
                return Response({'status': 'this slug already exist'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:

            # create new reviewed book 
            b = Reviewed_Book(title=title, slug=slug, description=description ,content=content ,critic=user, status=stat)
            b.thumbnail.save(thumbnail.name, thumbnail)
            b.image.save(image.name, image)
            for a in author[0].split(','):
                b.author.add(a)
        
            for a in category[0].split(','):
                b.category.add(a)

        return Response({'status': 'ok'}, status=status.HTTP_200_OK)



class AddNewsPanel(APIView):
    permission_classes = [IsAuthenticated&IsAuthor]

    def post(self, request):

        serializer = serializers.AddNewsPanelSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.data.get('title')
            slug = serializer.data.get('slug')
            description = serializer.data.get('description')
            content = serializer.data.get('content')
            stat = serializer.data.get('status')
            image = request.FILES.get('image')

            # check for correct status. the writer can't choose publish status
            if stat != 'd':
                if stat != 's':
                    return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = self.request.user

        # check for existing news with this slug
        if News.objects.filter(slug=slug):

            # if news status would be draft, the writer can update the information
            if News.objects.filter(written_by=user).filter(status='d'):

                News.objects.filter(slug=slug).update(title=title, slug=slug, description=description ,content=content ,written_by=user, status=stat)
                sample = get_object_or_404(News, slug=slug)
                sample.image.save(image.name, image)

            else:
                return Response({'status': 'this slug already exist'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:

            # create new news
            b = News(title=title, slug=slug, description=description ,content=content ,written_by=user, status=stat)
            b.image.save(image.name, image)

        return Response({'status': 'ok'}, status=status.HTTP_200_OK)



class AddQuotePanel(APIView):
    permission_classes = [IsAuthenticated&IsAuthor]

    def post(self, request):

        serializer = serializers.AddQuotePanelSerializer(data=request.data)
        if serializer.is_valid():
            author = serializer.data.get('fullName')
            description = serializer.data.get('description')
            thumbnail = request.FILES.get('thumbnail')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = self.request.user

        # create new quote
        b = Quote(author=author, description=description ,written_by=user, status='d')
        b.thumbnail.save(thumbnail.name, thumbnail)

        return Response({'status': 'ok'}, status=status.HTTP_200_OK)


# edit panel views
class ShowSingleBookEditPanel(APIView):
    permission_classes = [IsAuthenticated&IsAuthor]

    def post(self, request):

        serializer = serializers.SlugSerializer(data=request.data)
        if serializer.is_valid():
            slug = serializer.data.get('slug')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        books = get_object_or_404(Book, slug=slug)

        book = Book.objects.filter(slug=slug)

        username = request.user.username

        # show if status is draft or the user is the writer
        if books.status == 'd' and books.written_by.username == username:
            data = []
            for b in book:
                data.append({
                    'title': b.title,
                    'slug': b.slug,
                    'content': b.content,
                    'description': b.description,
                })
        else:
            return Response({'status': 'you can not see this book'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)



class ShowSingleAuthorEditPanel(APIView):
    permission_classes = [IsAuthenticated&IsAuthor]

    def post(self, request):

        serializer = serializers.SlugSerializer(data=request.data)
        if serializer.is_valid():
            slug = serializer.data.get('slug')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        authors = get_object_or_404(Author, slug=slug)

        author = Author.objects.filter(slug=slug)

        username = request.user.username

        # show if status is draft or the user is the writer
        if authors.status == 'd' and authors.written_by.username == username:
            data = []
            for b in author:
                data.append({
                    'full_name': b.full_name,
                    'slug': b.slug,
                    'content': b.content,
                    'description': b.description,
                })
        else:
            return Response({'status': 'you can not see this author'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)



class ShowSingleCategoryEditPanel(APIView):
    permission_classes = [IsAuthenticated&IsAuthor]

    def post(self, request):

        serializer = serializers.SlugSerializer(data=request.data)
        if serializer.is_valid():
            slug = serializer.data.get('slug')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        categories = get_object_or_404(Category, slug=slug)

        category = Category.objects.filter(slug=slug)

        username = request.user.username

        # show if status is draft or the user is the writer
        if categories.status == 'd' and categories.written_by.username == username:
            data = []
            for b in category:
                data.append({
                    'title': b.title,
                    'slug': b.slug,
                    'content': b.content,
                    'description': b.description,
                })
        else:
            return Response({'status': 'you can not see this author'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)



class ShowSingleReviewedBookEditPanel(APIView):
    permission_classes = [IsAuthenticated&IsAuthor]

    def post(self, request):

        serializer = serializers.SlugSerializer(data=request.data)
        if serializer.is_valid():
            slug = serializer.data.get('slug')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        books = get_object_or_404(Reviewed_Book, slug=slug)

        book = Reviewed_Book.objects.filter(slug=slug)

        username = request.user.username

        # show if status is draft or the user is the writer
        if books.status == 'd' and books.critic.username == username:
            data = []
            for b in book:
                data.append({
                    'title': b.title,
                    'slug': b.slug,
                    'content': b.content,
                    'description': b.description,
                })
        else:
            return Response({'status': 'you can not see this book'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)



class ShowSingleNewsEditPanel(APIView):
    permission_classes = [IsAuthenticated&IsAuthor]

    def post(self, request):

        serializer = serializers.SlugSerializer(data=request.data)
        if serializer.is_valid():
            slug = serializer.data.get('slug')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        n = get_object_or_404(News, slug=slug)

        news = News.objects.filter(slug=slug)

        username = request.user.username

        # show if status is draft or the user is the writer
        if n.status == 'd' and n.written_by.username == username:
            data = []
            for b in news:
                data.append({
                    'title': b.title,
                    'slug': b.slug,
                    'content': b.content,
                    'description': b.description,
                })
        else:
            return Response({'status': 'you can not see this book'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)
