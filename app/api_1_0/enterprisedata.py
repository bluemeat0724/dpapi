from app.models.enterprise import EnterpriseApplication,EnterpriseIndustry,EnterprisePrice,EnterprisePatentScore,EnterpriseScore
from app.api_1_0 import api
from flask import current_app,jsonify,request
import json

#企业创新图谱
@api.route('/ent/innovation/<uid>/')
def ent_innovation(uid):
    data = EnterpriseScore().get_data(uid=uid)
    return jsonify({'msg': 'done', 'content': data})

#企业创新录入
@api.route('/ent/innovationpost/',methods=["POST"])
def ent_innovationpossst():
    data=request.get_data()
    try:
        data=json.loads(data)
    except:
        return jsonify({'msg': 'error', 'content': 'wrong data form'})
    modelkeys=['overall','overallGrade','overallEval','identity','identityGrade','vigor','vigorGrade',
              'creativity','creativityGrade','risk','riskGrade','development','developmentGrade',
              'competitiveness','competitivenessGrade','update','entname']
    params=[]
    for i in modelkeys:
        try:
            param=data[i]
        except:
            param=None
        # print(i,param)
        params.append(param)
    if data.get('enid'):
        params.append(data.get('enid'))
    else:
        params.append('')
    EnterpriseScore.data_add(paramlist=params)
    return jsonify({'msg': 'done', 'inserted': data})

    # return jsonify({'msg': 'done', 'content': data})


#专利申请趋势
@api.route('/ent/application/<uid>/')
def ent_application(uid):
    data = EnterpriseApplication().get_data(uid=uid)
    return jsonify({'msg': 'done', 'content': data})

#产学研合作
@api.route('/ent/industry/<uid>/')
def ent_industry(uid):
    data = EnterpriseIndustry().get_data(uid=uid)
    return jsonify({'msg': 'done', 'content': data})

# 专利资产价值
@api.route('/ent/price/<type>/<uid>/')
def ent_price(type,uid):
    if type=='all':
        data = EnterprisePrice().get_data(uid=uid)
    elif type=='mean':
        data=EnterprisePrice().get_meandata(uid=uid)
    elif type=='max':
        data = EnterprisePrice().get_maxdata(uid=uid)
    elif type=='groups':
        data = EnterprisePrice().get_groups(uid=uid)
    else:
        return jsonify({'msg': 'wrong parameter', 'content': ''})
    return jsonify({'msg': 'done', 'content': data})





# 专利质量
@api.route('/ent/score/<uid>/')
def ent_score(uid):
    data = EnterprisePatentScore().get_data(uid=uid)
    return jsonify({'msg': 'done', 'content': data})
