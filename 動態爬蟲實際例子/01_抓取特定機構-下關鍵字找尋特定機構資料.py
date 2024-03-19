# %% [markdown]
# # 01_抓取特定機構-下關鍵字找尋特定機構資料

# %% [markdown]
# %% 安裝套件

#! pip install selenium==4.3.0


# ## 引入套件

# %%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
browser = webdriver.Chrome(service=ChromeService())
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC



# %% [markdown]
# ## 搜尋內容
# ### 先設定等等要爬取的機構名稱

# %%
search= "臺灣師範大學"

# %% [markdown]
# ## 透過browser開啟Google Maps

# %% [markdown]
# ### 若同學在這邊出現error，可以分別檢查兩件事情
# #### 1. chromedriver版本是否與瀏覽器相同
# #### 2. chromedriver是否與此程式碼位於相同工作目錄

# %%
url = 'https://www.google.com.tw/maps?hl=zh-TW&tab=rl&authuser=0'  

# %% [markdown]
# ## 前往該網址

# %%
browser.get(url)

# %% [markdown]
# ## 定位網頁元素後，填入搜尋內容

# %%
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'searchboxinput.xiQnY')))

search_input = browser.find_elements(By.CLASS_NAME,'searchboxinput.xiQnY')[0]

search_input.send_keys(search)

# %% [markdown]
# ## 同樣定位搜尋鍵並點擊，便可以看到臺師大的頁面囉

# %%
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'mL3xi')))

search_click = browser.find_elements(By.CLASS_NAME,'mL3xi')[0]

search_click.click()

print("Finish Searching! " + search)

# browser.close()
# %% [markdown]
# ## 小練習
# ### 請嘗試搜尋 search="成大"，並進入該介面

# %%
search= "???"

# 開啟chromedriver
url = 'https://www.google.com.tw/maps?hl=zh-TW&tab=rl&authuser=0'  
browser = webdriver.Chrome(service=ChromeService())
browser.get(???)

# 輸入欲搜尋的店家名稱
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'searchboxinput.xiQnY')))
search_input = browser.find_elements(By.CLASS_NAME,'searchboxinput.xiQnY')[0]
search_input.send_keys(???)

# 定位搜尋鍵並點擊
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'mL3xi')))
search_click = browser.find_elements(By.CLASS_NAME,'mL3xi')[0]
??? #hint: 點擊搜尋鍵

print("Finish Searching! " + search)

browser.close()
