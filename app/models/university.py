from app.models import db
from sqlalchemy import Integer, String,Float
from sqlalchemy.sql.expression import cast
import pandas as pd
from app.utils.transtools import pinyinstring

class UniversityApplication(db.Model):
    __tablename__='shh_university_application'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'comment':'专利申请趋势'}
    key=db.Column(Integer, primary_key=True, autoincrement=True)
    name=db.Column(String(255),comment='申请年')
    num=db.Column(Integer,comment='数量')
    ID=db.Column(String(255),comment='学校名称')
    UN_ID = db.Column(String(255),comment='学校id')

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

    @staticmethod
    def getparams():
        dataquery=db.session.query(UniversityApplication.UN_ID,UniversityApplication.ID).distinct(UniversityApplication.UN_ID)
        data=[]
        for i in dataquery:
            dic={}
            dic['uid']=i.UN_ID
            dic['name']=i.ID
            data.append(dic)
        return data

class UniversityIndustry(db.Model):
    __tablename__='shh_university_industry'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'comment': '产学研合作'}
    key = db.Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(String(255), comment='机构名称')
    num = db.Column(Integer, comment='数量')
    date_year=db.Column(String(255),comment='申请年')
    ID = db.Column(String(255),comment='学校名称')
    UN_ID = db.Column(String(255),comment='学校id')

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
        years=[str(i) for i in range(2011,2021)]
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


class UniversityPrice(db.Model):
    __tablename__='shh_university_price'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'comment': '专利资产市场价值分布'}
    key = db.Column(Integer, primary_key=True, autoincrement=True)
    num = db.Column(Integer, comment='序列')
    price = db.Column(Float, comment='价格')
    date_year=db.Column(String(255),comment='申请年')
    ID = db.Column(String(255),comment='学校名称')
    UN_ID = db.Column(String(255),comment='学校id')

    # def get_data(self,uid):
    #     # dataquery = self.query.filter(UniversityPrice.UN_ID==uid,UniversityPrice.date_year>2015).all()
    #     dataquery = db.session.query(UniversityPrice.ID,UniversityPrice.UN_ID,UniversityPrice.price,cast(UniversityPrice.date_year,Integer)).filter(UniversityPrice.UN_ID == uid).all()
    #     data = {}
    #     data['name'] = dataquery[0].ID
    #     data['uid'] = dataquery[0].UN_ID
    #     data['data'] = []
    #     print(dir(dataquery[0]))
    #     for i in dataquery:
    #         dic = {}
    #         dic['price'] = i.price
    #         # # dic['ordernum'] = i.num
    #         # try:
    #         #     year=int(i.date_year)
    #         # except:
    #         #     year=0
    #         dic['year'] = i.date_year
    #         # if year > 2009:
    #         #     data['data'].append(dic)
    #         data['data'].sort(key=lambda x: x['year'])
    #     print(len(data['data']))
    #     return data

    # def get_data(self,uid,page):
    #     dataquery = self.query.filter(UniversityPrice.UN_ID==uid,cast(UniversityPrice.date_year,Integer)>2015).opaginate(page,per_page=10000,error_out=False)
    #     data = {}
    #     data['name'] = dataquery.items[0].ID
    #     data['uid'] = dataquery.items[0].UN_ID
    #     data['total_page']=dataquery.pages
    #     data['current_page']=dataquery.page
    #     data['data'] = []
    #     for i in dataquery.items:
    #         dic = {}
    #         dic['price'] = i.price
    #         dic['ordernum'] = i.num
    #         try:
    #             year=int(i.date_year)
    #         except:
    #             year=0
    #         dic['year'] = year
    #         # if year>2015:
    #         #     data['data'].append(dic)
    #         data['data'].sort(key=lambda x:x['year'])
    #     return data

class UniversityProposal(db.Model):
    __tablename__='shh_university_proposal'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'comment': '专利处置方式建议'}
    key = db.Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(String(255), comment='处置建议')
    num = db.Column(Integer, comment='数量')
    ID = db.Column(String(255),comment='学校名称')
    UN_ID = db.Column(String(255),comment='学校id')

    def get_data(self,uid):
        dataquery = self.query.filter_by(UN_ID=uid).all()
        data = {}
        data['name'] = dataquery[0].ID
        data['uid'] = dataquery[0].UN_ID
        data['data'] = []
        for i in dataquery:
            dic = {}
            dic['proposal'] = i.name
            dic['num'] = i.num
            data['data'].append(dic)
        return data

class UniversityRecommend(db.Model):
    __tablename__='shh_university_recommend'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'comment': '高价值专利推荐'}
    key = db.Column(Integer, primary_key=True, autoincrement=True)
    number = db.Column(String(255), comment='申请号')
    title = db.Column(String(255), comment='标题')
    name1 = db.Column(String(255), comment='产业1级')
    name2 = db.Column(String(255), comment='产业2级')
    ID = db.Column(String(255),comment='学校名称')
    UN_ID = db.Column(String(255),comment='学校id')

    def get_data(self,uid):
        dataquery = self.query.filter_by(UN_ID=uid).all()
        data = {}
        data['name'] = dataquery[0].ID
        data['uid'] = dataquery[0].UN_ID
        data['data'] = []
        for i in dataquery:
            dic = {}
            dic['number'] = i.number
            dic['title'] = i.title
            dic['type_one'] = i.name1
            dic['type_two'] = i.name2
            data['data'].append(dic)
        return data


class UniversityRegion(db.Model):
    __tablename__='shh_university_region'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'comment': '高校专利受让人区域'}
    key = db.Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(String(255), comment='区域')
    date_year = db.Column(String(255), comment='转让年')
    num = db.Column(String(255), comment='数量')
    ID = db.Column(String(255),comment='学校名称')
    UN_ID = db.Column(String(255),comment='学校id')

    def get_data(self,uid,year):
        dataquery = self.query.filter_by(UN_ID=uid,date_year=year).all()
        data = {}
        data['name'] = dataquery[0].ID
        data['uid'] = dataquery[0].UN_ID
        data['data'] = []
        for i in dataquery:
            dic = {}
            dic['area'] = i.name
            dic['year'] = i.date_year
            dic['num'] = i.num
            data['data'].append(dic)
        return data

    def get_data_byregion(self,uid):
        dataquery = db.session.query(
            # UniversityRegion.ID, UniversityRegion.UN_ID,
            UniversityRegion.name,
                                db.func.sum(UniversityRegion.num)).filter_by(UN_ID=uid).group_by(UniversityRegion.name).all()
        data={}
        # data['name'] = dataquery[0][0]
        # data['uid'] = dataquery[0][1]
        data['data'] = []
        for i in dataquery:
            dic = {}
            dic['area'] = i[0]
            dic['num'] = i[1]
            data['data'].append(dic)
        return data

    def getregiondata(self,uid):
        dataquery = db.session.query(
            # UniversityRegion.ID, UniversityRegion.UN_ID,
            UniversityRegion.name,
                                db.func.sum(UniversityRegion.num)).group_by(UniversityRegion.name).all()
        data={}
        # data['name'] = dataquery[0][0]
        # data['uid'] = dataquery[0][1]
        data['data'] = []
        for i in dataquery:
            dic = {}
            dic['area'] = i[2]
            dic['num'] = i[3]
            data['data'].append(dic)
        return data



