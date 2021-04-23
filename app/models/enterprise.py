from app.models import db,str_to_int
from sqlalchemy import Integer,String,Float,desc
from datetime import datetime
import pandas as pd

class EnterpriseApplication(db.Model):
    __tablename__='shh_enterprise_application'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'comment':'专利申请趋势'}
    key=db.Column(Integer, primary_key=True, autoincrement=True)
    name=db.Column(String(255),comment='申请年')
    num=db.Column(Integer,comment='数量')
    ID=db.Column(String(255),comment='企业名称')
    UN_ID = db.Column(String(255),comment='企业id')

    def get_data(self,uid):
        dataquery=self.query.filter_by(UN_ID=uid).order_by(db.desc(self.name)).all()
        data={}
        data['name']=dataquery[0].ID
        data['uid']=dataquery[0].UN_ID
        data['data']=[]
        for i in dataquery:
            dic={}
            dic['year']=i.name
            dic['num']=i.num
            data['data'].append(dic)
        return data


class EnterpriseIndustry(db.Model):
    __tablename__='shh_enterprise_industry'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'comment': '产学研合作'}
    key = db.Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(String(255), comment='机构名称')
    num = db.Column(Integer, comment='数量')
    date_year=db.Column(String(255),comment='申请年')
    ID = db.Column(String(255),comment='企业名称')
    UN_ID = db.Column(String(255),comment='企业id')

    # def get_data(self,uid):
    #     dataquery = self.query.filter_by(UN_ID=uid).all()
    #     data = {}
    #     data['name'] = dataquery[0].ID
    #     data['uid'] = dataquery[0].UN_ID
    #     data['data'] = []
    #     for i in dataquery:
    #         dic = {}
    #         dic['enname'] = i.name
    #         dic['num'] = i.num
    #         dic['year'] = i.date_year
    #         data['data'].append(dic)
    #     return data
    def get_data(self,uid):
        dataquery = self.query.filter_by(UN_ID=uid).all()
        data = {}
        data['name'] = dataquery[0].ID
        data['uid'] = dataquery[0].UN_ID
        data['data'] = []
        for i in dataquery:
            dic = {}
            dic['enname'] = i.name
            dic['num'] = i.num
            dic['year'] = i.date_year
            data['data'].append(dic)
        table=pd.DataFrame(data['data'])

        table = table.pivot(index='enname', columns='year', values='num').fillna('')
        years=[str(i) for i in range(2013,2020)]
        for i in years:
            try:
                table[i]
            except:
                table[i] = ''
        table=table[years]
        tabledata = []
        for i, v in table.iterrows():
            c = {}
            c['enname'] = i
            c['years'] = []
            for y in years:
                yeardic = {}
                yeardic['year'] = y
                yeardic['num'] = v[y]
                c['years'].append(yeardic)
            tabledata.append(c)
        data['data'] = tabledata
        return data


class EnterprisePrice(db.Model):
    __tablename__='shh_enterprise_price'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'comment': '专利资产市场价值分布'}
    key = db.Column(Integer, primary_key=True, autoincrement=True)
    num = db.Column(Integer, comment='序列')
    price = db.Column(Float, comment='价格')
    date_year=db.Column(String(255),comment='申请年')
    ID = db.Column(String(255),comment='企业名称')
    UN_ID = db.Column(String(255),comment='企业id')

    def get_data(self,uid):
        dataquery = self.query.filter_by(UN_ID=uid).order_by(self.num).all()
        data = {}
        data['name'] = dataquery[0].ID
        data['uid'] = dataquery[0].UN_ID
        data['data'] = []
        for i in dataquery:
            dic = {}
            dic['price'] = i.price
            dic['ordernum'] = i.num
            dic['year'] = str_to_int(i.date_year)
            data['data'].append(dic)
        data['data'].sort(key=lambda x: x['year'])
        return data

    @staticmethod
    def get_meandata(uid):
        dataquery = db.session.query(EnterprisePrice.date_year,
                                     db.func.avg(EnterprisePrice.price)
                                     ).group_by(EnterprisePrice.date_year).filter(EnterprisePrice.UN_ID==uid)

        data={}
        data['data']=[]
        for i in dataquery:
            dic={}
            dic['year'] = str_to_int(i.date_year)
            dic['avgprice']= round(i[1],2)
            data['data'].append(dic)
        data['data'].sort(key=lambda x: x['year'])
        return data

    @staticmethod
    def get_maxdata(uid):
        dataquery = db.session.query(EnterprisePrice.date_year,
                                     db.func.max(EnterprisePrice.price)
                                     ).group_by(EnterprisePrice.date_year).filter(EnterprisePrice.UN_ID == uid)

        data = {}
        data['data'] = []
        for i in dataquery:
            dic = {}
            dic['year'] = str_to_int(i.date_year)
            dic['maxprice'] = round(i[1], 2)
            data['data'].append(dic)
        data['data'].sort(key=lambda x:x['year'])
        return data

    @staticmethod
    def get_groups(uid):
        maxdata = db.session.query(EnterprisePrice.date_year,
                                     db.func.max(EnterprisePrice.price)
                                     ).group_by(EnterprisePrice.date_year).filter(EnterprisePrice.UN_ID == uid)
        meandata = db.session.query(EnterprisePrice.date_year,
                                     db.func.avg(EnterprisePrice.price)
                                     ).group_by(EnterprisePrice.date_year).filter(EnterprisePrice.UN_ID == uid)

        data = {}
        data['max'] = []
        data['mean'] = []
        for i in maxdata:
            dic = {}
            dic['year'] = str_to_int(i.date_year)
            dic['price'] = round(i[1], 2)
            data['max'].append(dic)
        data['max'].sort(key=lambda x:x['year'])
        for i in meandata:
            dic = {}
            dic['year'] = str_to_int(i.date_year)
            dic['price'] = round(i[1], 2)
            data['mean'].append(dic)
        data['mean'].sort(key=lambda x:x['year'])
        return data


