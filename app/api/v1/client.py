"""
 Created by 陈东东 on 2018/11/26.
"""
__author__ = '陈东东'


from app.libs.redprint import Redprint
from app.validators.forms import ClientForm, UserEmailForm
from app.models.user import User
from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    # 注册 登录
    # 参数 校验 接收参数
    # WTForms 验证表单
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMALL: __register_user_by_email
    }
    promise[form.type.data]()

    # 我们可以预知已知的异常 APIException
    # 我们没法预知未知的异常

    # AOP 出口处理未知异常
    return Success()


def __register_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data, form.account.data, form.secret.data)

