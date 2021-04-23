from app.api_1_0 import api
from flask import current_app,jsonify,url_for,redirect
from app.models import DictData
from app.models.departments_sheet import TradeSheet,ChannelSheet,FinanceDepsheet,OperaterSheet,TechserviceSheet,CompanyserviceSheet
from app.models.enterprise import EnterprisePatentScore
from app.models.government import GovernmentDistribution
from app.models.university import UniversityApplication
from app.models.rollingdata import InnocationCenter
from app.utils.TDtool import gettrendingdata
from app import db
from datetime import datetime

@api.route('/')
def webtest():
    print(current_app.config)
    DictData.insert_dict()
    return current_app.config.get('ENV')

#交易部
@api.route('/tradeget')
def trade_getraw():
    return redirect(url_for('api_1_0.trade_get',year=datetime.today().year))

@api.route('/tradeget/<int:year>/')
def trade_get(year):
    data=TradeSheet().get_sheet(year=year)
    return jsonify({'msg':'done','data':data})

@api.route('/trade')
def trade_insert():
    # tradedata11=TradeSheet(project_type=1,deal_type=1,project_num=19,service_num=83,deals_ant=236.389290)
    # tradedata12 = TradeSheet(project_type=1, deal_type=2, project_num=30, service_num=1250, deals_ant=4233.8700)
    # tradedata21 = TradeSheet(project_type=2, deal_type=1, project_num=3, service_num=67, deals_ant=474.5490)
    # tradedata23 = TradeSheet(project_type=2, deal_type=3, project_num=49, service_num=133, deals_ant=60296.485641)
    #
    # tradedata11y = TradeSheet(project_type=1, deal_type=1, project_num=16, service_num=16, deals_ant=233.5088,year=2021)
    # tradedata12y = TradeSheet(project_type=1, deal_type=2, project_num=2, service_num=5, deals_ant=0,year=2021)
    # tradedata21y = TradeSheet(project_type=2, deal_type=1, project_num=0, service_num=0, deals_ant=0,year=2021)
    # tradedata23y = TradeSheet(project_type=2, deal_type=3, project_num=36, service_num=45, deals_ant=18781.351,year=2021)
    # db.session.add(tradedata11)
    # db.session.add(tradedata12)
    # db.session.add(tradedata21)
    # db.session.add(tradedata23)
    # db.session.add(tradedata11y)
    # db.session.add(tradedata12y)
    # db.session.add(tradedata21y)
    # db.session.add(tradedata23y)
    #
    # db.session.flush()
    # db.session.commit()
    # # print('tradedataid',tradedata.id)
    # # return jsonify({'msg': 'done', 'inserted': tradedata11.to_json()})
    # return jsonify({'msg':'done','inserted':[tradedata11.to_json(),tradedata12.to_json(),tradedata21.to_json(),tradedata23.to_json()]})
    return jsonify({'msg': 'done', 'inserted': 'nothing'})

#渠道服务部
@api.route('/channelget/<int:year>')
def channel_get(year=datetime.now().year):
    data=ChannelSheet().get_sheet(year=2021)
    return jsonify({'msg':'done','data':data})


@api.route('/channelget')
def channel_getraw(year=datetime.now().year):
    return redirect(url_for('api_1_0.channel_get', year=datetime.today().year))


@api.route('/channel')
def channel_insert():
    # channeldata=ChannelSheet(practice=18,professional=2,contract_reg=1991.460025,regyear=2021,cities=26,coupon=104645.230088)
    # db.session.add(channeldata)
    # db.session.flush()
    # db.session.commit()
    # print('tradedataid', channeldata.id)
    # return jsonify({'msg': 'done', 'inserted': channeldata.to_json()})
    return jsonify({'msg': 'done', 'inserted': 'nothing'})

#金融服务部
@api.route('/finance')
def finance_insert():
    # with db.auto_commit():
    #     financedata=FinanceDepsheet(products=3,contract_deal=3700,credit_issued=15000,service_predict=24000,corp_contact=35)
    #     db.session.add(financedata)
    #     db.session.flush()
    # # db.session.commit()
    # print('tradedataid', financedata.id)
    # return jsonify({'msg': 'done', 'inserted': financedata.to_json()})
    return jsonify({'msg': 'done', 'inserted': 'nothing'})

@api.route('/financeget')
def finance_get():
    data=FinanceDepsheet().get_sheet()
    return jsonify({'msg':'done','data':data})

#运营服务部
@api.route('/operate')
def operate_insert():
    # operatedata=OperaterSheet(trademain_view=50150,visitor_num=33216,registered=264)
    # db.session.add(operatedata)
    # db.session.flush()
    # db.session.commit()
    # print('tradedataid', operatedata.id)
    # return jsonify({'msg': 'done', 'inserted': operatedata.to_json()})
    return jsonify({'msg': 'done', 'inserted': 'nothing'})

@api.route('/operateget')
def operate_get():
    data=OperaterSheet().get_sheet()
    return jsonify({'msg':'done','data':data})

#成果服务部
@api.route('/techservice')
def techservice_insert():
    # techservicedata=TechserviceSheet(corp_contact=46,deal_contract=17,deal_predict=444,dealmoney_predict=70705,overseas=12)
    # db.session.add(techservicedata)
    # db.session.flush()
    # db.session.commit()
    # print('tradedataid', techservicedata.id)
    # return jsonify({'msg': 'done', 'inserted': techservicedata.to_json()})
    return jsonify({'msg': 'done', 'inserted': 'nothing'})

@api.route('/techserviceget')
def techservice_get():
    data=TechserviceSheet().get_sheet()
    return jsonify({'msg':'done','data':data})

