from django.contrib import admin
from .models import Author, Book, ContactUs, Reviewed_Book, User, Category, Quote, News, Score, Comment, Like



admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Quote)
admin.site.register(News)
admin.site.register(Reviewed_Book)





class ScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'user_score')

admin.site.register(Score, ScoreAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'subject', 'seen')
    search_fields = ['full_name', 'subject']

admin.site.register(ContactUs, ContactUsAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'score', 'rates')
    search_fields = ['title', 'slug', 'score', 'rates']

admin.site.register(Book, BookAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'reply_to',)
    search_fields = ['user', 'book']

admin.site.register(Comment, CommentAdmin)


class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'status',)
    search_fields = ['user', 'comment']

admin.site.register(Like, LikeAdmin)



class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_active', 'token')

admin.site.register(User, UserAdmin)
