#自定义异常
from app.utils.error import APIException

class Success(APIException):
    code = 201
    msg = 'success'
    error_code = 0

class ServerError(APIException):
    code = 500
    msg = 'Hehe, There is an unknown mistake.'
    error_code = 999

class ClientTypeError(APIException):
    #常用状态码 400参数错误 401未授权 403禁止访问 404未找到资源
    #           500服务器产生未知错误
    #           200查询成功 201创建更新成功 204删除成功
    #           301/302重定向
    code = 400
    msg = (
        'client is invalid'
    )
    error_code = 1006

class ParameterException(APIException):#公共异常
    code = 400
    msg = 'Invalid parameter'
    error_code = 1000

class NotFound(APIException):
    code =404
    msg = 'the resource are not found'
    error_code =1001

class AuthFailed(APIException):
    code = 401
    error_code = 1005
    msg = 'authorization failed'

class UserNotFound(APIException):
    code = 401
    error_code = 1005
    msg = 'UserNotFound'

class DeleteSuccess(Success):
    code = 202
    error_code = 1

class Forbidden(APIException):
    code = 403
    error_code = 1004
    msg = 'forbidden, not in scope'