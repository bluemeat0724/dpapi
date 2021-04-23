from app.api_1_0 import api
from flask import current_app,jsonify,url_for,redirect,send_from_directory,request
from app.models import DictData
from app.models.rollingdata import InnocationCenter
from app.models.statdata import firstcities,overseas
from app import db
from datetime import datetime
import pandas as pd

#创新中心
@api.route('/innovationcenterget')
def innovationcenter_get():
    data=InnocationCenter().get_sheet()
    return jsonify({'msg': 'done', 'data': data})

# @api.route('/innovationcenter')
# def innovationcenter():
#     df = pd.read_excel('E:\SynologyDrive\工作\数据治理\数据资料\相关数据.xlsx', sheet_name='创新中心full')
#     for i, v in df.iterrows():
#         name = v['name']
#         type_one = v['type_one']
#         type_one_id=v['type_one_id']
#         type_two_id = v['type_two_id']
#         type_two = v['type_two']
#         if str(type_two)=='nan':
#             tradedata = InnocationCenter(name=name, type_one=type_one,type_one_id=type_one_id)
#         else:
#             tradedata = InnocationCenter(name=name,type_one_id=type_one_id, type_one=type_one, type_two_id=type_two_id,type_two=type_two)
#         db.session.add(tradedata)
#     db.session.commit()
#     return jsonify({'msg':'done'})

#试点城市
@api.route('/opercities')
def ope_cities():
    return jsonify({'msg': 'done', 'data': firstcities})

#海外合作
@api.route('/oversea')
def overseaget():
    return jsonify({'msg': 'done', 'data': overseas})

