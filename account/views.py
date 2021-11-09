from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, permissions
from . import models
from . import serializers
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User

# list users
@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = models.User.objects.all()
        serializer = serializers.UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# list profile
@api_view(['GET', 'POST'])
def profile_list(request):
    if request.method == 'GET':
        users = models.Profile.objects.all()
        serializer = serializers.ProfileSerializerWithUser(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.ProfileSerializerWithUser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# update user
@api_view(['PUT', 'GET', 'DELETE'])
def get_update_delete_user(request, pk):
    try:
        user = models.User.objects.get(pk=pk)
    except:
        return Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ser = serializers.UserSerializerUpdate(user)
        return Response(ser.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        print('PUT ashkan')
        ser = serializers.UserSerializerUpdate(user, data=request.data)
        if ser.is_valid():
            print('valid')
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# update profile
@api_view(['PUT', 'GET', 'DELETE'])
def get_update_delete_profile(request, pk):
    try:
        user = models.Profile.objects.get(pk=pk)
    except:
        return Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ser = serializers.ProfileSerializerUpdate(user)
        return Response(ser.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        print('PUT ashitech')
        ser = serializers.ProfileSerializerUpdate(user, data=request.data)
        if ser.is_valid():
            print('valid')
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
