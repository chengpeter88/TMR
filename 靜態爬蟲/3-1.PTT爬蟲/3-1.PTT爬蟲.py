# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:55:36 2019

@author: Ivan
"""


import pandas as pd
from Ivan_ptt import crawl_ptt_page

## 必要設定的欄位
# 1. 修改ptt板位
# 2. 查看最新的頁數index
KoreaDrama = crawl_ptt_page(Board_Name ='KoreaDrama' ,
                            start =2188 ,page_num= 5)
Elephants = crawl_ptt_page(Board_Name ='Elephants' ,
                            start =4921 ,page_num= 5)

KoreaDrama.to_csv('KoreaDrama_test.csv',encoding = 'utf-8') #存檔
aa = pd.read_csv('KoreaDrama_test.csv',encoding = 'utf-8')
