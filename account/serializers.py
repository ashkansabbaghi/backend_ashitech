from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Profile
from django.utils import timezone


# User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# profile
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        # fields = '__all__'
        fields = ('user', 'bio', 'mobile', 'image')
        read_only_fields = ['created_at', 'updated_at']

# profile serializer with user
class ProfileSerializerWithUser(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        # fields = '__all__'
        fields = ('user', 'bio', 'mobile', 'image')
        read_only_fields = ['created_at', 'updated_at']

# user serializer with profile
class UserSerializerWithProfile(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ('id', 'username', 'email','profile')


# User Serializer update
class UserSerializerUpdate(serializers.ModelSerializer):
    # profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        # fields = '__all__'

    # def create(self,validated_data):
    #     obj = super().create(validated_data)
    #     # obj.created_at = timezone.now()
    #     obj.save()
    #     return obj

    # def update(self,instance,validated_data):
    #     # old_created_at = instance.created_at

    #     obj = super().update(instance,validated_data)
    #     # obj.created_at = old_created_at
    #     # obj.updated_at = timezone.now()
    #     obj.save()
    #     return obj


# profile serializers update
class ProfileSerializerUpdate(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = Profile
        # fields = '__all__'
        fields = ('user', 'bio', 'mobile')
        read_only_fields = ['created_at', 'updated_at']

    # def create(self, validated_data):
    #     obj = super().create(validated_data)
    #     obj.created_at = timezone.now()
    #     obj.save()
    #     return obj

    # def update(self, instance, validated_data):
    #     old_created_at = instance.created_at

    #     obj = super().update(instance, validated_data)
    #     obj.created_at = old_created_at
    #     obj.updated_at = timezone.now()
    #     obj.save()
    #     return obj


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])

        return user


# Change Password
class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


# login user
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Details.")
