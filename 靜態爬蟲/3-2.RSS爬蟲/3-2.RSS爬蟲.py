# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:39:50 2019

@author: Ivan
"""
import pandas as pd
import feedparser
NewsFeed = feedparser.parse("https://udn.com/rssfeed/news/2/6638?ch=news")

# 顯示第一筆新聞的標題
NewsFeed.entries[0]['title'] #字典方式
NewsFeed.entries[0].title #屬性方式

# 顯示第一筆新聞的內文
firstNew = NewsFeed.entries[0].summary

#進行文字處理
firstNew[  firstNew.find('</p><p>')+7:  -4   ]

#---------------整理出今天所有的新聞標題與內文------------------
title=[]
article=[]
thetime=[]
for i in NewsFeed.entries:
    title.append(i['title'])
    
    new = i.summary
    article.append(new[  new.find('</p><p>')+7:  -4   ])
    thetime.append(i['published'])

dic = {
       '標題': title,
       '文章內容': article,
       '文章時間': thetime
       }

data= pd.DataFrame(dic)