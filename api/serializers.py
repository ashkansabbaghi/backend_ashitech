from rest_framework import serializers
from .models import Blog, Tag
from django.contrib.auth.models import User
from account import models


# User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')
        # fields = '__all__'

#specialty
class specialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.specialty
        fields = ('id' , 'title')

# profile
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    specialty = specialtySerializer(read_only=True, many=True)
    class Meta:
        model = models.Profile
        # fields = '__all__'
        fields = ('user','bio', 'mobile','image', 'specialty')
        read_only_fields = ['created_at', 'updated_at']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('title','slug')


class BlogSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    author = ProfileSerializer()

    class Meta:
        model = Blog
        fields = ('author', 'slug', 'tags', 'caption', 'publish','views')
        # fields = "__all__"
        read_only_fields = ('updated', 'created')
