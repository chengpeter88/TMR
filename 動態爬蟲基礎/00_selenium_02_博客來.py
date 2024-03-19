# %%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time


# %%
# ------ 設定要前往的網址 ------
url = 'https://www.books.com.tw/'   

# %%

# ------ 開啟 Chrome browser ------
browser = webdriver.Chrome(service=ChromeService())

# %%
# ------ 前往該網址------
browser.get(url)    

# %%
# ------ 問題：去除廣告 close_top_banner------
browser.find_element(By.ID,"close_top_banner").click()


# %%
# ------ 查詢的關鍵字 ------
keyword = '行銷資料科學'


# %%
# 問題：找到可以輸入search-bar的xpath，並send_keys
browser.find_element(By.XPATH,'//*[@id="key"]').send_keys(keyword)


# %%
# ------ 點擊搜尋 ------
# 問題：找到可以點擊搜尋的xpath 
browser.find_element(By.XPATH,'//*[@id="search"]/div/button').click()


# %%
# ------ 執行 "滑鼠滾動的" JavaScript指令 ------
# 向下
js = 'window.scrollTo(0, document.body.scrollHeight);'
browser.execute_script(js)

# 向上
js = 'window.scrollTo(0, 10);'
browser.execute_script(js)

browser.close()

