# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from comm.utils.common import json_loads


class JSONField(models.TextField):
    """ defined JSON Field """
    description = _("JSON")

    def get_internal_type(self):
        return "JSONField"

    def to_python(self, value):
        value = super(JSONField, self).to_python(value)
        return json_loads(value)


# Create your models here.
class ModelBase(models.Model):
    """ the model base """
    id = models.AutoField(primary_key=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)
    is_valid = models.BooleanField('逻辑删除字段', default=True)

    class Meta:
        abstract = True


class Category(ModelBase):
    """
    博客分类
    """
    name = models.CharField('名称', max_length=50)

    def __unicode__(self):
        return self.name

    __str__ = __unicode__


class Tag(ModelBase):
    """ 标签 """
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    __str__ = __unicode__


class Blog(ModelBase):
    """ 博文 """
    STATUS_DRAFT = 1
    STATUS_PUBLISH = 2
    STATUS_OFFLINE = 3

    STATUS_TEXT = {
        STATUS_DRAFT: '草稿箱',
        STATUS_PUBLISH: '发布中',
        STATUS_OFFLINE: '已下线'
    }

    title = models.CharField(verbose_name='标题', max_length=80)
    author = models.CharField(verbose_name='作者', max_length=32)
    content = models.TextField(verbose_name='博客正文')
    categories = models.ManyToManyField(Category, verbose_name='分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    status = models.SmallIntegerField(verbose_name='状态', default=STATUS_PUBLISH)
    commentable = models.BooleanField(verbose_name='可评论', default=True)
    summary = models.CharField(verbose_name='文章摘要', max_length=2048, null=True)
    visitors = models.BigIntegerField(verbose_name='访问量', default=0)

    class Meta:
        ordering = ('-created_time', )

    def __unicode__(self):
        return self.title

    __str__ = __unicode__


class Comment(ModelBase):
    """
    评论
    """
    blog = models.ForeignKey(Blog, verbose_name='博客', related_name="comments")
    name = models.CharField(verbose_name='称呼', max_length=64)
    email = models.EmailField(verbose_name='邮箱')
    comment = models.ForeignKey(u'self', related_name=u'comments', verbose_name='评论的评论', null=True)
    content = models.CharField('内容', max_length=480)

    class Meta:
        ordering = ('-id', )
        verbose_name = '评论'
        verbose_name_plural = '评论'

    def __unicode__(self):
        return self.content

    __str__ = __unicode__
