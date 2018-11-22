"""
 Created by 陈东东 on 2018/11/20.
"""
from app.libs.redprint import Redprint

__author__ = '陈东东'

# Redprint
api = Redprint('book')


@api.route('/getBook', methods=['GET'])
def get_book():
    return 'get book'


@api.route('/createBook', methods=['POST'])
def create_book():
    return 'create book'

