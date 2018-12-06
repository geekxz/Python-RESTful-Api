"""
 Created by 陈东东 on 2018/12/05.
"""
__author__ = '陈东东'


from app import create_app
from app.models.base import db
from app.models.user import User

app = create_app()
with app.app_context():
    with db.auto_commit():
        # 创建一个超级管理员
        user = User()
        user.nickname = 'Super'
        user.password = '123456'
        user.email = 'geekxz@aliyun.com'
        user.auth = 2
        db.session.add(user)
