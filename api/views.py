from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import generics, permissions,status
from rest_framework.response import Response



class BlogViewSet(ModelViewSet):
    queryset = Blog.published.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def detail(request, post_id):
        blog = Blog.objects.get(id=post_id)
        blog.views += 1
        blog.save()
        print("BlogViewSet/detail")
        return Response(blog.data,status=status)


# class UserViewSet(ModelViewSet):
#     # permission_classes = [permissions.IsAuthenticated, ]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
