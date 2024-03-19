# %% [markdown]
# # 07_機構資料爬取－模組實戰

# %% [markdown]
# ## 以過去上課案例"臺師大"來查看結果

# %%
def google_review_store(search="臺師大"):
    import re
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
    time.sleep(2.85)
    soup = Soup(browser.page_source,"lxml")
    #定義接下來要抓取的清單
    school_type=[]
    addresses=[]
    authorities=[]
    phones=[]
    school_open_hours=[]
    #爬取機構種類
    try:
        school_category2 = soup.find_all('button',{'class':"DkEaL"})[0].text

        if len(school_category2)!=0:
            school_type.append(school_category2)
        else:
            school_type.append('')
    except:
        school_type.append("-")
        pass
    #print("機構種類:", school_type)
    #爬取機構地址
    try:
        address_frame = soup.find_all('button', {'data-item-id':"address"})

        addresses.append(address_frame[0].get('aria-label').strip().strip('地址: '))
    except:
        addresses.append("-")
        pass
    #print("機構地址：", addresses)
    #爬取機構網站
    try:
        authority_frame = soup.find_all('button', {'data-item-id':"authority"})
        if authority_frame == []:
            authorities.append([])
            #print('empty')
        else:
            authorities.append(authority_frame[0].get('aria-label').strip().strip("網站: "))
    except:
        authorities.append("-")
        pass
    #print("機構網站：",authorities)
    #爬取機構電話
    try:
        phone_frame = soup.find_all('button', {'data-tooltip':"複製電話號碼"})
        if phone_frame == []:
            phones.append([])
            #print('您的電話號碼為空號')
        else:
            phone_num = phone_frame[0].get('aria-label').strip().strip('電話號碼: ')
            
            phones.append(phone_num)
    except:
        phones.append("-")
        pass
    #print("機構電話號碼：", phones)
    #爬取機構營業時間
    try:
        open_hour_frame=soup.find_all(class_="t39EBf GUrTXd")

        if open_hour_frame == []:
            open_hours_sorted = []
        else:
            open_hours = open_hour_frame[0].get('aria-label')
            open_hours = open_hours.split('.')[0]
            open_hours_list = open_hours.split('; ')
            weekday = ['星期日','星期一','星期二','星期三','星期四','星期五','星期六']
            open_hours_sorted = []
            for oh in range(len(open_hours_list)):
                for op in open_hours_list:
                    if weekday[oh] in op:
                        open_hours_sorted.append(op)

        school_open_hours.append(open_hours_sorted)
    except:
        school_open_hours.append("-")
        pass
    #print("機構營業時間：", school_open_hours)
    #建立data frame
    school=pd.DataFrame({"機構名稱":search,
    "種類":school_type,
    "地址":addresses,
    "網站":authorities,
    "電話號碼":phones,
    "營業時間":school_open_hours})
    return school

# %%
from util import google_review_store

# %%
school=google_review_store(search="臺師大")

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
search="成大"
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
clear_input = browser.find_elements(By.CLASS_NAME,'searchboxinput.xiQnY')[0]
clear_input.click()

# %% [markdown]
# ## 小練習
# ### 試著使用模組爬取上課指定題目search="成大"

# %%
school=google_review_store(search="成大")

# %%
school


