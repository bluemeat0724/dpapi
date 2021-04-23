from app.models.university import UniversityApplication,UniversityIndustry,UniversityPrice,UniversityProposal,UniversityRecommend,UniversityRegion
from app.api_1_0 import api
from flask import current_app,jsonify,url_for,redirect,request,make_response
from app.models import db


from sqlalchemy import func,create_engine
from sqlalchemy.sql import label
from app.models import db

from sqlalchemy.orm import scoped_session,sessionmaker
from app.models import db

#专利申请趋势
@api.route('/uni/application/<uid>/')
def uni_application(uid):
    data = UniversityApplication().get_data(uid=uid)
    return jsonify({'msg': 'done', 'content': data})

#产学研合作
@api.route('/uni/industry/<uid>/')
def uni_industry(uid):
    data = UniversityIndustry().get_data(uid=uid)
    return make_response(jsonify({'msg': 'done', 'content': data}))


#专利资产价值
# @api.route('/uni/price/<uid>/',defaults={'page': 1})
# @api.route('/uni/price/<uid>/<int:page>/')
@api.route('/uni/price/<uid>')
def uni_price(uid):
    # data = UniversityPrice().get_data(uid=uid,page=page)
    # data = UniversityPrice().get_data(uid=uid)
    connection=db.engine.connect()
    dataquery=connection.execute("SELECT price,cast(date_year as SIGNED) as year FROM `shh_university_price` where cast(date_year as SIGNED)>2009")
    data = {}
    # data['uid'] = dataquery[0].UN_ID
    data['data'] = []
    for i in dataquery:
        dic = {}
        dic['price'] = i[0]
        dic['year']=i[1]
        data['data'].append(dic)
    data['data'].sort(key=lambda x: x['year'])
    connection.close()
    data['count'] = len(data['data'])
    return make_response(jsonify({'msg': 'done', 'content': data}))

#专利处置建议
@api.route('/uni/proposal/<uid>/')
def uni_proposal(uid):
    data = UniversityProposal().get_data(uid=uid)
    return jsonify({'msg': 'done', 'content': data})

#高价值专利推荐
@api.route('/uni/recommend/<uid>/')
def uni_recommend(uid):
    data = UniversityRecommend().get_data(uid=uid)
    return jsonify({'msg': 'done', 'content': data})

#高校专利受让人区域
@api.route('/uni/region/<uid>/<int:year>')
def uni_region(uid,year):
    data = UniversityRegion().get_data(uid=uid,year=year)
    return jsonify({'msg': 'done', 'content': data})

@api.route('/uni/regiontotal/<uid>/')
def uni_region_total(uid):
    data = UniversityRegion().get_data_byregion(uid=uid)
    return jsonify({'msg': 'done', 'content': data})

@api.route('/uni/test/<uid>/')
def uni_region_test(uid):
    # data=db.session.query(UniversityRegion.ID,UniversityRegion.UN_ID,UniversityRegion.name,db.func.sum(UniversityRegion.num)).group_by(UniversityRegion.name).all()
    data=UniversityRegion().getregiondata(uid=uid)
    return jsonify({'msg': 'done', 'content': data})