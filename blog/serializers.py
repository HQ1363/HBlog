#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
Created on 2019/11/17 下午6:08
@author: HQ
@Blog: https://blog.csdn.net/huangqiang1363
"""
import json
import logging
import traceback

from rest_framework import serializers
from rest_framework.utils import model_meta
from django.utils.translation import ugettext_lazy as _

from models import Blog, Category, Tag, Comment

logger = logging.getLogger(__name__)


class JsonSerializer(serializers.JSONField):

    default_error_messages = {
        'invalid_json': _('无效的json数据格式')
    }

    def to_representation(self, value):
        return json.loads(value or '{}')

    def to_internal_value(self, data):
        try:
            json.loads(data)
        except (TypeError, ValueError):
            self.fail('invalid_json')
        return data


class BaseSerializer(serializers.ModelSerializer):

    created_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    updated_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    def create(self, validated_data):
        """
        overwrite create function to support foregin key save, but update dont't need
        """
        serializers.raise_errors_on_nested_writes('create', self, validated_data)

        ModelClass = self.Meta.model

        # Remove many-to-many relationships from validated_data.
        # They are not valid arguments to the default `.create()` method,
        # as they require that the instance has already been saved.
        info = model_meta.get_field_info(ModelClass)
        many_to_many = {}
        one_to_many = {}
        for field_name, relation_info in info.relations.items():
            if relation_info.to_many and (field_name in validated_data):
                many_to_many[field_name] = validated_data.pop(field_name)
            if not relation_info.to_many and (field_name in self.context):
                one_to_many[field_name] = self.context[field_name]

        try:
            if one_to_many:
                validated_data.update(one_to_many)
            instance = ModelClass._default_manager.create(**validated_data)
        except TypeError:
            tb = traceback.format_exc()
            msg = (
                'Got a `TypeError` when calling `%s.%s.create()`. '
                'This may be because you have a writable field on the '
                'serializer class that is not a valid argument to '
                '`%s.%s.create()`. You may need to make the field '
                'read-only, or override the %s.create() method to handle '
                'this correctly.\nOriginal exception was:\n %s' %
                (
                    ModelClass.__name__,
                    ModelClass._default_manager.name,
                    ModelClass.__name__,
                    ModelClass._default_manager.name,
                    self.__class__.__name__,
                    tb
                )
            )
            raise TypeError(msg)

        # Save many-to-many relationships after the instance is created.
        if many_to_many:
            for field_name, value in many_to_many.items():
                field = getattr(instance, field_name)
                field.set(value)

        return instance


class TagSerializer(BaseSerializer):

    class Meta:
        model = Tag
        fields = "__all__"


class CategorySerializer(BaseSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class CommentSerializer(BaseSerializer):

    class Meta:
        model = Comment
        fields = "__all__"


class BlogSerializer(BaseSerializer):

    tags = TagSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    comments = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Blog
        fields = "__all__"

    @staticmethod
    def get_comments(obj):
        comments = obj.comments.all()
        # get comment list, but not tree structure
        return CommentSerializer(comments, many=True).data
