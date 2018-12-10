# Python Flask1.0.x构建可扩展的RESTful API
Python Flask构建可扩展的RESTdul API

### 目录结构

```

├─app 框架系统目录	
│  ├─api       		核心接口目录
│  ├─config         核心配置目录 
│  ├─libs     		框架类库目录
│  │  ├─enums.py     	客户端类型标识
│  │  ├─error.py  		API错误返回类
│  │  ├─error_code.py   错误状态码类  	
│  │  ├─redprint.py 	自定义红图
│  │  ├─scope.py     	权限管理类
│  │  ├─token_auth.py   Token验证
│  │  ├─ ...      	更多类库目录
│  ├─models         框架应用模式目录
│  ├─validators     表单验证器目录
│  └─app.py    		框架入口文件
├─geekxz.py
├─fake.py
├─Pipfile
├─Pipfile.lock
├─README.md
│

```

### 接口编写步骤

##### 1. ``app/api/v1/``目录下建立资源:

	例如想建立一个关于文章的api,在``app/api/v1/``目录下建立``article.py``

##### 2. ``app/models/``目录下建立对应的操作模型``article.py``

##### 3. ``app/validators/forms.py ``建立表单验证器类``ArticleSearchForm()继承ClientForm``

##### 4. 编写接口业务``app/api/v1/article.py``
	
	导入所需类库:
	```py
	from flask import jsonify
	from sqlalchemy import or_

	from app.validators.forms import ArticleSearchForm
	from app.libs.redprint import Redprint
	from app.models.article import Article
	```

	
	'''Redprint 调用自定义红图''' 
	api = Redprint('article')


	'''文章搜索'''
	@api.route('/search', methods=['POST'])
	def search():
	    # url:http://localhost:5000/v1/article/search?q={}
	    form = ArticleSearchForm().validate_for_api()
	    q = '%' + form.q.data + '%'
	    # articles = Article()
	    # 元类 ORM
	    articles = Article.query.filter(
	        or_(Article.title.like(q), Article.content.like(q))).all()
	    articles = [article.hide('content', 'id').append('view') for article in articles]
	    return jsonify(articles)
	```

##### 5.最后把自定义的红图注册到蓝图上:

	```py

	from flask import Blueprint
	from app.api.v1 import user, article, client, token

	def create_blueprint_v1():
	    # from app.api.v1.book import api
	    # from app.api.v1.user import api
	    bp_v1 = Blueprint('v1', __name__)

	    user.api.register(bp_v1)
	    client.api.register(bp_v1)
	    token.api.register(bp_v1)
	    return bp_v1


	    article.api.register(bp_v1)
	```

### 权限设置管理  : 基于 flask_httpauth 中 HTTPBasicAuth做token用户权限验证 

Scope.py

#### 权限简介

权限管理主要文件``libs/scope.py``
	
主要为``allow_api``列表,``allow_api``允许访问的列表模块,``forbidden``禁止允许访问的列表模块.三种模式任选其一
```
allow_api = []
allow_module = []
forbidden = []
```
#### 具体用法:

##### 用法一:(使用allow_api,不建议使用,太繁琐)

```py

class Scope:
    allow_api = []
    allow_module = []
    forbidden = []

    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api))
        # 运算符重载

        self.allow_module = self.allow_module + other.allow_module
        self.allow_module = list(set(self.allow_module))

        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))

        return self


class AdminScope(Scope):
    allow_api = ['v1.user+super_get_user', 'v1.user+super_delete_user'] 

	def __init__(self):
      	self + UserScope() # 使用allow_module不需要加UserScope()

class UserScope(Scope):
    allow_api = ['v1.user+get_user', 'v1.user+delete_user']


def is_in_scope(scope, endpoint):
    # 动态创建类
    # scope()
    # 反射
    # globals
    # v1.view_func   v1.module_name+view_func
    # v1.red_name+view_func
    scope = globals()[scope]()
    splits = endpoint.split('+')
    red_name = splits[0]
    if endpoint in scope.forbidden:
        return False
    if endpoint in scope.allow_api:
        return True
    if red_name in scope.allow_module:
        return True
    else:
        return False

```

##### 用法二:(使用allow_module)

```py

class Scope:
    allow_api = []
    allow_module = []
    forbidden = []

    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api))
        # 运算符重载

        self.allow_module = self.allow_module + other.allow_module
        self.allow_module = list(set(self.allow_module))

        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))

        return self


class AdminScope(Scope):
    allow_module = ['v1.user']


class UserScope(Scope):
    allow_module = ['v1.user+get_user', 'v1.user+delete_user']


def is_in_scope(scope, endpoint):
    # 动态创建类
    # scope()
    # 反射
    # globals
    # v1.view_func   v1.module_name+view_func
    # v1.red_name+view_func
    scope = globals()[scope]()
    splits = endpoint.split('+')
    red_name = splits[0]
    if endpoint in scope.forbidden:
        return False
    if endpoint in scope.allow_api:
        return True
    if red_name in scope.allow_module:
        return True
    else:
        return False
    pass

```
##### 用法三:(使用allow_module)

```py

class Scope:
    allow_api = []
    allow_module = []
    forbidden = []

    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api))
        # 运算符重载

        self.allow_module = self.allow_module + other.allow_module
        self.allow_module = list(set(self.allow_module))

        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))

        return self


class AdminScope(Scope):
    allow_module = ['v1.user']

    def __init__(self):
	    pass

class UserScope(Scope):
    # 排除
    forbidden = ['v1.user+super_get_user',
                 'v1.user+super_delete_user']

    def __init__(self):
        self + AdminScope()


def is_in_scope(scope, endpoint):
    # 动态创建类
    # scope()
    # 反射
    # globals
    # v1.view_func   v1.module_name+view_func
    # v1.red_name+view_func
    scope = globals()[scope]()
    splits = endpoint.split('+')
    red_name = splits[0]
    if endpoint in scope.forbidden:
        return False
    if endpoint in scope.allow_api:
        return True
    if red_name in scope.allow_module:
        return True
    else:
        return False
    pass

```


### 学习与讨论	<计算机视觉研发>(QQ群:883769572)

```

╔===================================================================╗
┆								     ┆
┆             		计算机视觉研发 http://www.geekxz.com         ┆
┆								     ┆
┆                《计算机视觉研发》 - 高质量的互联网技术分享平台    ┆
┆								     ┆
┆                             www.geekxz.com                        ┆
┆								     ┆
┆      ╔------------------------------------------------------╗   ┆
┆      ┆                                                      ┆   ┆
┆      ┆       智能设备  视觉资讯  图像处理  特效专家         ┆   ┆
┆      ┆                                                      ┆   ┆
┆      ┆       入门例子  好用例子  技术分享  经验分享         ┆   ┆
┆      ┆                                                      ┆   ┆
┆      ┆       技术交易  it技术分享 人工智能           	┆   ┆
┆      ┆                                                      ┆   ┆
┆      ╚------------------------------------------------------╝   ┆
┆								     ┆
┆                    ------> 共享创造价值 <------	             ┆
┆								     ┆
┆		           QQ交流群:883769572			     ┆
┆                 《计算机视觉研发》感谢有您的参与！ 	             ┆
┆							             ┆
┆								     ┆
╚===================================================================╝

```
