from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from . import serializers ,models
from knox.models import AuthToken
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.viewsets import ModelViewSet


class LoginAPI(generics.GenericAPIView):
    serializer_class = serializers.LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": serializers.UserSerializerWithProfile(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class RegisterAPI(generics.GenericAPIView):
    serializer_class = serializers.RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": serializers.UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class UserAPI(generics.RetrieveAPIView,):
    # permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.UserSerializerWithProfile

    def get_object(self):
        return self.request.user


class ProfileAPI (generics.RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.ProfileSerializerWithUser

    def get_object(self):
        return self.request.user


class UpdateUserApi(generics.RetrieveUpdateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.ProfileSerializerWithUser

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = serializers.ChangePasswordSerializer
    model = User
    # permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
