from app.models.government import GovernmentApplication,GovernmentDistribution,GovernmentTechOrigin,GovernmentIndustry,GovernmentInventor,GovernmentTechOut
from app.api_1_0 import api
from flask import current_app,jsonify,url_for,redirect,request,make_response


#专利申请区域
@api.route('/gov/application/<uid>/')
def gov_application(uid):
    data = GovernmentApplication().get_data(uid=uid)
    return jsonify({'msg': 'done', 'content': data})


#企业专利数量分布
@api.route('/gov/distribution/<uid>/')
def gov_distribution(uid):
    data = GovernmentDistribution().get_data(uid=uid)
    return jsonify({'msg': 'done', 'content': data})


#技术源所属地区
@api.route('/gov/techorigin/<uid>/')
def gov_techorigin(uid):
    data = GovernmentTechOrigin().get_data(uid=uid)
    return jsonify({'msg': 'done', 'content': data})

#战略新型产业成果产出排行
@api.route('/gov/industry/<uid>/')
def gov_industry(uid):
    data = GovernmentIndustry().get_data(uid=uid)
    return jsonify({'msg': 'done', 'content': data})

#每年新增发明人
@api.route('/gov/inventor/<uid>/')
def gov_inventor(uid):
    data = GovernmentInventor().get_data(uid=uid)
    return jsonify({'msg': 'done', 'content': data})

#技术流出所属地区
@api.route('/gov/techout/<uid>/')
def gov_techout(uid):
    data = GovernmentTechOut().get_data(uid=uid)
    return jsonify({'msg': 'done', 'content': data})