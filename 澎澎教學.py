

### 澎澎爬蟲 ch1
import urllib.request   as request
src = "https://www.ntu.edu.tw/" 
with request.urlopen(src) as response:
    data = response.read().decode("utf-8")
    # 台灣大學網站原始碼
print(data)

url = 'https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire'
import json
with request.urlopen(url) as response:
    data = json.load(response)
    print(data)

clist = data["result"]["results"]   
print(clist)
with open('data.txt','w',encoding='utf-8') as file:
    for company in clist:
        file.write(company["公司名稱"]+'\n')
for company in clist:
    print(company["公司名稱"])


### 澎澎爬蟲 ch2
### <html>  
### <head>
### <title>我的網頁</title>
### </head>
### <body>
### <div class="content">
##    <span> 階層節構<\span>
##    <\div>
### <\body>
### <\html>    
### <a href="http://www.ntu.edu.tw">台灣大學</a>
    
#內建模組 urllib.request 用來處理網路連線 
#但連線看來不像是正常使用者
import urllib.request as req
with req.urlopen("https://www.ptt.cc/bbs/movie/index.html") as response:
    data = response.read().decode("utf-8")

# 網路連線request.header    user-agent
    
# 進入ptt電影版 需要夠像是正常使用者    

#目前讀取的資料是ptt電影版的原始碼 不容易解讀
import urllib.request as urllib_req
url = "https://www.ptt.cc/bbs/movie/index.html"
userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
#  建立一個Request物件，附加Request Headers的資訊
headers = {'User-Agent': userAgent}
request = urllib_req.Request(url, headers = headers)
with urllib_req.urlopen(request) as response:
    data = response.read().decode("utf-8")
print(data)

import bs4 
root = bs4.BeautifulSoup(data, "html.parser") # 讓beautifulsoup協助解析HTML格式文件
print(root.title.string) # 取得HTML標題內容
print(root.title) # 取得HTML標題標籤
#####NOTE -  只有一個title標籤
titles=root.find("div", class_="title") # 尋找class="title"的div標籤
print(titles) # 全部
print(titles.a) # 抓取標題 a 
print(titles.a.string) # 取得標題文字 a裡面文字

## <div class = 'title'>
## <a href = "link" >name</a> 

alltitles=root.find_all("div", class_="title") # 尋找所有class="title"的div標籤
for title in alltitles:
    if title.a != None: # 如果標題包含a標籤(沒有被刪除), 印出來 
        print(title.a.string)

### 澎澎爬蟲 ch3 cookies    
import urllib.request as urllib_req
url = "https://www.ptt.cc/bbs/Gossiping/index.html"
userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
#  建立一個Request物件，附加Request Headers的資訊
headers = {
    'User-Agent': userAgent,
    'Cookie': 'over18=1'
}
request = urllib_req.Request(url, headers = headers, )
with urllib_req.urlopen(request) as response:
    data = response.read().decode("utf-8")


import bs4 
root = bs4.BeautifulSoup(data, "html.parser") # 讓beautifulsoup協助解析HTML格式文件
## <div class = 'title'>
## <a href = "link" >name</a> 
alltitles=root.find_all("div", class_="title") # 尋找所有class="title"的div標籤
for title in alltitles:
    if title.a != None: # 如果標題包含a標籤(沒有被刪除), 印出來 
        print(title.a.string)

# <a class="btn wide" href="/bbs/Gossiping/index39139.html">‹ 上頁</a>
nextlink=root.find('a',string='‹ 上頁')['href']



#### 連續爬取多頁
import urllib.request as urllib_req
import bs4
import bs4 
def getData(url):
    userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
#  建立一個Request物件，附加Request Headers的資訊
    headers = {
    'User-Agent': userAgent,
    'Cookie': 'over18=1'
    }
    request = urllib_req.Request(url, headers = headers, )
    with urllib_req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    root = bs4.BeautifulSoup(data, "html.parser") # 讓beautifulsoup協助解析HTML格式文件
    ## <div class = 'title'>
    ## <a href = "link" >name</a> 
    alltitles=root.find_all("div", class_="title") # 尋找所有class="title"的div標籤
    for title in alltitles:
        if title.a != None: # 如果標題包含a標籤(沒有被刪除), 印出來 
            print(title.a.string)
    
    nextlink=root.find('a',string='‹ 上頁')['href']
    return nextlink
#pageurl='https://www.ppt.cc'+getData(pageurl)
# print(pageurl)
##主要code 多個頁面
pageurl="https://www.ptt.cc/bbs/Gossiping/index.html"
count =0
#抓五頁
while count<5:
    pageurl='https://www.ptt.cc'+getData(pageurl)
    count+=1



##SECTION -  澎澎爬蟲 ch4   meduim
###  AJAX  -  Asynchronous JavaScript and XML 網頁會兩段式呈現



## 澎澎爬蟲 ch5  -  selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
Options.chrome_excutbale_path = '/usr/bin/chromewebdriver'
driver=webdriver.Chrome(chrome_options=chrome_options)
driver.maximize_window()
driver.get("https://www.google.com")    
driver.save_screenshot('test.png')
driver.get("https://www.ntu.edu.tw")   
driver.save_screenshot('ntu.png')
driver.close()




###  
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
chrome_options = Options()
Options.chrome_excutbale_path = '/usr/bin/chromewebdriver'
driver=webdriver.Chrome(chrome_options=chrome_options)

url = 'https://www.ptt.cc/bbs/Stock/index.html'
driver.get(url)
time.sleep(1)
# print(driver.page_source)
count = 0
while count < 5:
    tag=driver.find_elements(By.CLASS_NAME,"title")
    for t in tag:
        print(t.text)
    link=driver.find_element(By.LINK_TEXT,"‹ 上頁")
    link.click()
    time.sleep(1)
    count += 1
