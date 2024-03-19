# %% [markdown]
# # 10_消費者資料爬取（3） - 抓取消費者評論，瞭解消費者在想什麼

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
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME,'hfpxzc')))
    choose_first_item_click=browser.find_elements(By.CLASS_NAME,'hfpxzc')[0]
    choose_first_item_click.click()
    #紀錄需要多點擊一次
    need_second_click=1
except:
    need_second_click=0
    print('不用點到第二層')
print("Finish Searching! " + search)
time.sleep(2.85)
soup = Soup(browser.page_source,"lxml")

# %% [markdown]
# ## 點擊更多評論

# %%
# 原本的 class name 中存在空格："HHrUdb fontTitleSmall rqjGif"，有時會讓程式抓不到
# 所以空格的部分要改成「.」才能成功抓取
if need_second_click==1:
    search_all_name=browser.find_element(By.CLASS_NAME,'DUwDvf.lfPIob').text
    browser.get(url)

    # 輸入欲搜尋的店家名稱
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'searchboxinput.xiQnY')))
    search_input = browser.find_elements(By.CLASS_NAME,'searchboxinput.xiQnY')[0]
    search_input.send_keys(search_all_name)

    # 定位搜尋鍵並點擊
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, 'searchbox-searchbutton')))

    search_click = browser.find_elements(By.ID,'searchbox-searchbutton')[0]

    search_click.click()

#點擊進入更多評論
review_click= browser.find_elements(By.CLASS_NAME,"wNNZR.fontTitleSmall")[2]
actions=ActionChains(browser)
actions.move_to_element(review_click).perform()
review_click.click()

# %% [markdown]
# ## 開啟評論選單

# %%
# 0:撰寫評論 1:搜尋
# 所以空格的部分要改成「.」才能成功抓取
menu_click = browser.find_elements(By.CLASS_NAME,'g88MCb.S9kvJb')[2]

print(menu_click.text)

menu_click.click()

# %% [markdown]
# ## 選擇評論類型

# %%
data_index = 0 # 最相關

category_click = browser.find_elements(By.CLASS_NAME,'fxNQSd')

print(category_click[data_index].text)

category_click[data_index].click()

# %% [markdown]
# ## 選取評論元素和消費者名稱

# %%
# 有時將空格取代的方法會失效，此時改回原始樣態即可
soup = Soup(browser.page_source,"lxml")
all_reviews = soup.find_all(class_ ='jftiEf fontBodyMedium')

# %%
ar=all_reviews[0]
ar

# %%
#
all_text_review=[]
all_title_review=[]
all_title_review.append(ar.find(class_ = "d4r55").text)
all_text_review.append(ar.find(class_ = "wiI7pd").text)
print(all_title_review)
print(all_text_review)

# %% [markdown]
# ## 建立df

# %%
school=pd.DataFrame({"學校名稱":search,"評論者名稱":all_title_review,"評論內容":all_text_review})
school

# %% [markdown]
# ## 小練習
# ### 請嘗試爬取上堂課指定題目 search="北商" 的排序為最新底下的第一則評論者及內容(需先執行下面段落)

# %%
search= "北商"

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
    #紀錄需要多點擊一次
    need_second_click=1
except:
    need_second_click=0
    print('不用點到第二層')
print("Finish Searching! " + search)
time.sleep(2.85)
soup = Soup(browser.page_source,"lxml")

# %%
# 點開更多評論
review_click= browser.find_elements(By.CLASS_NAME,"wNNZR.fontTitleSmall")[2]
actions=ActionChains(browser)
actions.move_to_element(review_click).perform()
review_click.click()

# %%
# 開啟評論選單
menu_click = browser.find_elements(By.CLASS_NAME,'g88MCb.S9kvJb')[2]

print(menu_click.text)

menu_click.click()

# 選擇評論類型
data_index = 1 # 最新

category_click = browser.find_elements(By.CLASS_NAME,'fxNQSd')

print(category_click[data_index].text)

category_click[data_index].click()

# %%
# 選取評論元素和消費者名稱
soup = Soup(browser.page_source,"lxml")
all_reviews = soup.find_all(class_ = 'jftiEf fontBodyMedium')
ar=all_reviews[0] #第一則評論
#
all_text_review=[]
all_title_review=[]
try:
    all_text_review.append(ar.find(class_ = "wiI7pd").text)
except:
    all_text_review.append("沒有評論")

all_title_review.append(ar.find(class_ = "d4r55").text)

# 建立df
school=pd.DataFrame({"學校名稱":search,"評論者名稱":all_title_review,"評論內容":all_text_review})
school



# %%
