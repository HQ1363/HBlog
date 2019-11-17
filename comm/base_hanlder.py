#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
Created on 2019/11/17 下午3:29
@author: HQ
@Blog: https://blog.csdn.net/huangqiang1363
"""
from django.db.models import Count
from datetime import datetime, date, timedelta
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection, transaction, models


class BaseHandler(object):

    def __init__(self, model):
        self.model = model

    def __getattr__(self, item):
        return getattr(self.model, item)

    def count(self, field=None, filters=None):
        if not field and not filters:
            return self.model.objects.count()
        if not field:
            if all([isinstance(condition, Q) for condition in filters]):
                return self.model.objects.filter(*filters).count()
            else:
                raise TypeError
        if not filters:
            return self.model.objects.all().values(field).annotate(count=Count(self.model.__name__)).values(field, 'count')
        return self.model.objects.filter(*filters).values(field).annotate(count=Count(self.model.__name__)).values(field, 'count')

    def all(self, start=None, end=None):
        return self.model.objects.all()[start:end]

    def create(self, permit_repeat=True, **kwargs):
        if permit_repeat:
            return self.model.objects.create(**kwargs)
        return self.model.objects.get_or_create(**kwargs)

    def exists(self, filters):
        if all([isinstance(condition, Q) for condition in filters]):
            return self.model.objects.filter(*filters).exists()
        else:
            raise TypeError

    def first(self, filters, order_by='created_time', desc=False):
        if all([isinstance(condition, Q) for condition in filters]):
            query_set = self.model.objects.filter(*filters).order_by(order_by)
            if not desc:
                return query_set.first()
            else:
                return query_set.reverse().first()
        else:
            raise TypeError

    def last(self, filters, order_by='created_time', desc=False):
        if all([isinstance(condition, Q) for condition in filters]):
            query_set = self.model.objects.filter(*filters).order_by(order_by)
            if not desc:
                return query_set.last()
            else:
                return query_set.reverse().last()
        else:
            raise TypeError

    def pagination_query(self, filters, fields=(), distinct=False, order_by='created_time',
                  desc=False, page=1, size=10):
        if all([isinstance(condition, Q) for condition in filters]):
            query = self.model.objects.filter(*filters)
            if fields and isinstance(fields, (tuple, list)) and distinct:
                query = query.distinct(fields)
            if desc:
                query = query.order_by(order_by).reverse()
            offset = (page - 1) * size
            return query[offset:offset+size]
        else:
            raise TypeError

    def bulk_create(self, obj_list, batch_size=31):
        if isinstance(obj_list, (list, tuple)):
            objs = []
            for item in obj_list:
                obj = self.model(**item)
                objs.append(obj)
            self.model.objects.bulk_create(objs, batch_size=batch_size)
        else:
            raise TypeError

    def bulk_delete(self, filters):
        if all([isinstance(condition, Q) for condition in filters]):
            # filters is q list
            return self.model.objects.filter(*filters).delete()
        else:
            # filter is kwargs map
            return self.model.objects.filter(**filters).delete()

    def bulk_update(self, filters, **update):
        if all([isinstance(condition, Q) for condition in filters]):
            return self.model.objects.filter(*filters).update(**update)
        else:
            raise TypeError

    def update_or_create(self, obj=None, force_update=False, with_dict=False, filters=None, *update_fields, **update):
        if not obj:
            obj, _ = self.model.objects.update_or_create(**update)
            return obj
        else:
            if not with_dict:
                if not filters:
                    self.model.objects.filter(id=obj.id).update(**update)
                    return self.model.objects.get(id=obj.id)
                else:
                    return self.model.objects.filter(**filters).update(**update)
            else:
                for k, v in update:
                    setattr(obj, k, v)
                if force_update:
                    obj.save(update_fields=update_fields)
                else:
                    obj.save()
                return obj

    def get_or_404(self, pk=None, with_pk=True, q_list=None, only_one=False, **kwargs):
        try:
            if with_pk:
                return self.model.objects.get(pk=pk, **kwargs)
            else:
                if q_list:
                    if all([isinstance(condition, Q) for condition in q_list]):
                        objs = self.model.objects.filter(*q_list)
                        if not objs:
                            return None
                        if only_one and len(objs) > 1:
                            raise OverflowError('overflow count limit')
                        elif only_one:
                            return objs[0]
                        else:
                            return objs
                    else:
                        raise TypeError
                else:
                    objs = self.model.objects.filter(**kwargs)
                    if not objs:
                        return None
                    if only_one and len(objs) > 1:
                        raise OverflowError('overflow count limit')
                    return objs[0]
                    # elif len(objs) > 1:
                    #     return objs[0]
                    # else:
                    #     return objs
        except ObjectDoesNotExist:
            return None

    def mget(self, order_by='created_time', desc=False, distinct=False, q_list=None, exclude_list=None, **filters):
        if not q_list:
            query = self.model.objects.filter(**filters).order_by('index')
        else:
            if all([isinstance(condition, Q) for condition in q_list]):
                query = self.model.objects.filter(*q_list).order_by('index')
                if exclude_list:
                    if all([isinstance(condition, Q) for condition in exclude_list]):
                        query = query.exclude(*exclude_list)
                    else:
                        raise TypeError
            else:
                raise TypeError
        if desc:
            query = query.order_by(order_by).reverse()
        if distinct:
            query = query.order_by(order_by).distinct()
        return query.all()

    def execute_sql(self, sql, use_cursor=False):
        if not use_cursor:
            return self.model.objects.raw(sql)
        else:
            cursor = connection.cursor()
            cursor.execate(sql)
            transaction.commit()

    def get_fields(self, ret_tuple=True, *args):
        if len(args) == 1:
            return self.model.objects.values_list(*args, flat=True)
        return self.model.objects.values_list(*args)
