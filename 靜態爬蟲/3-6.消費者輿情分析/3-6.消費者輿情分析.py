#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 12:22:00 2019

@author: cheating
"""
import jieba.analyse
import pandas as pd
import jieba
import numpy as np
import matplotlib.pyplot as plt
#plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
jieba.set_dictionary('dict.txt.big')
colrogroup = ['#427f8f','#4a8fa1','#559db0','#66a7b8','#77b1c0','#89bbc8','#9ac5d0','#bdd9e0','#cee3e8','#e0edf0']

# 無意義字元列表，可以自行新增
removeword = ['span','class','f3','https','imgur','h1','_   blank','href','rel',
              'nofollow','target','cdn','cgi','b4','jpg','hl','b1','f5','f4',
              'goo.gl','f2','email','map','f1','f6','__cf___','data','bbs'
              'html','cf','f0','b2','b3','b5','b6','原文內容','原文連結','作者'
              '標題','時間','看板','<','>','，','。','？','—','閒聊','・','/',
              ' ','=','\"','\n','」','「','！','[',']','：','‧','╦','╔','╗','║'
              ,'╠','╬','╬',':','╰','╩','╯','╭','╮','│','╪','─','《','》','_'
              ,'.','、','（','）','　','*','※','~','○','”','“','～','@','＋','\r'
              ,'▁',')','(','-','═','?',',','!','…','&',';','『','』','#','＝'
              ,'\l']

#設定你關心的影劇名稱
movie = ['成為王的男人','皇后的品格','赤月青日','神的測驗',
        '死之詠讚','王牌大律師','Priest驅魔者','加油吧威基基',
        '皮諾丘','魔女寶鑑','好運羅曼史','購物王路易','七次初吻',
        '男朋友','請回答1997','來自星星的你']

# 讀入爬蟲資料
KoreaDrama=pd.read_csv('KoreaDrama_re.csv') #開啟檔案

#----------------------------------分析區--------------------------------------
#所有文章和標題都串在一起
theSTR = KoreaDrama['標題'].sum() + KoreaDrama['內容'].sum()

# 移除無意義字元列
for word in removeword:
    theSTR = theSTR.replace(word,'')
    
'好棒棒'.replace('好', '')

# 關鍵詞提取
keywords=keywords_top=jieba.analyse.extract_tags(theSTR,topK=10, withWeight=True)

### 問題:
### 如何把keywords畫成棒狀圖
keywords_top_DF = pd.DataFrame(keywords)


plt.bar(keywords_top_DF[0], keywords_top_DF[1], color=colrogroup) #給予線標籤
plt.xlabel('關鍵字',fontsize=15)
plt.ylabel('熱度',fontsize=15)
plt.title('市場關鍵字排名',fontsize=20)
plt.show()

#-------------------------------土法煉鋼分析------------------------------------
#切詞
words = list(jieba.cut(theSTR, cut_all=False))

# 計算每個keyword共出現幾次
#word_voice= []
#for i in words:
#    word_voice.append(words.count(i))

    
dic = {
       'word':words,
       'word_voice':word_voice
       }

word_voiceDF = pd.DataFrame(dic)


### 問題:
### 如何移除重複
word_voiceDF = word_voiceDF.drop_duplicates('word')

#-------------------------------品牌聲量分析------------------------------------
### 問題:
### 以影劇為單位，去計算每個影劇，在所有資料中的聲量
mv_voice= []
for j in movie:
    mv_voice.append(words.count(j))
    

plt.bar(movie, mv_voice, color=colrogroup) #給予線標籤
plt.xticks(fontsize=15,rotation=90) 
plt.xlabel('關鍵字', fontsize=15)
plt.ylabel('熱度', fontsize=15)
plt.title('熱門影集排名', fontsize=20)
plt.show()

#-------------------------------原始資料擷取------------------------------------
import re
findword = '血跡'
for m in re.finditer(findword, theSTR):
    print(theSTR[m.start()-50 : m.start()+50])


#----------------------------------點陣圖--------------------------------------
#所有文章和標題都串在一起
theSTR = KoreaDrama['標題'].sum() + KoreaDrama['內容'].sum()

# 移除無意義字元列
for word in removeword:
    theSTR = theSTR.replace(word,'')
    
#切詞
words = list(jieba.cut(theSTR, cut_all=False))

#以影劇為單位，去計算每個影劇，在所有資料中的聲量
mv_voice= []
for j in movie:
    mv_voice.append(words.count(j))

#存成csv檔案
voice_df = pd.DataFrame(mv_voice)
voice_df.columns = ['聲量']
voice_df.index = movie
voice_df.to_csv('voice_df.csv', encoding = 'utf-8')

# 計算聲量的平均
avg=np.mean(mv_voice)

# 豆瓣上面的評分
bean = [6.9, 7.5, 8.6, 7.8, 8.5, 9.3, 6.8, 8.6, 8.2, 5.9, 6.7, 7.2, 5.8, 7.0, 9.0, 8.3]
#繪圖

plt.figure(figsize=(20,10))
#判斷四個象限所在的位置，來決定顏色
voice_list =[]
bean_list = []
axe_list = []
for i in range(len(bean)):
    if bean[i]>8 and mv_voice[i] >avg:#第一象限
        color = '#66b877'
        axe = '第一象限'
        
    elif bean[i]>8 and mv_voice[i] <= avg:#第四象限
        color = '#66a7b8'
        axe = '第四象限'
        
    elif bean[i]<=8 and mv_voice[i] > avg:#第三象限
        color = '#b866a7'
        axe = '第二象限'
        
    else:#第二象限
        color = '#b87766'
        axe = '第三象限'
    
    # 繪製圓點
    plt.scatter(bean[i],mv_voice[i], color=color,s=500*mv_voice[i],alpha=0.5)
    # 加上文字註解
    plt.text(bean[i],mv_voice[i], movie[i], fontsize=15 )
    
    voice_list.append(mv_voice[i])
    bean_list.append(bean[i])
    axe_list.append(axe)
    
voice_df = pd.DataFrame(voice_list, columns = ['追劇率']) 
bean_df = pd.DataFrame(bean_list, columns = ['評分'] ) 
axe_df = pd.DataFrame(axe_list, columns = ['象限'] )     
final1 = pd.concat([voice_df,bean_df,axe_df], axis = 1)
final1['劇名']  = movie
    
plt.axhline(avg, color='c', linestyle='dashed', linewidth=1) # 繪製平均線 
plt.axvline(8, color='c', linestyle='dashed', linewidth=1) # 繪製平均線    

plt.title("追劇率 V.S 豆瓣評分",fontsize=30)#標題
plt.ylabel("追劇率（次數）",fontsize=20)#y的標題
plt.xlabel("豆瓣評分（0～10）",fontsize=20) #x的標題

#plt.savefig('消費者輿情分析'+'.png', dpi=300)
plt.show()
