# from flask import Blueprint,current_app,jsonify,url_for,redirect
# from app.models import DictData
# from app.models.departments_sheet import TradeSheet
# from app import db
# from datetime import datetime
#
# test = Blueprint('test',__name__)
#
# @test.route('/')
# def webtest():
#     print(current_app.config)
#     DictData.insert_dict()
#     return current_app.config.get('ENV')
#
# @test.route('/tradeget')
# def trade_getraw():
#     return redirect(url_for('test.trade_get',year=datetime.today().year))
#
# @test.route('/tradeget/<int:year>/')
# def trade_get(year=2021):
#     data=TradeSheet().get_sheet(year=year)
#     return jsonify({'msg':'done','data':data})
#
# @test.route('/trade')
# def trade_insert():
#     tradedata=TradeSheet(project_type=1,deal_type=1,project_num=20212,service_num=2021,deals_ant=2021.0)
#     db.session.add(tradedata)
#     db.session.flush()
#     db.session.commit()
#     print('tradedataid',tradedata.id)
#     return jsonify({'msg':'done','inserted':tradedata.to_json()})