from rest_framework import serializers



class SlugSerializer(serializers.Serializer):
    slug = serializers.CharField(allow_null=False, allow_blank=False)



class ContactUsSerializer(serializers.Serializer):
    full_name = serializers.CharField(allow_null=False, allow_blank=False)
    email = serializers.EmailField(allow_null=False, allow_blank=False)
    subject = serializers.CharField(allow_null=False, allow_blank=False)
    content = serializers.CharField(allow_null=False, allow_blank=False)



class MakeRateSerializer(serializers.Serializer):
    user_score = serializers.IntegerField()
    slug = serializers.CharField()



class MakeCommentSerializer(serializers.Serializer):
    content = serializers.CharField(allow_null=False, allow_blank=False)
    slug = serializers.CharField(allow_null=False, allow_blank=False)
    id = serializers.IntegerField(allow_null=True)



class LikeCommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(allow_null=True)



class SendEmailSerializer(serializers.Serializer):
    username = serializers.CharField(allow_null=False, allow_blank=False)
    email = serializers.EmailField()



class GetProfileInformationSerializer(serializers.Serializer):
    first_name = serializers.CharField(allow_null=False, allow_blank=False)
    last_name = serializers.CharField(allow_null=False, allow_blank=False)
    age = serializers.IntegerField()
    public_score = serializers.BooleanField()
    sex = serializers.CharField(allow_null=False, allow_blank=False)



# =============================
# author panel serializers
# =============================

class AddBookPanelSerializer(serializers.Serializer):
    title = serializers.CharField(allow_null=False, allow_blank=False)
    slug = serializers.SlugField(allow_null=False, allow_blank=False)
    author = serializers.SlugField()
    category = serializers.SlugField()
    description = serializers.CharField(allow_null=False, allow_blank=False)
    content = serializers.CharField(allow_null=False, allow_blank=False)
    # thumbnail = serializers.ImageField(allow_null=False, allow_blank=False)
    # image = serializers.ImageField(allow_null=False, allow_blank=False)