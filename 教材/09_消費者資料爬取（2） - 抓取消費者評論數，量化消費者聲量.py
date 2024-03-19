# %% [markdown]
# # 09_消費者資料爬取（2） - 抓取消費者評論數，量化消費者聲量

# %% [markdown]
# ## 引入套件

# %%
import time
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
browser = webdriver.Chrome(service=ChromeService())
from bs4 import BeautifulSoup as Soup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

# %% [markdown]
# ## 首先，我們先執行到顯示"臺師大"頁面的地方，並利用Soup取得網頁元素框架

# %%
search= "國臺北大學"

# 開啟chromedriver
url = 'https://www.google.com.tw/maps?hl=zh-TW&tab=rl&authuser=0'  
browser.get(url)

# 輸入欲搜尋的店家名稱
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'searchboxinput.xiQnY')))
search_input = browser.find_elements(By.CLASS_NAME,'searchboxinput.xiQnY')[0]
search_input.send_keys(search)

# 定位搜尋鍵並點擊
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, 'searchbox-searchbutton')))

search_click = browser.find_elements(By.ID,'searchbox-searchbutton')[0]

search_click.click()

#選擇第一個點選

try:
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME,'hfpxzc')))
    choose_first_item_click=browser.find_elements(By.CLASS_NAME,'hfpxzc')[0]
    choose_first_item_click.click()
except:
    print('不用點到第二層')
print("Finish Searching! " + search)
time.sleep(2.85)
soup = Soup(browser.page_source,"lxml")

# %% [markdown]
# ## 爬取店家總評論數

review_num = []
reviews = soup.find_all(class_="F7nice")

if reviews:
    review_sum = reviews[0].text[3:].replace("(","").replace(")","").replace(",","")
    review_num.append(review_sum)
    print("學校總評論數：", review_num)
else:
    print("未找到評論數")

#%%
from bs4 import BeautifulSoup
import re

# 假設 html 是你的網頁內容
html = '''<div class="F7nice " jslog="76333;mutable:true;"><span><span aria-hidden="true">4.4</span><span class="ceNzKf" role="img" aria-label="4.4 星級 "><span class="rFrJzc"></span><span class="rFrJzc"></span><span class="rFrJzc"></span><span class="rFrJzc"></span><span class="rFrJzc UpDOYb"></span></span></span><span><span><span aria-label="885 則評論">(885)</span></span></span></div>'''

soup = BeautifulSoup(html, 'html.parser')

# 使用 find 方法找到第一個含有特定 aria-label 屬性的 span 元素
span = soup.find('span', {'aria-label': re.compile('.*則評論')})

# 如果找到了元素，則印出其文字內容
if span:
    print(span.text)  # 輸出：(885)
else:
    print('未找到元素')

# %%
#舊的無法用
review_num = []
reveiw_sum=soup.find_all(class_="F7nice mmu3tf")[0].text[3:].replace("(","").replace(")","").replace(",","")
review_num.append(reveiw_sum)
print("學校總評論數：", review_num)


review_num = []
reviews = soup.find_all(class_="F7nice mmu3tf")

if reviews:
    review_sum = reviews[0].text[3:].replace("(","").replace(")","").replace(",","")
    review_num.append(review_sum)
    print("學校總評論數：", review_num)
else:
    print("未找到評論數")


# %%
school=school=pd.DataFrame({"學校名稱":search,"學校總評論數":review_num})
school

browser.close()
# %% [markdown]
# ## 小練習
# ### 請嘗試爬取上堂課指定題目 search="成大" 之「學校總評論數」(需先執行下面段落)

# %%
search= "成大"

# 開啟chromedriver
url = 'https://www.google.com.tw/maps?hl=zh-TW&tab=rl&authuser=0'  
browser = webdriver.Chrome(service=ChromeService())
browser.get(url)

# 輸入欲搜尋的店家名稱
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'searchboxinput.xiQnY')))
search_input = browser.find_elements(By.CLASS_NAME,'searchboxinput.xiQnY')[0]
search_input.send_keys(search)

# 定位搜尋鍵並點擊
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, 'searchbox-searchbutton')))

search_click = browser.find_elements(By.ID,'searchbox-searchbutton')[0]

search_click.click()

#選擇第一個點選

try:
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME,'hfpxzc')))
    choose_first_item_click=browser.find_elements(By.CLASS_NAME,'hfpxzc')[0]
    choose_first_item_click.click()
except:
    print('不用點到第二層')
print("Finish Searching! " + search)
time.sleep(2.85)
soup = Soup(browser.page_source,"lxml")

# %%
# 爬取學校總評論數
review_num=[]
reveiw_sum.append(soup.find_all(class_="???")[0].text[3:].replace("(","").replace(")","").replace(",",""))
print("學校總評論數：", review_num)

# 建立df
school=school=pd.DataFrame({"學校名稱":search,"學校總評論數":???})
school

browser.close()
