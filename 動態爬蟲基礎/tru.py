from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import time 
from selenium import webdriver  
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
url="https://www.techwithtim.net/"
driver.get(url)
# link= driver.find_element_by_class_name("tag__TagContainer-sc-3f52y0-0 fPNUsx")
# element = driver.find_element(By.CSS_SELECTOR, '.tag__TagContainer-sc-3f52y0-0.fPNUsx')
# element.click()
time.sleep(1)

# 使用 CSS 選擇器找到元素
element = driver.find_element(By.CSS_SELECTOR, '.content__CardContentContainer-sc-1nrnigk-0.iSmWKS')

# 點擊元素
element.click()



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
 
 
options = Options()
options.add_argument("--disable-notifications")
 
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get("https://www.facebook.com/")


######################
from selenium import webdriver
chromedirver_path = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://shopping.pchome.com.tw/")
driver.find_element_by_link_text("3C").click()
driver.find_element(By.CSS_SELECTOR, 'c-menuList__link gtmClick gtmClickV2').click()
<a href="https://24h.pchome.com.tw/region/DHAA" class="c-menuList__link gtmClick gtmClickV2">筆 記 電 腦</a>from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('http://www.someurl.com')

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'myId'))
    )
finally:
    driver.quit()


from selenium import webdriver
chromedriver = '/usr/local/bin/chromedriver' #要用變數指定chromedriver的放置路徑
browser=webdriver.Chrome(chromedriver)
browser.get("https://myvbalearning.wordpress.com/2017/10/15/mac%E5%AE%89%E8%A3%9Dchromedriver/")
driver.find_element_by_link_text("HOME").click()
