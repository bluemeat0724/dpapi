# -*- coding: utf-8 -*-
"""
Created on Mon May  7 20:44:20 2018

@author: G
"""

import pymysql
connection=pymysql.connect(host='localhost',user='root',password='19901990',db='iris',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        sql= " SELECT * FROM `iris_with_id` WHERE `id`=%s"
        cursor.execute(sql,('3',))
        result=cursor.fetchone()
        print(result)
        print(result['id'])
finally:
    connection.close()