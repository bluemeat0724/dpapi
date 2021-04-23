#继承HTTPException功能，重构其返回值为json格式（原返回值为http格式）

from flask import request, json
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    code = 500 #默认值 500为未知
    msg = 'sorry, there is an unkonwn mistake'
    error_code = 999

    def __init__(self,msg=None, code=None, error_code=None, headers=None):
        if code:
            self.code=code
        if error_code:
            self.error_code=error_code
        if msg:
            self.msg = msg
        super(APIException, self).__init__(msg, None)#调用基类构造函数,基类参数description, response,有msg,None代替填空

        #重写getbody方法
    def get_body(self, environ=None):
        #设计错误响应
        body = dict(
            msg=self.msg,
            error_code=self.error_code,
            request=request.method+' '+ self.get_url_no_param()#当前请求url路径
        )
        text = json.dumps(body)#转换json格式
        return text

        #获取请求路径（不包含参数部分）
    @staticmethod
    def get_url_no_param():
        full_path=str(request.full_path)#拿到请求的完整路径
        main_path=full_path.split('?')
        return main_path[0]

    # 重写getheaders方法，修改返回头信息为json
    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [("Content-Type", "application/json")]