#企业服务部
@api.route('/companyservice')
def companyservice_insert():
    # companyservicedata=CompanyserviceSheet(company_contacted=47,company_deals=11,purchasing_req=33,purchasing_pred=2710,transfer_req=216,
    #                                        transfer_pred=54990,project_deals=31,deal_amt=57700)
    # db.session.add(companyservicedata)
    # db.session.flush()
    # db.session.commit()
    # print('tradedataid', companyservicedata.id)
    # return jsonify({'msg': 'done', 'inserted': companyservicedata.to_json()})
    return jsonify({'msg': 'done', 'inserted': 'nothing'})

@api.route('/companyserviceget')
def companyservice_get():
    data=CompanyserviceSheet().get_sheet()
    return jsonify({'msg':'done','data':data})

#大屏数据
@api.route('/datamap')
def datamap():
    trade=TradeSheet().get_sheet(year=datetime.now().year)
    channel=ChannelSheet().get_sheet()
    finance=FinanceDepsheet().get_sheet()
    operate=OperaterSheet().get_sheet()
    techservice=TechserviceSheet().get_sheet()
    companyservice=CompanyserviceSheet().get_sheet()
    data={}
    # 累计挂牌科技成果数
    acculisted_num = 0
    for i in [0, 1, 3]:
        acculisted_num += trade['total'][i]['service_num']
    data['acculisted_num']=acculisted_num
    # 累计成交金额
    deal_amount = 0
    for i in [2, 3]:
        deal_amount += trade['total'][i]['deals_ant']
    deal_amount = round(deal_amount / 10000, 2)
    data['deal_amount']=deal_amount
    # 意向进场科技成果数
    tech_listwill = trade['total'][1]['service_num'] + techservice['deal_predict'] + \
                    companyservice['project_deals']
    data['tech_listwill']=tech_listwill
    # 意向进场交易金额
    tradewill_amount = trade['total'][1]['deals_ant'] + techservice['dealmoney_predict'] + \
                       companyservice['deal_amt']
    tradewill_amount = round(tradewill_amount / 10000, 3)
    data['tradewill_amount'] = tradewill_amount
    # 2021年挂牌科技成果数
    listed_num2021 = 0
    for i in [0, 1, 3]:
        listed_num2021 += trade['by_year'][i]['service_num']
    data['listed_num2021']=listed_num2021
    # 2021累计成交金额
    deal_amount2021 = 0
    for i in [2, 3]:
        deal_amount2021 += trade['by_year'][i]['deals_ant']
    deal_amount2021 = round(deal_amount2021 / 10000, 2)
    data['deal_amount2021']=deal_amount2021
    # 成果转化创新中心
    data['t_deal_contract']=techservice['deal_contract']
    data['dealmoney_predict'] = round(techservice['dealmoney_predict']/10000,2)
    data['t_corp_contact'] = techservice['corp_contact']
    data['deal_predict'] = techservice['deal_predict']
    #企业联合创新中心
    data['company_deals'] = companyservice['company_deals']
    data['deal_amt'] = round(companyservice['deal_amt']/10000,2)
    data['c_corp_contact'] = companyservice['company_contacted']
    data['project_deals'] = companyservice['project_deals']
    #金融运营创新中心
    data['f_corp_contact']=finance['corp_contact']
    data['credit_issued'] = round(finance['credit_issued']/10000,2)
    data['products'] = finance['products']
    data['service_predict'] = round(finance['service_predict']/10000,2)
    #区域协同创新中心
    data['cities']=channel['cities']
    data['contract_reg'] = round((channel['contract_reg']+1179109)/10000,2)
    data['overseas'] = techservice['overseas']
    #技术交易服务机构
    data['service_institution']=channel['practice']+channel['professional']
    data['i_corp_contact'] = channel['corp_contact']
    #运营
    #获取运行信息
    registered = operate['registered']
    lasttimeraw = operate['create_time']
    print('lasttimeraw',lasttimeraw)
    print('now', datetime.now())
    # lasttime = datetime.strptime(lasttimeraw, '%Y-%m-%d %H:%M:%S')
    timedelta = datetime.now() - lasttimeraw
    seconds = timedelta.total_seconds()
    if seconds>3600*24:
        try:
            result = gettrendingdata()
            operatedata=OperaterSheet(trademain_view=result[-1]['pv'],visitor_num=result[-1]['uv'],registered=registered)
            db.session.add(operatedata)
            db.session.commit()
            data['trademain_view'] = result[-1]['pv']
            data['visitor_num'] = result[-1]['uv']
            data['registered'] = registered
            print('data renewed')
        except:
            print('api fail')
            data['trademain_view'] = operate['trademain_view']
            data['visitor_num'] = operate['visitor_num']
            data['registered'] = operate['registered']
    else:
        print('normal')
        data['trademain_view']=operate['trademain_view']
        data['visitor_num'] = operate['visitor_num']
        data['registered'] = operate['registered']
    return jsonify({'msg':'done','data':data})

#大屏数据
@api.route('/operatesum')
def operatesum():
    result = gettrendingdata()
    operate=OperaterSheet().get_sheet()
    registered=operate['registered']
    try:
        operatedata=OperaterSheet(trademain_view=result[-1]['pv'],visitor_num=result[-1]['uv'],registered=registered)
        db.session.add(operatedata)
        db.session.commit()
    except:
        pass
    return  jsonify({'msg':'done','data':result})


#id参数
@api.route('/apiparam')
def apiparam():
    enterprise=EnterprisePatentScore().getparams()
    government=GovernmentDistribution().getparams()
    university=UniversityApplication().getparams()
    data={'enterprise':enterprise,
          'government':government,
          'university':university}

    return jsonify({'msg':'done','data':data})

