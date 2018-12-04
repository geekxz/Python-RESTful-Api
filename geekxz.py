"""
 Created by 陈东东 on 2018/11/20.
"""

from werkzeug.exceptions import HTTPException
from app.libs.error_code import APIException
from app.libs.error_code import ServerError
from app import create_app

__author__ = '陈东东'


app = create_app()


# flask1.0才支持errorhandler HTTPException
@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        # 调试模式
        # log
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e


if __name__ == '__main__':
    app.run(debug=True)
