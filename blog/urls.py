#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
Created on 2019/11/17 下午7:55
@author: HQ
@Blog: https://blog.csdn.net/huangqiang1363
"""
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from views import BlogViewSet, CategoryViewSet, CommentViewSet, TagViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'article', BlogViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'tag', TagViewSet)
app_name = "duty"
urlpatterns = [
    url(r'^', include(router.urls)),
]
