# 總分為 245分
# 第一段：145分
# 第二段：100分
# 及格分數為 140 分

#---------第一段：for、list、function----------

# %%
# 問題：使用 for 迴圈（2行），印出1、2、3、4、5
# 10分
for i in range(1, 6):
    print(i)

# %%
# 問題：請將下述 list 附加上：'TMR課程好'
# 10分
tmrlist = ['今日頭條新聞，TMR公司開設行銷資料科學專班', 
           '好棒棒']
tmrlist.append('TMR課程好')
print(tmrlist)

# %%
# 問題：請將下述 list 中，「有」 TMR 的句子以 list 的方式儲存起來
# 10分
tmrlist = ['今日頭條新聞，TMR公司開設行銷資料科學專班', 
           '好棒棒', 'TMR課程好', '我愛daphne', '我愛howard']
tmrlist2 = []
for i in tmrlist:
    if 'TMR' in i:
        tmrlist2.append(i)
print(tmrlist2)


# %%
# 問題：請將下述 list 中，「沒有」 TMR 的句子以list的方式儲存起來
# 10分
tmrlist = ['今日頭條新聞，TMR公司開設行銷資料科學專班', 
           '好棒棒', 'TMR課程好', '我愛daphne', '我愛howard']
tmrlist3 = []
for i in tmrlist:
    if 'TMR' not in i:
        tmrlist3.append(i)
print(tmrlist3)

# %%
# 問題：製作一個 function，請完成下述的「find_ky」。
# 25分
'''
下述為這個 function 的 input、output 說明與舉例。
input：
    1.可以輸入不同的list --> input_list
    2.從list裡面找出關鍵字 --> keyword

output：
    - 從輸入的 list 中，找出有「關鍵字」的句子，並以 list 存出來

舉例：
    1. 從tmrlist（可以替換）中找出 'daphne'字詞的句子，並存成list
    2. funlist經過 find_ky(input_list, keyword) 的function後，可以產出僅有daphne的字詞list

'''
funlist =  ['今日頭條新聞，TMR公司開設行銷資料科學專班', 
           '好棒棒', 'TMR課程好','我愛daphne', '我愛howard']

def find_ky(input_list, keyword):
    kylist = []
    for i in input_list:
        if keyword in i:
            kylist.append(i)
    return kylist   

print(find_ky(funlist, 'daphne'))


# %%
# 問題：製作一個 function，請完成下述的「not_find_ky」。
# 10分
'''
下述為這個 function 的 input、output 說明與舉例。
input: 
    1.可以輸入不同的list
    2.從list裡面找出「非」關鍵字

output
    - 從list裡面找出有「非」「關鍵字」的句子，並以list存出來

舉例：從tmrlist（可以替換）中找出 「非」'daphne'字詞的句子，並存成list

'''
funlist =  ['今日頭條新聞，TMR公司開設行銷資料科學專班', 
           '好棒棒', 'TMR課程好','我愛daphne', '我愛howard']

def not_find_ky(input_list, keyword):
    nkylist = []
    for i in input_list:
        if keyword not in i:
            nkylist.append(i)
    return nkylist
not_find_ky(funlist, 'daphne')
    
#---------第二段：爬蟲與pandas----------
    
# %%
import time
import random 
import pandas as pd
import numpy as np
import json


# %%
# 問題：請進入 TWSE 的網站中，輸入 0050（代表臺灣卓越50基金），
# 並將當頁的 DataFrame 資料 request 下來，最後將 request get 的結果存入到 req 的變數中
# TWSE網址：(https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html)
# hint：request 找 preview 裏面的 json 檔案
# hint2：可將 preview.JPG
# 10分

import requests

url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20220401&stockNo=0050'

# Send the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # The JSON data is stored in the response
    req = response.json()
else:
    print("Failed to retrieve data: Status code", response.status_code)
    req = None





# %%
# 問題：接上題，將 Request 下來的資料，轉換成 json 形式，並存在一個 soup 的物件中
# hint: json.loads(  )
# 20分
import json
soup = json.loads(response.text)
soup

