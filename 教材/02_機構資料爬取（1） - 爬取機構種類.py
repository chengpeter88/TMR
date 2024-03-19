# %% [markdown]
# # 02_機構資料爬取（1） - 爬取機構種類

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
# ## 首先，我們先執行到顯示"臺師大"頁面的地方

# %%
search= "臺灣師範大學"

# 開啟chromedriver
url = 'https://www.google.com.tw/maps?hl=zh-TW&tab=rl&authuser=0'  
browser.get(url)

# 輸入欲搜尋的店家名稱
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'searchboxinput.xiQnY')))
search_input = browser.find_elements(By.CLASS_NAME,'searchboxinput.xiQnY')[0]
search_input.send_keys(search)

# 定位搜尋鍵並點擊
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'mL3xi')))
search_click = browser.find_elements(By.CLASS_NAME,'mL3xi')[0]
search_click.click()

print("Finish Searching! " + search)

# %% [markdown]
# ## 利用Soup取得網頁元素框架

# %%
time.sleep(2)

soup = Soup(browser.page_source,"lxml")

# %% [markdown]
# ## 使用button爬取學校種類

# %%
school_type=[]

school_category2 = soup.find_all('button',{'class':"DkEaL"})[0].text

if len(school_category2)!=0:
    school_type.append(school_category2)
else:
    school_type.append('')

print("學校種類:", school_type)

# %% [markdown]
# ## 建立dataframe

# %%
school=pd.DataFrame({"學校名稱":[search],"學校種類":school_type})
school

browser.close()
# %% [markdown]
# ## 小練習
# ### 請嘗試爬取上堂課指定題目 search="成大" 之「學校種類」(需先執行下面段落)

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
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'mL3xi')))
search_click = browser.find_elements(By.CLASS_NAME,'mL3xi')[0]
search_click.click()

print("Finish Searching! " + search)

# %%
# 利用Soup取得網頁元素框架
time.sleep(2)

soup = ???(browser.page_source,"lxml")

# 使用button爬取該店家種類
school_type=[]

school_category2 = soup.find_all('button',{'class':"DkEaL"})[0].text

if len(school_category2)!=0:
    school_type.append(school_category2)
else:
    school_type.append('')

print("學校種類:", ???)

# 建立dataframe
school=???
school

browser.close()

