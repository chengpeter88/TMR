# %% [markdown]
# # 15_消費者資料爬取（8） - 抓取評論者照片，基礎起手式

# %% [markdown]
# ## 引入套件

# %%
import time
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome(service=ChromeService())
from bs4 import BeautifulSoup as Soup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

# %% [markdown]
# ## 首先，我們先執行到顯示"臺師大"最相關留言的地方

# %%
search= "台大"

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
time.sleep(2)
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
    time.sleep(2)

#點擊進入更多評論
review_click= browser.find_elements(By.CLASS_NAME,"wNNZR.fontTitleSmall")[1]
actions=ActionChains(browser)
actions.move_to_element(review_click).perform()
review_click.click()

# 開啟評論選單
time.sleep(2.85)
menu_click = browser.find_elements(By.CLASS_NAME,'g88MCb.S9kvJb')[2]
print(menu_click.text)
menu_click.click()

# 選擇相關評論
data_index = 0 # 相關
category_click = browser.find_elements(By.CLASS_NAME,'fxNQSd')
print(category_click[data_index].text)
category_click[data_index].click()

# %% [markdown]
# ## 假設這邊選擇下拉兩次

# %%
#設定下拉幾次
scroll_time = 2
for st in range(scroll_time):
    time.sleep(2)
    pane = browser.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]')
    browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pane)
    print(st+1,'scroll')
    time.sleep(2)

# %% [markdown]
# ## 爬取照片

# %%
soup = Soup(browser.page_source,"lxml")

all_reviews = soup.find_all(class_ = 'jftiEf fontBodyMedium')

# %%
#尋找有照片內容的評論
ar=all_reviews[0]

# %%
all_photo_review=[]

photos = ar.find_all(class_ = "Tya61d")

# %%
photo_urls = []
for ph in photos:
    photo_urls.append(ph.get('style'))
    
all_photo_review.append(photo_urls)

# %%
all_photo_review

# %% [markdown]
# ## 刪除空白及文字

# %%
all_photo_review[0][0].strip('"background-image: url(').split('")')[0]

# %% [markdown]
# ## 利用for迴圈爬取已建立的評論內容

# %%
all_text_review=[]
all_title_review=[]
all_time_review=[]
all_star_review=[]
all_photo_review=[]
for ar in all_reviews:
    all_title_review.append(ar.find(class_ = "d4r55").text)
    all_text_review.append(ar.find(class_ = "wiI7pd").text)
    all_time_review.append(ar.find(class_="rsqaWe").text)
    all_star_review.append(str(ar.find(class_ = "kvMYJc").get('aria-label').strip().strip("顆星").strip()))
    #
    photos = ar.find_all(class_ = "Tya61d")
    photo_urls=[]
    for ph in photos:
        photo_urls.append(ph.get('style').strip('"background-image: url(').split('")')[0])
    all_photo_review.append(photo_urls)

# %% [markdown]
# ## 建立dataframe

# %%
school=pd.DataFrame({"學校名稱":search,"評論者名稱":all_title_review,"評論時間":all_time_review,"評論內容":all_text_review,"評論星數":all_star_review,"評論照片":all_photo_review})
school

# %%
school["評論照片"][2]

#%%
browser.close()

# %% [markdown]
# # 咦?怎麼好像有些照片沒有爬取下來

# %% [markdown]
# ## 小練習
# ### 請嘗試爬取上堂課指定題目 search="北商" 下拉4次 scroll=4 的所有評論以及評論時間(需先執行下面段落)

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
    time.sleep(2)

#點擊進入更多評論
review_click= browser.find_elements(By.CLASS_NAME,"wNNZR.fontTitleSmall")[2]
actions=ActionChains(browser)
actions.move_to_element(review_click).perform()
review_click.click()

# 開啟評論選單
time.sleep(2.85)
menu_click = browser.find_elements(By.CLASS_NAME,'g88MCb.S9kvJb')[2]
print(menu_click.text)
menu_click.click()

# 選擇最新評論
data_index = 1 # 最新
category_click = browser.find_elements(By.CLASS_NAME,'fxNQSd')
print(category_click[data_index].text)
category_click[data_index].click()

# %%
#下拉評論
scroll_time=4
for st in range(scroll_time):
    time.sleep(2)
    pane = browser.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]')
    browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pane)
    print(st+1,'scroll')
    time.sleep(2)

# %%
#爬取所有評論
soup = Soup(browser.page_source,"lxml")

all_reviews = soup.find_all(class_ = 'jftiEf fontBodyMedium')

all_text_review=[]
all_title_review=[]
all_time_review=[]
all_star_review=[]
all_photo_review=[]
for ar in all_reviews:
    try:
        all_text_review.append(ar.find(class_ = "wiI7pd").text)
    except:
        all_text_review.append("沒有評論")
    all_title_review.append(ar.find(class_ = "d4r55").text)
    all_time_review.append(ar.find(class_="rsqaWe").text)
    all_star_review.append(str(ar.find(class_ = "kvMYJc").get('aria-label').strip().strip("顆星").strip()))
    #
    photos = ar.find_all(class_ = "???")
    photo_urls=[]
    for ph in photos:
        photo_urls.append(ph.???('???').???('"background-image: url(').???('")')[0])
    all_photo_review.append(photo_urls)

school=pd.DataFrame({"學校名稱":search,"評論者名稱":all_title_review,"評論時間":all_time_review,"評論內容":all_text_review,"評論星數":all_star_review,"評論照片":all_photo_review})
school.head()

browser.close()
