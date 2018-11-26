"""
 Created by 陈东东 on 2018/11/21.
"""

__author__ = '陈东东'


from app.libs.error import APIException


class Success(APIException):
    code = 200
    msg = 'ok'
    error_code = 0


class ClientTypeError(APIException):
    # 400 401 403 404
    # 500
    # 200 201 204
    # 301 302
    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParamException(APIException):
    # 400 401 403 404
    # 500
    # 200 201 204
    # 301 302
    code = 400
    msg = 'invalid parameter'
    error_code = 1000
