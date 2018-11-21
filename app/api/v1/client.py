"""
 Created by 陈东东 on 2018/11/21.
"""
__author__ = '陈东东'

from flask import request, jsonify
from app.libs.redprint import Redprint
from app.validators.forms import ClientForm, UserEmailForm
from app.models.user import User
from app.libs.enums import ClientTypeEnum

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    # 注册 登录
    # 参数 校验 接收参数
    # WTForms 验证表单
    data = request.json
    form = ClientForm(data=data)
    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMALL: __register_user_by_email
        }
        promise[form.type.data]()
    return 'success'


def __register_user_by_email():
    form = UserEmailForm(data=request.json)
    if form.validate():
        User.register_by_email(form.nickname.data,
                               form.account.data,
                               form.secret.data)

