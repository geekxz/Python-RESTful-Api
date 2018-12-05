"""
 Created by 陈东东 on 2018/11/21.
"""

__author__ = '陈东东'


from app.libs.error import APIException


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


# 删除成功
class DeleteSuccess(Success):
    code = 202
    error_code = 1


# 服务器错误
class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999


# 客户端错误
class ClientTypeError(APIException):
    # 400 401 403 404
    # 500
    # 200 201 204
    # 301 302
    code = 400
    msg = 'client is invalid'
    error_code = 1006


# 参数错误
class ParamException(APIException):
    # 400 401 403 404
    # 500
    # 200 201 204
    # 301 302
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


# 用户不存在
class NotFound(APIException):
    code = 404
    msg = 'the resource are not found O__O...'
    error_code = 1001


# 授权失败
class AuthFailed(APIException):
    code = 401
    error_code = 1005
    msg = 'authorization failed'


#   权限不够
class Forbidden(APIException):
    code = 403
    error_code = 1004
    msg = 'forbidden, not in scope'