class EnterprisePatentScore(db.Model):
    __tablename__='shh_enterprise_score'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'comment': '专利质量'}
    key = db.Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(String(255), comment='分数')
    num = db.Column(Integer, comment='数量')
    ID = db.Column(String(255),comment='企业名称')
    UN_ID = db.Column(String(255),comment='企业id')

    def get_data(self,uid):
        dataquery = self.query.filter_by(UN_ID=uid).all()
        data = {}
        data['name'] = dataquery[0].ID
        data['uid'] = dataquery[0].UN_ID
        data['data'] = []
        for i in dataquery:
            dic = {}
            try:
                score=float(i.name.replace('分',''))
            except:
                score=0
            dic['score'] = score
            dic['num'] = i.num
            data['data'].append(dic)
        return data

    @staticmethod
    def getparams():
        dataquery=db.session.query(EnterprisePatentScore.UN_ID,EnterprisePatentScore.ID).distinct(EnterprisePatentScore.UN_ID)
        data=[]
        for i in dataquery:
            dic={}
            dic['uid']=i.UN_ID
            dic['name']=i.ID
            data.append(dic)
        return data



class EnterpriseScore(db.Model):
    __tablename__ = 'enterprise_innovation'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'comment': '企业创新图谱'}
    key = db.Column(Integer, primary_key=True, autoincrement=True)
    overall = db.Column(Float, comment='综合评价评分')
    overallgrade = db.Column(String(30), comment='综合评价等级')
    overalleval = db.Column(String(30), comment='综合评价')
    identity = db.Column(Float, comment='身份特征评分')
    identityGrade = db.Column(String(30), comment='身份特征等级')
    vigor = db.Column(Float, comment='活跃度')
    vigorGrade = db.Column(String(30), comment='活跃度等级')
    creativity = db.Column(Float, comment='创新能力')
    creativityGrade = db.Column(String(30), comment='创新能力等级')
    risk = db.Column(Float, comment='经营风险')
    riskGrade = db.Column(String(30), comment='经营风险等级')
    development = db.Column(Float, comment='发展潜力')
    developmentgrade = db.Column(String(30), comment='发展潜力等级')
    competitiveness = db.Column(Float, comment='竞争实力')
    competitivenessgrade = db.Column(String(30), comment='竞争实力等级')
    ID = db.Column(String(255), comment='企业名称')
    UN_ID = db.Column(String(255), comment='企业id')
    update_time = db.Column(db.DateTime, default=datetime.now)
    create_time = db.Column(db.DateTime, default=datetime.now)

    @staticmethod
    def data_add(paramlist):
        # with db.auto_commit():
        try:
            score=EnterpriseScore()
            score.overall=paramlist[0]
            score.ovallgrade=paramlist[1]
            score.overalleval=paramlist[2]
            score.identity=paramlist[3]
            score.identityGrade=paramlist[4]
            score.vigor=paramlist[5]
            score.vigorGrade=paramlist[6]
            score.creativity=paramlist[7]
            score.creativityGrade = paramlist[8]
            score.risk = paramlist[9]
            score.riskGrade = paramlist[10]
            score.development = paramlist[11]
            score.developmentgrade = paramlist[12]
            score.competitiveness = paramlist[13]
            score.competitivenessgrade = paramlist[14]
            score.update_time = paramlist[15]
            score.ID=paramlist[16]
            score.UN_ID=paramlist[17]
            db.session.add(score)
            db.session.commit()
        except:
            db.session.rollback()

    def get_data(self,uid):
        dataquery = self.query.filter_by(UN_ID=uid).order_by(desc('create_time')).first()
        #竞争实力，发展潜力，经营风险，创新能力，活跃度
        data={}
        data['name'] = dataquery.ID
        data['uid'] = dataquery.UN_ID
        data['competitiveness'] = dataquery.competitiveness
        data['development'] = dataquery.development
        data['risk'] = dataquery.risk
        data['creativity'] = dataquery.creativity
        data['vigor'] = dataquery.vigor

        return data







