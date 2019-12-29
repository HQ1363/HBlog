# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from blog.models import Blog, Comment, Category, Tag, UserProfile


# Register your models here.
class ProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False


class UserProfileAdmin(UserAdmin):
    inlines = [ProfileInline, ]


admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Tag)
