"""
 Created by 陈东东 on 2018/11/20.
"""

from flask import jsonify, g

from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.user import User
from app.models.base import db
from app.libs.error_code import DeleteSuccess, AuthFailed


__author__ = '陈东东'

# 自定义的红图 redprint
api = Redprint('user')


@api.route('/getUser', methods=['GET'])
@auth.login_required
def get_user():
    # 验证token是否合法 是否过期
    uid = g.user.id
    user = User.query.filter_by(id=uid).first_or_404()
    # dict
    # view_model
    # 视图层 个性化的视图模型
    return jsonify(user)


@api.route('/delUser', methods=['DELETE'])
@auth.login_required
def delete_user():
    # 不需要用户输入uid 从token读取uid(原因用户超权)
    # g线程隔离 不同用户访问不会冲突
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()   # 软删除 更改数据库状态
    return DeleteSuccess()


# 管理员权限访问
@api.route('/getUser/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    # 验证token是否合法 是否过期
    user = User.query.filter_by(id=uid).first_or_404()
    # dict
    # view_model
    # 视图层 个性化的视图模型
    return jsonify(user)


@api.route('/delUser/<int:uid>', methods=['DELETE'])
def super_delete_user(uid):
    pass

