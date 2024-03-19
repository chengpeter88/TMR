# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 17:46:46 2019

@author: Ivan
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import datetime

# 資料來源：高雄市政府新聞局https://kcginfo.kcg.gov.tw/json.aspx
#請求的網站
url = 'https://kcginfo.kcg.gov.tw/Json_News.aspx?n=C527413F7300192A'
#開始請求
list_req = requests.get(url)
soup = BeautifulSoup(list_req.content, "html.parser")  #將網站內文爬下來
#將扒下來的文字轉成Json
getjson=json.loads(soup.text)


#------------------資料處理教學-------------------
#取第一筆資料
getjson[0]

#取第一筆資料的內容標題
getjson[0]['Title']

#快速取出所有的標題
for i in getjson:
    print(i['Title'])
    
#篩選所有文章標題中有提到「高雄」字眼的的文章
for i in getjson:
    if '高雄' in i['Title']:
        print(i['Title'])    
    
#將Json資料轉成DataFrame
dfJson = pd.DataFrame(getjson)

#將pubDate欄位轉成時間格式，並且覆蓋
dfJson['pubDate'] = pd.to_datetime(dfJson['pubDate'])
#找到一個月前的日期
month_ago = datetime.datetime.now() - datetime.timedelta(days=30)
#吐出一個月以內的新聞
dfJson[   dfJson['pubDate'] > month_ago   ]
