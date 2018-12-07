# Python-RESTfulAPI
Python Flask构建可扩展的RESTdul API


### 目录结构

```

├─app 框架系统目录	
│  ├─api       		核心接口目录
│  ├─config         核心配置目录 
│  ├─libs     		框架类库目录
│  │  ├─enums.py     	
│  │  ├─error.py  	
│  │  ├─error_code.py     	
│  │  ├─redprint.py 
│  │  ├─scope.py     	
│  │  ├─token_auth.py    	
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

### 权限设置管理

Scope.py

##### 权限简介

权限管理主要文件libs/scope.py
	
主要为allow_api列表,allow_api允许访问的列表模块,forbidden禁止允许访问的列表模块.三种模式任选其一

allow_api = []
allow_module = []
forbidden = []

##### 具体用法:

用法一:(使用allow_api,不建议使用,太繁琐)

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

用法二:(使用allow_module)

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
用法三:(使用allow_module)

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