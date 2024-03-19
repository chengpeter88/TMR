
def google_review_customer(search="臺大",scroll_time=4, review_category = "最新"):
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
    if review_category =="最相關":
        data_index = 0
    elif review_category == "最新":
        data_index = 1
    elif  review_category == "評分最高":
        data_index = 2
    elif review_category == "評分最低":
        data_index = 3
    else:
        print("無此類別")
    # 開啟chromedriver
    url = 'https://www.google.com.tw/maps?hl=zh-TW&tab=rl&authuser=0'  
    browser.get(url)
    browser.set_window_size(782, 831)
        
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





    # 爬取機構星級
    time.sleep(2.85)
    soup = Soup(browser.page_source,"lxml")
    star_section=[]
    star_section.append(float((soup.find_all(class_="F7nice")[0].text)[:3]))
    print("學校星級：", star_section)

    # 爬取機構總評論數
    review_num = []
    reveiw_sum=soup.find_all(class_="F7nice")[0].text[3:].replace("(","").replace(")","").replace(",","")
    review_num.append(reveiw_sum)
    print("學校總評論數：", review_num)

   # 空格的部分要改成「.」才能成功抓取
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
    if need_second_click==1:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"wNNZR.fontTitleSmall")))
        review_click= browser.find_elements(By.CLASS_NAME,"wNNZR.fontTitleSmall")[1]
    else:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"wNNZR.fontTitleSmall")))
        review_click= browser.find_elements(By.CLASS_NAME,"wNNZR.fontTitleSmall")[2]
    actions=ActionChains(browser)
    actions.move_to_element(review_click).perform()
    review_click.click()

    # 開啟評論選單
    time.sleep(2.85)
    menu_click = browser.find_elements(By.CLASS_NAME,'g88MCb.S9kvJb')[2]
    print(menu_click.text)
    menu_click.click()

    # 選擇相關評論
    category_click = browser.find_elements(By.CLASS_NAME,'fxNQSd')
    print(category_click[data_index].text)
    category_click[data_index].click()

    # 下拉評論
    for st in range(scroll_time):
        time.sleep(2)
        pane = browser.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]')
        browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pane)
        print(st+1,'scroll')
        time.sleep(2)
    #　爬取所有評論
    soup = Soup(browser.page_source,"lxml")

    all_reviews = soup.find_all(class_ = 'jftiEf fontBodyMedium')
    
    all_text_review=[]
    all_title_review=[]
    all_time_review=[]
    all_star_review=[]
    all_photo_review=[]
    #　點開所有照片
    all_photo = browser.find_elements(By.CLASS_NAME,'Tya61d')
    for ap in all_photo:
        ap.click()

    for ar in all_reviews:
        try:
            all_text_review.append(ar.find(class_ = "wiI7pd").text)
        except:
            all_text_review.append("沒有評論")
        all_title_review.append(ar.find(class_ = "d4r55").text)
        all_time_review.append(ar.find(class_="rsqaWe").text)
        all_star_review.append(int(ar.find(class_ = "kvMYJc").get('aria-label').strip().strip(" 顆星")))
        #
        photos = ar.find_all(class_ = "Tya61d")
        photo_urls=[]
        for ph in photos:
            photo_urls.append(ph.get('style').strip('"background-image: url(').split('")')[0])
        all_photo_review.append(photo_urls)
    # 建立Df
    today = datetime.today().strftime("%Y-%m-%d")
    customer_review=pd.DataFrame({"機構名稱":search,
    "評論者名稱":all_title_review,
    "評論時間":all_time_review,
    "評論內容":all_text_review,
    "評論星數":all_star_review,
    "評論照片":all_photo_review,
    "爬取日期":today})
    # 機構相關訊息
    section= pd.DataFrame({"機構名稱":search,
    "機構總評論數":review_num,
    "機構星數":star_section,
    "爬取日期":today})
    browser.close()
    return customer_review,section