# %%
# 問題：請將 soup（json檔）裏面的 stat 欄位（key值）與 value 值刪除
# 5分
del soup['stat']

# %%
# 問題：請將 soup 裏面的 title 欄位的 value 值取出來到 title 物件裏面
# 5分
title = soup['title']

# %%
# 問題：請將 soup 轉換成如附檔：2330.csv 所示，並存成 csv 檔案，名稱：0050.csv
# 15分
import pandas as pd
df = pd.DataFrame(soup['data'], columns=soup['fields'])
df.to_csv('0050.csv', index=False)


# %%
# 問題：請將股票號碼與名稱放到「股票」新欄位中，如同附檔：2330_2.csv 所示，並存成 csv 檔案，名稱：0050_2.csv
# hint：善用 title 變數 + split 函數
# 15分


# 讀取 CSV 文件
title = "0050 元大台灣50"

# 使用 split 函數分割 title
stock_info = title.split()

# 將股票號碼和名稱添加到新的「股票」欄位中
df['股票'] = stock_info[0] + " " + stock_info[1]

# 將 DataFrame 存儲為 CSV 文件
df.to_csv('0050_2.csv', index=False)



# %%
### 重要訊息
# !pip install selenium==4.3.0 以上
# 導入套件
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup as Soup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# %%
# 問題：請使用 ChromeDriverManager 開啟 webdriver
# 10分
# 開啟網頁
browser = webdriver.Chrome(service=ChromeService())


# %%
# 限制網頁大小在(1500, 1000)
browser.set_window_size(1500, 1000)

# %%
# 跳轉到 google 新聞，台灣版
url = 'https://news.google.com/home?tab=rn&hl=zh-TW&gl=TW&ceid=TW:zh-Hant'

# 問題：請控制 browser 到指定的 url 
# 10分
browser.get(url)


# 等待網頁架構出現
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'Ly25Ed')))

# %%
# 搜尋資料科學
# 問題：找到輸入框元素並輸入資料科學 
# 20分
# 加分題: 有使用 WebDriverWait 等待元素出現 + 5分
search = '資料科學'

WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'Ax4B8.ZAGvjd')))
search_input = browser.find_element(By.CLASS_NAME, 'Ax4B8.ZAGvjd')
search_input.send_keys(search)


# %%
# 點擊搜尋
# 問題：找到搜尋按鈕元素並點擊 
# 20分
# 加分題: 有使用 WebDriverWait 等待元素出現 + 5分
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'gb_Je')))
search_click = browser.find_element(By.CLASS_NAME, 'gb_Je')
search_click.click()



# %%
# 爬取第一則的標題
# 問題：請等待標題的元素出現，接著利用 soup & browser.page_source 爬取第一則的標題
# 40分
# 加分題: 有使用 WebDriverWait 等待元素出現 + 5分
wait=WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'IFHyqb.DeXSAc')))

soup = Soup(browser.page_source, 'html.parser')

# 尋找所有匹配的元素
elements = soup.find_all('a', class_='JtKRv')

# 從中選擇正確的元素
for element in elements:
    if "NASA 透過AI 搜尋加速科學發展" in element.text:
        title = element.text
        break
print(title) 
first_title = title    
#first_title = soup.select_one('body.tQj5Y.ghyPEc.IqBfM.lF2Cpe.k1PYFe.eCItwe.dm7YTc.hZmmCc.EIlDfe.cjGgHb.d8Etdd.LcUz9d.b30Rkd.e2G3Fb:nth-child(2) c-wiz.zQTmif.SSPGKf:nth-child(31) div.T4LgNb:nth-child(1) main.IKXQhd div.UW0SDc c-wiz.D9SJMe c-wiz.PO9Zff.Ccj79.kUVvS:nth-child(1) c-wiz.XBspb:nth-child(2) article.IFHyqb.DeXSAc:nth-child(1) div.m5k28 div.XlKvRb > a.WwrzSb').text

# %%
# 列印出標題
print(first_title)



