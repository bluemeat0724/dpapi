from app.models import db
from sqlalchemy import Integer,String,Float
from app.utils.transtools import pinyinstring

class GovernmentApplication(db.Model):
    __tablename__='shh_government_application_region'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'comment':'专利申请区域'}
    key=db.Column(Integer, primary_key=True, autoincrement=True)
    name=db.Column(String(255),comment='申请区域')
    num=db.Column(Integer,comment='数量')
    ID=db.Column(String(255),comment='行政区域')
    UN_ID = db.Column(String(255),comment='行政区id')

    def get_data(self,uid):
        dataquery=self.query.filter_by(UN_ID=uid).order_by(db.desc(self.name)).all()
        data={}
        data['gov']=pinyinstring(dataquery[0].ID)
        data['govcn'] = dataquery[0].ID
        data['uid']=dataquery[0].UN_ID
        data['data']=[]
        for i in dataquery:
            dic={}
            dic['region']=i.name+'区'
            dic['org_region'] = i.name
            dic['num']=i.num
            data['data'].append(dic)
        return data

class GovernmentDistribution(db.Model):
    __tablename__='shh_government_distribution'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'comment':'企业专利数量分布(仅发明)'}
    key=db.Column(Integer, primary_key=True, autoincrement=True)
    name=db.Column(String(255),comment='分布区间')
    num=db.Column(Integer,comment='数量')
    ID=db.Column(String(255),comment='行政区域')
    UN_ID = db.Column(String(255),comment='行政区id')

    def get_data(self,uid):
        dataquery=self.query.filter_by(UN_ID=uid).order_by(db.desc(self.name)).all()
        data={}
        data['gov']=dataquery[0].ID
        data['uid']=dataquery[0].UN_ID
        data['data']=[]
        for i in dataquery:
            dic={}
            dic['range']=i.name
            dic['num']=i.num
            data['data'].append(dic)
        return data

    @staticmethod
    def getparams():
        dataquery=db.session.query(GovernmentDistribution.UN_ID,GovernmentDistribution.ID).distinct(GovernmentDistribution.UN_ID)
        data=[]
        for i in dataquery:
            dic={}
            dic['uid']=i.UN_ID
            dic['name']=i.ID
            data.append(dic)
        return data


class GovernmentTechOrigin(db.Model):
    __tablename__='shh_government_in'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'comment':'技术源所属地区'}
    key=db.Column(Integer, primary_key=True, autoincrement=True)
    name=db.Column(String(255),comment='省市名称')
    num=db.Column(Integer,comment='数量')
    ID=db.Column(String(255),comment='行政区域')
    UN_ID = db.Column(String(255),comment='行政区id')

    def get_data(self,uid):
        dataquery=self.query.filter_by(UN_ID=uid).order_by(db.desc(self.name)).all()
        data={}
        data['gov']=dataquery[0].ID
        data['uid']=dataquery[0].UN_ID
        data['data']=[]
        for i in dataquery:
            dic={}
            dic['region']=i.name
            dic['num']=i.num
            data['data'].append(dic)
        return data


class GovernmentIndustry(db.Model):
    __tablename__='shh_government_industry'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'comment':'战略新型产业成果产出排行'}
    key=db.Column(Integer, primary_key=True, autoincrement=True)
    name=db.Column(String(255),comment='产业名称')
    num=db.Column(String(255),comment='数量')
    level=db.Column(Integer,comment='产业级别')
    ID=db.Column(String(255),comment='行政区域')
    UN_ID = db.Column(String(255),comment='行政区id')

    def get_data(self,uid):
        dataquery=self.query.filter_by(UN_ID=uid).order_by(db.desc(self.name)).all()
        data={}
        data['gov']=dataquery[0].ID
        data['uid']=dataquery[0].UN_ID
        data['data']=[]
        for i in dataquery:
            dic={}
            dic['industry'] = i.name
            dic['level']=i.level
            try:
                num=int(i.num.replace(',',''))
            except:
                num=0
            dic['num']=num
            data['data'].append(dic)
        return data


class GovernmentInventor(db.Model):
    __tablename__='shh_government_inventor'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'comment':'每年新增发明人'}
    key=db.Column(Integer, primary_key=True, autoincrement=True)
    date_year=db.Column(String(255),comment='申请年')
    num1=db.Column(Integer,comment='发明人数量')
    num2=db.Column(Integer,comment='新增发明人数量')
    ID=db.Column(String(255),comment='行政区域')
    UN_ID = db.Column(String(255),comment='行政区id')

    def get_data(self,uid):
        dataquery=self.query.order_by(self.date_year).filter_by(UN_ID=uid).all()
        data={}
        data['gov']=dataquery[0].ID
        data['uid']=dataquery[0].UN_ID
        data['data']=[]
        for i in dataquery:
            dic={}
            try:
                year=int(i.date_year)
            except:
                year=0
            dic['year']=year
            dic['num']=i.num1
            dic['increased'] = i.num2
            data['data'].append(dic)
        data['data'].sort(key=lambda x:x['year'])
        return data


class GovernmentTechOut(db.Model):
    __tablename__='shh_government_out'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'comment':'技术流出所属地区'}
    key=db.Column(Integer, primary_key=True, autoincrement=True)
    name=db.Column(String(255),comment='省市名称')
    num=db.Column(Integer,comment='数量')
    ID=db.Column(String(255),comment='行政区域')
    UN_ID = db.Column(String(255),comment='行政区id')

    def get_data(self,uid):
        dataquery=self.query.filter_by(UN_ID=uid).all()
        data={}
        data['gov']=dataquery[0].ID
        data['uid']=dataquery[0].UN_ID
        data['data']=[]
        for i in dataquery:
            dic={}
            dic['region']=i.name
            dic['num']=i.num
            data['data'].append(dic)
        return data


