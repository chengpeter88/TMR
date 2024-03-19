# %% [markdown]
# # 03_機構資料爬取（2） - 爬取機構地址

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
search= "臺灣師範大學"

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
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME,'hfpxzc')))
    choose_first_item_click=browser.find_elements(By.CLASS_NAME,'hfpxzc')[0]
    choose_first_item_click.click()
except:
    print('不用點到第二層')
print("Finish Searching! " + search)

# %% [markdown]
# ## 利用Soup取得網頁元素框架

# %%
time.sleep(2)

soup = Soup(browser.page_source,"lxml")

# %% [markdown]
# ## 使用button爬取店家地址

# %%
addresses=[]

address_frame = soup.find_all('button', {'data-item-id':"address"})

# %%
address_frame

# %% [markdown]
# ## 使用aria-label搭配strip()得到確切地址

addresses.append(address_frame[0].get('aria-label').strip().strip('地址: '))

print("學校地址：", addresses)

# %%
school=pd.DataFrame({"學校名稱":[search],"學校地址":addresses})
school

browser.close()
# %% [markdown]
# ## 小練習
# ### 請嘗試爬取上堂課指定題目 search="成大" 之「學校地址」(需先執行下面段落)

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
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME,'hfpxzc')))
    choose_first_item_click=browser.find_elements(By.CLASS_NAME,'hfpxzc')[0]
    choose_first_item_click.click()
except:
    print('不用點到第二層')
print("Finish Searching! " + search)
# %%
# 使用Soup取得網頁元素框架
time.sleep(2)

soup = Soup(browser.page_source,"lxml")

# %%
# 建立空白list
addresses=[]

# 使用button爬取
address_frame = soup.find_all('button', {'data-item-id':"???"})

# 利用aria-label及strip抓區準確地址
addresses.append(address_frame[0].get('aria-label').strip().strip('???'))

print("學校地址：", addresses)

# %%
# 建立dataframe
school=pd.DataFrame({"學校名稱":???,"學校種類":addresses})
school

browser.close()
