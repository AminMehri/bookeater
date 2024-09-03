from rest_framework import serializers
from .models import Book, Author, Category



class SlugSerializer(serializers.Serializer):
    slug = serializers.CharField()



class ContactUsSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    email = serializers.EmailField()
    subject = serializers.CharField()
    content = serializers.CharField()



class MakeRateSerializer(serializers.Serializer):
    user_score = serializers.IntegerField()
    slug = serializers.CharField()



class MakeCommentSerializer(serializers.Serializer):
    content = serializers.CharField()
    slug = serializers.CharField()
    id = serializers.IntegerField(allow_null=True)



class LikeCommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(allow_null=True)



class SendEmailSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()



class GetProfileInformationSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    age = serializers.IntegerField()
    public_score = serializers.BooleanField()
    sex = serializers.CharField()
    thumbnail = serializers.ImageField(required=False)
    image = serializers.ImageField(required=False)



class ReportSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    cause = serializers.CharField()


# =============================
# author panel serializers
# =============================

class AddBookPanelSerializer(serializers.Serializer):
    title = serializers.CharField()
    slug = serializers.SlugField()
    author = serializers.ListField()
    category = serializers.ListField()
    description = serializers.CharField()
    content = serializers.CharField()
    status = serializers.CharField()
    thumbnail = serializers.ImageField()
    image = serializers.ImageField()



class AddAuthorPanelSerializer(serializers.Serializer):
    fullName = serializers.CharField()
    slug = serializers.SlugField()
    category = serializers.ListField()
    description = serializers.CharField()
    content = serializers.CharField()
    status = serializers.CharField()
    thumbnail = serializers.ImageField()
    image = serializers.ImageField()



class AddCategoryPanelSerializer(serializers.Serializer):
    title = serializers.CharField()
    slug = serializers.SlugField()
    author = serializers.ListField()
    description = serializers.CharField()
    content = serializers.CharField()
    status = serializers.CharField()
    thumbnail = serializers.ImageField()
    image = serializers.ImageField()



class AddNewsPanelSerializer(serializers.Serializer):
    title = serializers.CharField()
    slug = serializers.SlugField()
    description = serializers.CharField()
    status = serializers.CharField()
    content = serializers.CharField()
    image = serializers.ImageField()



class AddQuotePanelSerializer(serializers.Serializer):
    fullName = serializers.CharField()
    description = serializers.CharField()
    thumbnail = serializers.ImageField()
