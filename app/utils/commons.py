# 定义正则转换器
from werkzeug.routing import BaseConverter
from flask import session,jsonify,g
from app.utils.response_code import RET

class ReConverter(BaseConverter):
    def __init__(self,url_map,regex):
        super(ReConverter,self).__init__(url_map)
        self.regex = regex

#登陆状态验证
def login_required(view_func):
    def wrapper(*args,**kwargs):
        #判断用户登陆状态
        user_id=session.get('user_id')
        #如果登陆，执行视图函数
        if user_id is not None:
            g.user_id = user_id
            return view_func(*args,**kwargs)
        else:
            return jsonify(errno=RET.SERVERERR, errmsg="用户未登录")
        #如果未登录，返回未登录信息

    return wrapper


