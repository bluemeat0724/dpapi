from app.models import db,Base
from sqlalchemy import Integer ,Float
from app.models import DictData
from sqlalchemy import desc
from datetime import datetime

#交易部
class TradeSheet(Base):
    __tablename__ = 'tradesheet'
    id = db.Column(Integer,primary_key=True,autoincrement=True)
    project_type = db.Column(Integer ,comment='项目类型')
    deal_type = db.Column(Integer,comment='成交类型')
    project_num = db.Column(Integer,comment='项目数',default=None)
    service_num = db.Column(Integer, comment='服务数',default=None)
    deals_ant = db.Column(Float,comment='金额',default=None)
    year = db.Column(Integer, default=0)

    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item

    def get_data(self,project_type,deal_type,year):
        ts=self.query.filter_by(project_type=project_type,deal_type=deal_type,year=year).order_by(desc('create_time')).first()

        if ts is not None:
            data = {'id':ts.id,
                    'project_type':DictData.query.filter_by(dict_name='project_type',dict_sort=ts.project_type).first().dict_label,
                    'deal_type':DictData.query.filter_by(dict_name='deal_type',dict_sort=ts.deal_type).first().dict_label,
                    'project_num':ts.project_num,
                    'service_num':ts.service_num,
                    'deals_ant':ts.deals_ant}

            for i in list(data):
                if data[i] is None:
                    data.pop(i)
            if year!=0:
                data['year']=year

            return data
        else:
            return None

    def get_sheet(self,year):
        data={'total':[
                self.get_data(1,1,0),
                self.get_data(1,2,0),
                self.get_data(2,1,0),
                self.get_data(2,3,0)],
              'by_year':[
                  self.get_data(1,1,year),
                  self.get_data(1,2,year),
                  self.get_data(2,1,year),
                  self.get_data(2,3,year)]}
        return data


#渠道服务部
class ChannelSheet(Base):
    __tablename__='channelsheet'
    id = db.Column(Integer,primary_key=True,autoincrement=True)
    practice = db.Column(Integer,comment='执业类服务机构')
    professional = db.Column(Integer,comment='专业类服务机构')
    corp_contact = db.Column(Integer, comment='合作触达')
    contract_reg = db.Column(Float,comment='技术合同登记额')
    regyear = db.Column(Integer,comment='合同登记额年度', default=datetime.now().year)
    cities = db.Column(Integer,comment='首批试点城市')
    coupon = db.Column(Float,comment='双创券发送额度')

    def get_sheet(self,year=datetime.now().year):
        cs = self.query.filter_by(regyear=year).order_by(
            desc('create_time')).first()
        data = {'id': cs.id,
                'practice':cs.practice,
                'professional':cs.professional,
                'corp_contact':cs.corp_contact,
                'contract_reg':cs.contract_reg,
                'cities': cs.cities,
                'coupon':cs.coupon,
                'regyear':cs.regyear}

        return data

#运营服务部
class OperaterSheet(Base):
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    trademain_view = db.Column(Integer,comment='浏览交易大厅数')
    visitor_num = db.Column(Integer,comment='访客数')
    registered = db.Column(Integer,comment='注册用户数')

    def get_sheet(self):
        ops = self.query.order_by(
            desc('create_time')).first()
        data = {'id': ops.id,
                'trademain_view': ops.trademain_view,
                'visitor_num': ops.visitor_num,
                'registered': ops.registered,
                'create_time':ops.create_time}

        return data


#金融服务部
class FinanceDepsheet(Base):
    id = db.Column(Integer,primary_key=True,autoincrement=True)
    products=db.Column(Integer,comment='金融产品（项）')
    contract_deal=db.Column(Float,comment='技术合同额（万元）')
    credit_issued = db.Column(Float,comment='授信额度（亿元')
    service_predict = db.Column(Float,comment='拟交易服务金额（亿元）')
    corp_contact = db.Column(Integer,comment='合作触达')

    def get_sheet(self):
        fs = self.query.order_by(
            desc('create_time')).first()
        data = {'id': fs.id,
                'products': fs.products,
                'contract_deal': fs.contract_deal,
                'credit_issued': fs.credit_issued,
                'service_predict': fs.service_predict,
                'corp_contact': fs.corp_contact}

        return data

#成果服务部
class TechserviceSheet(Base):
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    corp_contact = db.Column(Integer,comment='合作触达')
    deal_contract = db.Column(Integer,comment='签约创新中心（托管高校院所）')
    deal_predict = db.Column(Integer,comment='意向进场交易数')
    dealmoney_predict = db.Column(Float,comment='意向进程交易额')
    overseas = db.Column(Integer,comment='海外合作触达')

    def get_sheet(self):
        ts = self.query.order_by(
            desc('create_time')).first()
        data = {'id': ts.id,
                'corp_contact': ts.corp_contact,
                'deal_contract': ts.deal_contract,
                'deal_predict': ts.deal_predict,
                'dealmoney_predict': ts.dealmoney_predict,
                'overseas': ts.overseas}
        return data

#企业服务部
class CompanyserviceSheet(Base):
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    company_contacted = db.Column(Integer,comment='已对接企业数')
    company_deals = db.Column(Integer,comment='已签约企业数')
    purchasing_req = db.Column(Integer,comment='当前采购需求数')
    purchasing_pred = db.Column(Float,comment='意向采购总金额（万元）')
    transfer_req = db.Column(Integer,comment='当前转让需求数')
    transfer_pred = db.Column(Float,comment='意向转让总金额（万元）')
    project_deals = db.Column(Integer,comment='技术交易项目数')
    deal_amt = db.Column(Float,comment='技术交易总金额')

    def get_sheet(self):
        cs = self.query.order_by(
            desc('create_time')).first()
        data = {'id': cs.id,
                'company_contacted': cs.company_contacted,
                'company_deals': cs.company_deals,
                'purchasing_req': cs.purchasing_req,
                'purchasing_pred': cs.purchasing_pred,
                'transfer_req': cs.transfer_req,
                'transfer_pred': cs.transfer_pred,
                'project_deals': cs.project_deals,
                'deal_amt': cs.deal_amt,}
        return data

