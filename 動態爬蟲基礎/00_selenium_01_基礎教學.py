
# # Selenium動態網頁爬蟲
# - 定位網頁元素
# - Selenium函式的使用規則
# - Selenium函式八大選擇器的使用方法

# %%
# pip install selenium==4.1.5

#%%
# 導入套件
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from show import showimg


# ## 定位網頁元素


# %%
# 透過Browser Driver 開啟 Chrome 

driver = webdriver.Chrome(service=ChromeService())


# ### 前往 https://www.google.com.tw 網站

# %%
# 前往特定網址
default_url = 'https://www.google.com.tw'
driver.get(default_url)

# %%
# 獲取目前網頁url
driver.current_url


# ## 利用 Selenium 輸入與點擊
showimg('https://imgur.com/WRLEzpi.png')
showimg('https://imgur.com/Bd4Ybvc.png')
showimg('https://imgur.com/WJ2ojIX.png')

# %%
element = driver.find_element(By.CLASS_NAME,"gLFyf") 

# %%
element.send_keys("Selenium Python")

element.clear()

# %%
showimg('https://imgur.com/lxEUYti.png')

driver.find_element(By.CLASS_NAME,"gNO89b").click() 



# %%
showimg('https://imgur.com/XYwA20O.png')

driver.back()

# %%

# ## 函式八大選擇器的使用方法
showimg('')

showimg('https://imgur.com/e3GpjWX.png')

showimg('https://imgur.com/jUZYYSd.png')


showimg('https://imgur.com/IqLXzjQ.png')


showimg('https://imgur.com/Qy9YMcg.png')

showimg('https://imgur.com/fLBvwCo.png')

showimg('https://imgur.com/nmqObvo.png')

# %%
# 抓取「gmail」的按鈕
# 其classname為gb_e gb_f的網頁元素有以下方法
# 注意：字串內有空格要改為"."，例如："gb_e gb_f"要轉成"gb_e.gb_f"
# 僅抓取第一個元素
driver.find_element(By.CLASS_NAME, "gb_H") # 抓取第一個
driver.find_elements(By.CLASS_NAME, "gb_H")[0].click()
driver.back()

# ### 問題：抓取「登入」按鈕
# hint：其classname為gb_1 gb_2 gb_6d gb_6c的網頁元素，並執行點擊（click）
# 若發現要素多於1者，要用[數字]的方法來做選擇哦  
driver.find_elements(By.CLASS_NAME,"gb_Ba gb_md gb_Od gb_me")[0].click()
driver.find_elements(By.CLASS_NAME, "gb_Ba.gb_md.gb_Od.gb_me")[0].click()
driver.back()
# %%


# %%

showimg('https://imgur.com/u6oWxzi.png')
# 
showimg('https://imgur.com/6ImcvJp.png')
# 
showimg('https://imgur.com/o5L9XnV.png')

# %%
# 使用NAME查找網頁元素
driver.find_element(By.NAME, "csi")

# selenium 4.2.0 (含)以下可使用 
driver.find_element_by_name("csi")


# ### 問題：抓取所有name為btnI的網頁元素
driver.find_element(By.NAME, "btnI")

# selenium 4.2.0 (含)以下可使用 
driver.find_element_by_name("btnI")
# %%


# %%

showimg('https://imgur.com/LxkZghP.png')
# 
showimg('https://imgur.com/MvaKpU3.png')
# 
showimg('https://imgur.com/KIEXX9j.png')

# %%
# 使用LINK_TEXT查找網頁元素
driver.find_element(By.LINK_TEXT, "關於 Google").click()
driver.back()

# selenium 4.2.0 (含)以下可使用
driver.find_element_by_link_text("關於 Google")


# ### 問題：使用LINK_TEXT查找"Google 商店"網頁元素，並點擊
driver.find_elements(By.LINK_TEXT, "Google 商店")[0].click()
driver.back()
# %%
showimg('https://imgur.com/PQbdtfq.png')

driver.find_elements(By.PARTIAL_LINK_TEXT, "Google")[1].text


showimg('https://imgur.com/ggY6ZjX.png')
# 
showimg('https://imgur.com/5RxqI4c.png')
# 
showimg('https://imgur.com/LytnGIu.png')

# %%
# 使用TAG_NAME查找網頁元素
# tag即是HTML網頁標籤，是網頁檢視器裡紫色的字元部分，將網頁結構劃歸為各個階層，如：head、body、style、div等。
driver.find_element(By.TAG_NAME, "head")

# selenium 4.2.0 (含)以下可使用
driver.find_element_by_tag_name("head")


# %%

showimg('https://imgur.com/6tCaLUQ.png')
# 
showimg('https://imgur.com/HI645rx.png')
# 
showimg('https://imgur.com/bQZL1Z7.png')
# 
showimg('https://imgur.com/aqGJ7Vo.png')
# 

# %%
# /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input
# 使用XPATH查找網頁元素，方法為在想要獲取的元素上點擊右鍵，點擊Copy full xpath
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/a[1]')

# selenium 4.2.0 (含)以下可使用
driver.find_element_by_xpath('/html/body/div[1]/div[1]/a[1]')


# 用bs4抓取網頁元素，取相關內容
from bs4 import BeautifulSoup as Soup
soup2 = Soup(driver.page_source, "lxml")
for i in soup2.find_all('a', 'MV3Tnb'):
    print(i.text)

# ### 用Xpath抓取所有Gmail的網頁元素，並執行字詞抓取與點擊（click）
driver.find_elements(By.XPATH, '//*[@id="gb"]/div/div[1]/div/div[1]/a')[0].text

driver.close()


# %%
