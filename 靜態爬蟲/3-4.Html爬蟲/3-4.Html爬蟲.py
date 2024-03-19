# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 02:34:02 2018

@author: linzino
"""

from bs4 import BeautifulSoup
import re

# 網頁字串
html_doc = """
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1 id='h1title'>This is a Heading</h1>
<p class = 'pc'>This is a paragraph1.</p>
<p class = 'pc'>This is a paragraph2.</p>
<div class = 'Box'>
<a class="sister_grg" href="http://example.com/elsie" id="link1">Elsie</a>
</div>
<div class = 'Box'>
<a class="sister_g6x" href="http://example.com/lacie" id="link2">Lacie</a>
</div>
<div class = 'Box'>
<a class="sister_vs4" href="http://example.com/tillie" id="link3">Tillie</a>
</div>
</body>
</html>
"""

# 丟入bs4解析器
soup = BeautifulSoup(html_doc,'html.parser')

# 印出整理過的格式
print(soup.prettify())


## 各種抓取標籤方法
# 找到所有 p標籤
soup.find_all('p')

# 找到所有 a標籤
for link in soup.find_all('a'):
    print(link.get('href'))

# 根據id
soup.find(id="h1title")
soup.find(id="link3")
# 根據class
soup.find_all('p',{'class':'pc'})
# 根據class  只要有sister的都抓
soup.find_all('a', re.compile('sister_'))

# 使用選擇器抓取
soup.select('.Box')

# 抓內部文字
# <a class="sister_vs4" href="http://example.com/tillie" id="link3">Tillie</a>
atag = soup.find(id="link3")
atag.text
atag['class']
atag['href']



# 真實網站的爬蟲程式碼
import requests
from bs4 import BeautifulSoup

url = 'https://hahow.in/'
#請求網站
list_req = requests.get(url)
#將整個網站的程式碼爬下來
soup = BeautifulSoup(list_req.content, "html.parser")
soup.text