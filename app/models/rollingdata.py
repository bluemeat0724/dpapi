from app.models import db,Base
from sqlalchemy import Integer, String
from app.models import DictData
from sqlalchemy import desc
from datetime import datetime
from flask import url_for

class InnocationCenter(Base):
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(String(32))
    type_one_id = db.Column(Integer)
    type_one = db.Column(String(32),default=None)
    type_two_id = db.Column(Integer)
    type_two = db.Column(String(32),default=None)
    image_url = db.Column(String(255))

    def get_data(self,type_one_id):
        ics=self.query.filter_by(type_one_id=type_one_id).all()
        iclist=[]
        for ic in ics:
            iclist.append([ic.name,ic.type_one,ic.type_two,ic.image_url])
        title=iclist[0][1]
        subtitles = list(set([i[2] for i in iclist]))
        d={}
        d['title']=title
        d['content']=[]
        for st in subtitles:
            content={}
            if st not in content:
                content['subtitle']=st
            content['data']=[]#获取名称
            content['dir'] = []
            for i in iclist:
                name=i[0]
                # typeone=i[1]
                typetwo=i[2]
                image=i[3]
                if typetwo==st:
                    content['data'].append(name)
                    if image is None:
                        content['dir'].append('')
                    else:
                        content['dir'].append(url_for('api_1_0.uploaded_file',filename=image))
            d['content'].append(content)
        return d

    def get_sheet(self):
        types=['1','2','3','4']
        data=[]
        for i in types:
            data.append(self.get_data(i))
        return data