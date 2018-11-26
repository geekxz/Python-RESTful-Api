"""
 Created by 陈东东 on 2018/11/26.
"""
__author__ = '陈东东'

from flask import request
from wtforms import Form

from app.libs.error_code import ParamException


class BaseFrom(Form):
    def __init__(self):
        data = request.json
        super(BaseFrom, self).__init__(data=data)

    def validate_for_api(self):
        valid = super(BaseFrom, self).validate()
        if not valid:
            # form errors
            raise ParamException(msg=self.errors)
        return self
