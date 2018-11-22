"""
 Created by 陈东东 on 2018/11/20.
"""
from app.libs.redprint import Redprint

__author__ = '陈东东'

# redprint
api = Redprint('user')


@api.route('/getUser', methods=['GET'])
def get_user():
    return 'get user'