# tag=driver.find_elements(By.CLASS_NAME,"title")
# for t in tag:
#     print(t.text)

# link=driver.find_element(By.LINK_TEXT,"‹ 上頁")
# link.click()

# tag=driver.find_elements(By.CLASS_NAME,"title")
# for t in tag:
#     print(t.text)

driver.close()
Keys.PAGE_DOWN

### 澎澎爬蟲 捲動頁面

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd 
chrome_options = Options()
Options.chrome_excutbale_path = '/usr/bin/chromewebdriver'
driver=webdriver.Chrome(chrome_options=chrome_options)

url = 'https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0'
driver.get(url)
time.sleep(1)
#捲動頁面
work_title = []
for i in range(10):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(1)
titletag=driver.find_elements(By.CLASS_NAME,"base-card__full-link")
for t in titletag:
    print(t.text)
    work_title.append(t.text)
    # print(t.get_attribute('href'))
    # t.get_attribute()
    print('')
driver.close()  

df = pd.DataFrame(work_title, columns=['title'])
# <h3 class="base-search-card__title">
            
#  Experience Concierge for Magical Company- F U L L Y R E M O T E
      
# </h3>













### selenium  -  自動化測試工具 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
Options.chrome_excutbale_path = '/usr/bin/google-chrome'
driver=webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.google.com")    
print(driver.title)

search = '國立台灣大學'
driver= webdriver.Chrome('Chromedriver')
driver.get('https://www.google.com/maps')
location = driver.find_element_by_id('searchboxinput')
location.send_keys(search)
#location.send_keys(Keys.RETURN)
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'searchbox-searchbutton'))
    )
    main.click()
except:
    print('error')
### 我使用find_element 只會丟出一個element 最先出現的
###  關查到電話也是用這格 可以用find_elements 找找看對應     
address_element = driver.find_element(
    By.CLASS_NAME, 'rogA2c')
address = address_element.text
print(address)
import pandas as pd
school = pd.DataFrame({'學校名稱': [search], '地址': [address]})
school

website_element=driver.find_elements(
    By.CLASS_NAME, 'rogA2c')[1]
website = website_element.text
print(website)
phone_element=driver.find_elements(
    By.CLASS_NAME, 'rogA2c')[2]
phone = phone_element.text
print(phone)
school = pd.DataFrame({'學校名稱': [search], '地址': [address], '網站': [website], '電話': [phone]})
school




######
def get_info(search):
    import pandas as pd
    driver= webdriver.Chrome('Chromedriver')
    driver.get('https://www.google.com/maps')
    location = driver.find_element_by_id('searchboxinput')
    location.send_keys(search)
    try:
        main = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, 'searchbox-searchbutton'))
        )
        main.click()
        Elements = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'rogA2c')))
        address = Elements[0].text
        website = Elements[1].text
        phone = Elements[2].text
        

    except:
        print('error')

    school = pd.DataFrame({'學校名稱': [search], '地址': [address], '網站': [website], '電話': [phone]})
    return school

get_info('國立台灣大學')






from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.someurl.com")

try:
    # 等待元素出現
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "rogA2c"))
    )
    address = element.text
    print(address)
finally:
    driver.quit()

    driver= webdriver.Chrome('Chromedriver')
    driver.get('https://www.google.com/maps')
    location = driver.find_element_by_id('searchboxinput')
    location.send_keys(search)
    try:
        main = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, 'searchbox-searchbutton'))
        )
        main.click()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def get_info(search):
    import pandas as pd
    driver = webdriver.Chrome('Chromedriver')
    driver.get('https://www.google.com/maps')
    location = driver.find_element_by_id('searchboxinput')
    location.send_keys(search)
    try:
        main = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, 'searchbox-searchbutton'))
        )
        main.click()
        
        # 執行下滑到頁面底部的動作
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # 找到需要點擊的元素
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'OyjIsf'))
        )
        
        # 創建ActionChains物件
        actions = ActionChains(driver)
        
        # 執行點擊動作
        actions.move_to_element(element).click().perform()
        
        Elements = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'rogA2c'))
        )
        
        address = Elements[0].text
        website = Elements[1].text
        phone = Elements[2].text
        
    except:
        print('error')

    school = pd.DataFrame({'學校名稱': [search], '地址': [address], '網站': [website], '電話': [phone]})

    return school

get_info('國立台灣大學')


import pandas as pd
import time
search = '國立台灣大學'
driver= webdriver.Chrome('Chromedriver')
driver.get('https://www.google.com/maps')
location = driver.find_element_by_id('searchboxinput')
location.send_keys(search)
try:
    main = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, 'searchbox-searchbutton'))
        )
    main.click()
    move = driver.find_element("tag name", "body")
    time.sleep(3)

    move.send_keys(Keys.PAGE_DOWN) # 往下捲動一頁
    time.sleep(3)
except:
    print('error')


from selenium.webdriver.chrome.service import Service
# 設定 WebDriver 服務和選項

driver= webdriver.Chrome('Chromedriver')


url = "https://new.ntpu.edu.tw"
driver.get(url)
time.sleep(5)
driver.find_element('xpath', "//a[contains(text(),'訪客')]").click() 
#visit = driver.find_element("link text","訪客") # 尋找第一個含有 xx 內容的<a>元素
#visit.click()
time.sleep(3)
school_map = driver.find_element("xpath","//body/app-root[1]/div[1]/app-university[1]/main[1]/app-simple[1]/app-section[1]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[2]/a[1]/div[1]")
school_map.click()
#/html[1]/body[1]/app-root[1]/div[1]/app-university[1]/main[1]/app-simple[1]/app-section[1]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[1]/a[1]/div[1]/span[1]


