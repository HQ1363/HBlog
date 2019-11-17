#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
Created on 2019/11/17 下午3:42
@author: HQ
@Blog: https://blog.csdn.net/huangqiang1363
"""
import json

from datetime import date, datetime
from django.core.serializers.json import DjangoJSONEncoder


class DotDict(dict):
    """
    d = DotDict({'a': 'spam', 'b': 'ham'})
    print d['a']
    >   spam
    print d.b
    >   ham
    d.c = 'python!'
    print d.c
    >   python!
    '''
    """
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__
    __delattr__ = dict.__delitem__

    @property
    def to_json(self):
        data = eval(str(self))
        return json.dumps(data, cls=ComplexEncoder)


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


def json_loads(data):
    return json.loads(data)


def json_dumps(data):
    return json.dumps(
        data, separators=(',', ':'), encoding="UTF-8", ensure_ascii=False, cls=DjangoJSONEncoder)

