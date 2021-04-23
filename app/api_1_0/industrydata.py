from app.models.industry import IndustryFever,IndustryFeverMonth,IndustryPrice,IndustryPriceMonth
from app.api_1_0 import api
from flask import current_app,jsonify,url_for,redirect,request,make_response
from app.models import db


#市场热度初始值
@api.route('/industry/fever/')
def industry_fever():
    data = IndustryFever().get_data()
    return jsonify({'msg': 'done', 'content': data})


#市场热度月度对数
@api.route('/industry/fevermonth/')
def industry_fevermonth():
    data = IndustryFeverMonth().get_data(log=True)
    return jsonify({'msg': 'done', 'content': data})

#市场热度月度原始
@api.route('/industry/fevermonthorg/')
def industry_fevermonthorg():
    data = IndustryFeverMonth().get_data()
    return jsonify({'msg': 'done', 'content': data})


#市场价格初始数据
@api.route('/industry/price/')
def industry_price():
    data = IndustryPrice().get_data()
    return jsonify({'msg': 'done', 'content': data})


#市场价格月度数据
@api.route('/industry/pricemonth/')
def industry_pricemonth():
    data = IndustryPriceMonth().get_data()
    return jsonify({'msg': 'done', 'content': data})

#产业信息表
@api.route('/industry/infotable/')
def industry_infotable():
    dataquery=db.session.query(IndustryPrice.name,IndustryPrice.level,IndustryPrice.industry_id,IndustryPrice.p_value,IndustryFever.f_value,).join(IndustryFever,IndustryFever.name == IndustryPrice.name).all()
    data={}
    data['data'] = []
    for i in dataquery:
        dic={}
        dic['name']=i.name
        dic['level']=i.level
        dic['industry_id']=i.industry_id
        dic['price']='-' if i.p_value=='0.00' or i.p_value=='0' else i.p_value
        dic['fever']='-' if i.f_value=='0.00' or i.f_value=='0' else i.f_value
        data['data'].append(dic)
    return jsonify({'msg': 'done', 'content': data})

