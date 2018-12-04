"""
 Created by 陈东东 on 2018/11/20.
"""

from flask import jsonify

from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.user import User


__author__ = '陈东东'

# 自定义的红图 redprint
api = Redprint('user')


@api.route('/getUser/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    # 验证token是否合法 是否过期
    user = User.query.get_or_404(uid)
    # dict

    return jsonify(user)
