from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from datetime import datetime
from sqlalchemy import Integer, String, SmallInteger
# from app import db
from contextlib import contextmanager


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e


db = SQLAlchemy()

class Base(db.Model):
    __abstract__=True
    create_time = db.Column(db.DateTime ,default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now)
    # status = Column(SmallInteger, default=1)  # 软删除

    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        print(item, 'hehe')
        return item

# class DictType(db.Model):
#     __tablename__='dicttype'
#     id = db.Column(Integer,)
#     dict_name = db.Column(String(32))
#     dict_type = db.Column(String(32))
#     status = db.Column(SmallInteger,default = 1)

class DictData(db.Model):
    __tablename__='dictdata'
    id = db.Column(Integer,autoincrement=True,primary_key=True)
    # dict_code = db.Column(Integer)
    dict_name = db.Column(String(32))
    dict_sort = db.Column(Integer)
    dict_label = db.Column(String(32))
    status = db.Column(SmallInteger,default = 1)

    @staticmethod
    def insert_dict():
        data_dicts = {'project_type':['挂牌项目','成交项目'],
                     'deal_type':['正式挂牌','意向挂牌','非公开协议成交']}
        for name in data_dicts:
            for label in data_dicts[name]:
                labeldata = DictData.query.filter_by(dict_label=label,dict_name=name).first()
                # typedata = DictData.query.filter_by(dict_name=name).first()
                if labeldata is None:
                    sort = DictData.query.filter_by(dict_name=name).count()+1
                    data = DictData(dict_name=name,dict_sort=sort,dict_label=label)
                    db.session.add(data)
        db.session.commit()

def str_to_int(strdata):
    try:
        return int(strdata)
    except:
        return 0



