# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 16:17:47 2019

@author: Ivan
"""

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
from wordcloud import WordCloud
import jieba

#-------使用簡體字典--------
seg_list = jieba.cut("小明硕士毕业于中国科学院计算所，后在日本京都大学深造") 
print(" ".join(seg_list)) # 全模式 

# 簡體對照繁體會有一些問題
text = '''
我只有消瘦的臉孔
所謂軟弱
所謂的順從一向是我
的座右銘'''
words = jieba.cut(text )
print("/ ".join(words))


#-------使用繁體字典--------
import jieba
jieba.set_dictionary('dict.txt.big')

words = jieba.cut(text)
print("/ ".join(words))


# 關鍵詞提取
import jieba.analyse
keywords1=jieba.analyse.extract_tags(text)
print("/".join(keywords1))

# top 3 關鍵字
keywords_top=jieba.analyse.extract_tags(text,topK=3, withWeight=True)

# 總詞數
print('總詞數{}'.format(len(list(jieba.cut(text)))))



#-------繪畫出文字雲--------
cut_text = " ".join(jieba.cut(text))
wordcloud = WordCloud(collocations=False, 
                      font_path='標楷體.ttf', 
                      width=800, 
                      height=600, 
                      margin=2).generate(cut_text)
wordcloud.to_image()  
#存檔
wordcloud.to_image().save('wordcloud.png',"PNG")



