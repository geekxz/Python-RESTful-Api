"""
 Created by 陈东东 on 2018/11/21.
"""
__author__ = '陈东东'

from enum import Enum


class ClientTypeEnum(Enum):
    # 用户邮箱 手机号登录
    USER_EMALL = 100
    USER_MOBILE = 101

    # 小程序登录
    USER_MINA = 200
    # 微信登录
    USER_WX = 201
