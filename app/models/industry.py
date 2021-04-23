from app.models import db
from sqlalchemy import Integer,String,Float
from operator import itemgetter
from itertools import groupby
import math

class IndustryFever(db.Model):
    __tablename__='shh_industry_fever'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'comment':'市场热度初始值'}
    key=db.Column(Integer, primary_key=True, autoincrement=True)
    industry_id=db.Column(String(255),comment='产业ID')
    parent_id=db.Column(String(255),comment='上级ID')
    name=db.Column(String(255),comment='产业名称')
    level = db.Column(Integer, comment='产业级别')
    num=db.Column(Integer,comment='数量')
    f_value=db.Column(String(255),comment='热度')
    time_slot = db.Column(String(255),comment='时间段')
    ID=db.Column(String(255),comment='行政区域')
    UN_ID = db.Column(String(255),comment='行政区id')

    def get_data(self):
        dataquery=self.query.filter_by(level=1).order_by(db.desc(self.name)).all()
        data={}
        data['data']=[]
        for i in dataquery:
            dic={}
            dic['industry_id'] = i.industry_id
            dic['parent_id'] = i.parent_id
            dic['industry'] = i.name
            dic['level']=i.level
            # fever = float(i.f_value)
            try:
                fever=float(i.f_value)
                # if log:
                # fever=round(math.log(fever*10+2.8),3)
            except:
                fever=0
            dic['fever']=fever
            dic['time_slot']=i.time_slot
            dic['num']=i.num
            data['data'].append(dic)
            data['data'].sort(key=lambda x: x['fever'], reverse=False)
        return data


class IndustryFeverMonth(db.Model):
    __tablename__='shh_industry_fever_month'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'comment':'市场热度月度数据'}
    key=db.Column(Integer, primary_key=True, autoincrement=True)
    industry_id=db.Column(String(255),comment='产业ID')
    parent_id=db.Column(String(255),comment='上级ID')
    name=db.Column(String(255),comment='产业名称')
    level=db.Column(Integer,comment='产业级别')
    num = db.Column(Integer, comment='数量')
    f_value=db.Column(String(255),comment='热度')
    time_slot = db.Column(String(255),comment='时间段')
    ID=db.Column(String(255),comment='行政区域')
    UN_ID = db.Column(String(255),comment='行政区id')

    def get_data(self,log=False):
        dataquery=self.query.filter_by(level=1,).all()
        data={}
        data['data']=[]
        content=[]
        for i in dataquery:
            dic={}
            dic['industry_id'] = i.industry_id
            dic['parent_id'] = i.parent_id
            dic['industry'] = i.name
            dic['level']=i.level
            try:
                fever=float(i.f_value)
                if log:
                    fever=round(math.log(fever*10+2.8),3)
            except:
                fever=0
            try:
                dic['fever']=fever
                dic['time_slot']=i.time_slot
                dic['year'],dic['month']=[int(t) for t in i.time_slot.split('-')]
                dic['num']=i.num
                content.append(dic)
            except:
                pass
        content.sort(key=lambda x: x['month'])
        content.sort(key=lambda x:x['year'])
        content.sort(key=lambda x: x['industry'])
        for industry, items in groupby(content, key=itemgetter('industry')):
            item = {}
            info = list(items)
            item['industry'] = industry
            # item['items'] = info
            item['years'] = [i['time_slot'] for i in info]
            item['feveries'] = [i['fever'] for i in info]
            data['data'].append(item)
        return data

class IndustryPrice(db.Model):
    __tablename__='shh_industry_price'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'comment':'市场价格初始数据'}
    key=db.Column(Integer, primary_key=True, autoincrement=True)
    industry_id=db.Column(String(255),comment='产业ID')
    parent_id=db.Column(String(255),comment='上级ID')
    name=db.Column(String(255),comment='产业名称')
    level = db.Column(Integer, comment='产业级别')
    p_value=db.Column(String(255),comment='价格')
    time_slot = db.Column(String(255),comment='时间段')
    ID=db.Column(String(255),comment='行政区域')
    UN_ID = db.Column(String(255),comment='行政区id')

    def get_data(self):
        dataquery=self.query.filter_by(level=1).order_by(db.desc(self.name)).all()
        data={}
        data['data']=[]
        for i in dataquery:
            dic={}
            dic['industry_id'] = i.industry_id
            dic['parent_id'] = i.parent_id
            dic['industry'] = i.name
            dic['level']=i.level
            try:
                price=float(i.p_value)
            except:
                price=0
            dic['price']=price
            dic['time_slot']=i.time_slot
            data['data'].append(dic)
            data['data'].sort(key=lambda x: x['price'], reverse=False)
        return data


class IndustryPriceMonth(db.Model):
    __tablename__='shh_industry_price_month'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'comment':'市场价格月度数据'}
    key=db.Column(Integer, primary_key=True, autoincrement=True)
    industry_id=db.Column(String(255),comment='产业ID')
    parent_id=db.Column(String(255),comment='上级ID')
    name=db.Column(String(255),comment='产业名称')
    p_value=db.Column(String(255),comment='价格')
    level=db.Column(Integer,comment='产业级别')
    time_slot = db.Column(String(255),comment='时间段')
    ID=db.Column(String(255),comment='行政区域')
    UN_ID = db.Column(String(255),comment='行政区id')

    def get_data(self):
        dataquery = self.query.filter_by(level=1, ).all()
        data = {}
        data['data'] = []
        content = []
        for i in dataquery:
            dic = {}
            dic['industry_id'] = i.industry_id
            dic['parent_id'] = i.parent_id
            dic['industry'] = i.name
            dic['level'] = i.level
            try:
                price = float(i.p_value)
            except:
                price = 0
            try:
                dic['price'] = price
                dic['time_slot'] = i.time_slot
                dic['year'], dic['month'] = [int(t) for t in i.time_slot.split('-')]
                content.append(dic)
            except:
                pass
        content.sort(key=lambda x: x['month'])
        content.sort(key=lambda x: x['year'])
        content.sort(key=lambda x: x['industry'])
        for industry, items in groupby(content, key=itemgetter('industry')):
            item = {}
            info=list(items)
            item['industry'] = industry
            # item['items'] = info
            item['years']=[i['time_slot'] for i in info]
            item['price']=[i['price'] for i in info]
            data['data'].append(item)
        return data