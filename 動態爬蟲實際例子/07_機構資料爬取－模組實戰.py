# %% [markdown]
# # 07_機構資料爬取－模組實戰

# %% [markdown]
# ## 以過去上課案例"臺師大"來查看結果

# %%
from util import google_review_store

# %%
school=google_review_store(search="臺灣師範大學")

# %%
school

# %% [markdown]
# ## 使用限制:關鍵字需為最終標的

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
# ## 那我們要怎麼樣在google maps上查看呢?

# %%
# 開啟chromedriver
url = 'https://www.google.com.tw/maps?hl=zh-TW&tab=rl&authuser=0'  
browser.get(url)

# %%
search="立法院"
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
search_input.clear()

# %%
browser.close()

# %% [markdown]
# ## 小練習
# ### 試著使用模組爬取上課指定題目search="成大"

# %%
school=google_review_store(search="私立東吳大學城中校區")

# %%
school



# %%
