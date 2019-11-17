# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from serializers import BlogSerializer, TagSerializer, CategorySerializer, CommentSerializer
from models import Blog, Comment, Category, Tag


# Create your views here.
class BlogViewSet(ModelViewSet):

    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


class CategoryViewSet(ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        category_name = data.get('name')
        if category_name:
            existed = Category.objects.filter(name__exact=category_name).exists()
            if not existed:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:
                return Response(
                    data=dict(errmsg=u'category has existed, not to replication'), status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data=dict(errmsg=u'lack the must parameters'), status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(ModelViewSet):

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class TagViewSet(ModelViewSet):

    serializer_class = TagSerializer
    queryset = Tag.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        category_name = data.get('name')
        if category_name:
            existed = Category.objects.filter(name__exact=category_name).exists()
            if not existed:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:
                return Response(data=dict(errmsg=u'tag has existed, not to replication'), status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data=dict(errmsg=u'lack the must parameters'), status=status.HTTP_400_BAD_REQUEST)
