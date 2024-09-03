from django.contrib import admin
from .models import (Author, Book, ContactUs, Reviewed_Book, 
                        User, Category, Quote, News, 
                        Score, Comment, Like, Report
                    )



class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'written_by', 'status', 'score', 'rates')
    search_fields = ['title', 'slug', 'written_by']

admin.site.register(Book, BookAdmin)



class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'slug', 'written_by', 'popular_author', 'status')
    search_fields = ['full_name', 'written_by']

admin.site.register(Author, AuthorAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'written_by', 'popular_category', 'status')
    search_fields = ['title', 'written_by']

admin.site.register(Category, CategoryAdmin)



class QuoteAdmin(admin.ModelAdmin):
    list_display = ('author', 'written_by', 'status')
    search_fields = ['author', 'written_by']

admin.site.register(Quote, QuoteAdmin)



class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'written_by', 'status')
    search_fields = ['title', 'written_by']

admin.site.register(News, NewsAdmin)



class Reviewed_BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'critic', 'status')
    search_fields = ['title', 'slug', 'critic']

admin.site.register(Reviewed_Book, Reviewed_BookAdmin)



class ScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'user_score')

admin.site.register(Score, ScoreAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'subject', 'seen')
    search_fields = ['full_name', 'subject']

admin.site.register(ContactUs, ContactUsAdmin)



class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'reply_to',)
    search_fields = ['user', 'book']

admin.site.register(Comment, CommentAdmin)


class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'status',)
    search_fields = ['user', 'comment']

admin.site.register(Like, LikeAdmin)



class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_active', 'is_author')

admin.site.register(User, UserAdmin)



class ReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment')

admin.site.register(Report, ReportAdmin)