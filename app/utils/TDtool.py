from datetime import datetime
from datetime import timedelta
import requests,json
from app.secure import TD_PASSWORD,TD_TOKEN,TD_USERNAME


sitesid=[15938737, 16038030, 16058658, 16058920, 16075740, 16199665]
domains=['stte.com','u-shares.com','gaoxiaotech.com','techdeal.cn','fin.stte.com','peiyuku.com']
createtime=['20201022', '20201120', '20201126', '20201126', '20201202', '20210112']

def gettrendingdata():
    reporturl='https://api.baidu.com/json/tongji/v1/ReportService/getData'
    datetimenow=datetime.now().strftime('%Y%m%d')
    requestdata={
        "header": {
            "account_type": 1,
            "password":TD_PASSWORD,
            "token": TD_TOKEN,
            "username": TD_USERNAME
        }
    }
    results=[]

    for i in range(6):
        body={
                "site_id": sitesid[i],
                "start_date": createtime[i],
                "end_date": datetimenow,
                "metrics": "pv_count,visitor_count,ip_count",
                "method": "trend/time/a"
            }
        requestdata['body']=body
        r=requests.post(reporturl,data=json.dumps(requestdata))
        sitesum=json.loads(r.text)['body']['data'][0]['result']['sum'][0]
        results.append({'name':domains[i],'pv':sitesum[0],'uv':sitesum[1],'ip':sitesum[2]})
    pv=0
    uv=0
    ip=0
    for i in results:
        pv+=i['pv']
        uv+=i['uv']
        ip+=i['ip']
    results.append({'name':'sum','pv':pv,'uv':uv,'ip':ip})
    return results