"""
 Created by 陈东东 on 2018/11/20.
"""

from app.app import create_app

__author__ = '陈东东'


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
