import time
import pandas as pd  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# 啟動瀏覽器工具的選項          
driver = webdriver.Chrome('chromedriver')
url = 'https://www.google.com.tw/maps?hl=zh-TW&tab=rl&authuser=0'  
driver.get(url)  # 開啟瀏覽器並連到該網頁   

# 搜尋地點
#NOTE -  方法一 
search = '台師大'
# wait停留在這個 標籤下等一下 
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'searchboxinput.xiQnY')))
search_input = driver.find_element(By.CLASS_NAME, 'searchboxinput.xiQnY')   
search_input.send_keys(search)
search_input.send_keys(Keys.ENTER)                                                       


# #NOTE -  方法二   
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'searchboxinput.xiQnY')))
search_input = driver.find_element(By.CLASS_NAME, 'searchboxinput.xiQnY')
search_input.send_keys(search)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'searchbox-searchbutton')))
search_click = driver.find_element(By.ID, 'searchbox-searchbutton')
search_click.click()



#NOTE -  方法三
try:
    location = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'searchboxinput.xiQnY')))
    location.send_keys(search)
    location.send_keys(Keys.ENTER)
    main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                    By.ID, 'searchbox-searchbutton')))
    main.click()
except:
    print('error')


### 架設要抓的東西不只一層停止

try:
    first_item=WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME,'hfpxzc')))
    # first_item_click=driver.find_elements(By.CLASS_NAME,'hfpxzc')[0]
    first_item.click()
    #紀錄需要多點擊一次
    need_second_click=1
except:
    need_second_click=0
    print('不用點到第二層')

print("Finish Searching! " + search)    



# 爬網站資料    
Elements = WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'rogA2c')))
address = Elements[0].text
website = Elements[1].text
phone = Elements[2].text
print(address, website, phone)
school = pd.DataFrame({'學校名稱': [search], '地址': [address], '網站': [website], '電話': [phone]})
print(school)
driver.quit()  # 關閉瀏覽器

### function 限制第一層
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