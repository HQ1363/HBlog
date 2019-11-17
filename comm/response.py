#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
Created on 2019/11/17 下午3:50
@author: HQ
@Blog: https://blog.csdn.net/huangqiang1363
"""
import logging

from rest_framework import status
from rest_framework.exceptions import APIException
from functools import wraps
from traceback import print_exc
from rest_framework.response import Response

from comm.utils.common import DotDict

logger = logging.getLogger('default')


class CommResponse(object):

    """ this response will wrapper the base response """
    error_message = DotDict(error=status.HTTP_500_INTERNAL_SERVER_ERROR, msg=u'内部服务器异常, {0}')

    __instance = None

    def __new__(cls, *args, **kwargs):
        if CommResponse.__instance is None:
            CommResponse.__instance = object.__new__(cls)
        return CommResponse.__instance

    def __init__(self, data=None, status_code=None, headers=None, exception=False):
        if not data:
            self.data = self.error_message
        if not exception:
            self.exception = APIException
        if not status_code:
            self.status_code = status.HTTP_200_OK
        self.headers = headers

    def __call__(self, func):
        if callable(func):
            @wraps(func)
            def wrapper_func(*args, **kwargs):
                try:
                    result = func(*args, **kwargs)
                    if len(result) > 1:
                        self.status_code = result[1]
                    self.data = result[0]
                except Exception as exc:
                    print_exc(exc)
                    logger.exception(exc)
                    self.data = self.error_message.msg.format(exc.message)
                    self.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
                finally:
                    if not isinstance(self.data, (dict, )):
                        return_data = self.data
                    else:
                        return_data = dict(self.data)
                    return Response(data=return_data, status=self.status_code, headers=self.headers)
            return wrapper_func
        else:
            raise TypeError(u'this deco only be used for callable object')


comm_response = CommResponse()
