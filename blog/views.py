# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from rest_framework import status
from django.http.response import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from comm.utils.common import json_dumps
from serializers import BlogSerializer, TagSerializer, CategorySerializer, CommentSerializer
from models import Blog, Comment, Category, Tag

logger = logging.getLogger(__name__)


# Create your views here.
class BlogViewSet(ModelViewSet):

    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        categories = data.pop('categories', [])
        tags = data.pop('tags', [])
        category_ids = []
        tag_ids = []
        for category in categories:
            cate, _ = Category.objects.get_or_create(**category)
            category_ids.append(cate.id)
        for tag in tags:
            label, _ = Tag.objects.get_or_create(**tag)
            tag_ids.append(label.id)
        default_context = self.get_serializer_context()
        default_context.update(dict(
            categories=category_ids,
            tags=tag_ids,
        ))
        serializer = BlogSerializer(data=data, context=default_context)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return HttpResponse(json_dumps(dict(errmsg=serializer.errors, code=status.HTTP_400_BAD_REQUEST)))


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
