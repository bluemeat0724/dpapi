from flask import url_for

class InnovationCenterTableView:
    def __init__(self,dataquery):
        self.__dataquery = dataquery
        self.items=self.__parse()

    def __parse(self):
        items=[]
        for i in self.__dataquery:
            item=self.__itemparse(i)
            items.append(item)
        return items

    def __itemparse(self,item):
        id=item.id
        name=item.name
        type_one=item.type_one
        type_two=item.type_two
        if item.image_url is not None:
            imageurl=url_for('api_1_0.uploaded_file',filename=item.image_url)
        else:
            imageurl=''
        r={
            'id':id,
            'name':name,
            'type_one':type_one,
            'type_two':type_two,
            'image':imageurl
        }
        return r