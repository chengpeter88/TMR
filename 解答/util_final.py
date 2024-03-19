def move_file(detect_name, folder_name):
    '''
    detect_name:
        
    folder_name:
        
    '''    
    # 抓出為【正常模型】的所有檔案名稱
    import os 
    save = []
    for i in os.listdir():
        if detect_name in i:
            save.append(i)
    
    # make folder
    ff = [i for i in save if not '.' in i ]
    ff = [i for i in ff if  '（' in i ]
    
    
            
    try:
        os.makedirs(folder_name)
        folder_namenew= folder_name
    
    except:
        
        try:
            os.makedirs(folder_name + '（' +str(0)+'）')
            folder_namenew= folder_name + '（' +str(0)+'）'
        except: 
            
            for i in range(0, 10):
                iinn = [j for j in ff if folder_name + '（' +str(i)+'）'  in j]
                if len(iinn) == 0:
                    os.makedirs(folder_name + '（' +str(i)+'）')
                    folder_namenew =folder_name + '（' +str(i)+'）'
                    break
    # move files to that created folder
    import shutil
    save = [i for i in save if '.' in i ]
    for m in save:
        shutil.move(m, folder_namenew)

def google_review(search="中山區影城",scroll_time=1, review_category="最相關"):
    import re
    import time
    import os
    import pandas as pd
    from datetime import datetime
    from bs4 import BeautifulSoup as Soup
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support import expected_conditions as EC
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    browser = webdriver.Chrome(service=ChromeService())
    
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

    i=0
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

    soup = Soup(browser.page_source,"lxml")
    time.sleep(5)
    # 取得網頁元素框架（搜尋結果）
    #WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'section-result')))


    WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'hfpxzc')))
    t = 0
    find = True
    while find == True:
        time.sleep(1)
        pane = browser.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]')
        browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pane)
        time.sleep(1)
        t+=1
        try:
            soup = Soup(browser.page_source,"lxml")
            end = soup.find_all(class_ = "HlvSq")[0].text
            if end == "你已看完所有搜尋結果。":
                find=False
        except:
            print("正在下拉搜尋結果...")
        if t >1000:
            find = False

    store_frame = soup.find_all(class_="hfpxzc")
    # 找所有機構名稱
    store_name = []
    for stores in store_frame:
        new_store = stores.get('aria-label')
        if (new_store != None) :
            store_name.append(new_store)
    print("機構名稱：")
    for sn in store_name:
        print(sn)
    print("一共有"+str(len(store_name))+"家店要爬取!")
    browser.close()
    # key point
    for n in range(len(store_name)):
        # n = 0 # 第幾個機構
        # 抓個別機構資料
        # WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'hfpxzc')))
        # store_click = browser.find_elements_by_class_name('hfpxzc')[9]
        # store_click.click()
        print("正在爬取_"+store_name[n]) 
        browser = webdriver.Chrome(service=ChromeService())
        browser.get(store_frame[n].get("href"))
        browser.set_window_size(782, 831)
        soup = Soup(browser.page_source,"lxml")
        # 網頁元素定位
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
            authority_frame = soup.find_all('a', {'data-item-id':"authority"})
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
            phone_frame = soup.find_all('button', {'data-item-id':re.compile('phone:')})
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
        # 爬取機構星級
        time.sleep(2.85)
        star_section=[]
        try:
            soup = Soup(browser.page_source,"lxml")
            star_section.append(float((soup.find_all(class_="F7nice")[0].text)[:3]))
        except:
            star_section.append("-")
            pass
        #print("機構星級：", star_section)
        # 爬取機構總評論數
        review_num=[]
        try:
            review_num.append(int(soup.find_all(class_="F7nice")[0].text[3:].replace("(","").replace(")","").replace(",","")))
        except:
            review_num.append("-")
            pass
        #print("機構總評論數：", review_num)
        #建立df
        today = datetime.today().strftime("%Y-%m-%d")
        brief=pd.DataFrame({"機構名稱":search,
        "機構種類":school_type,
        "機構地址":addresses,
        "機構網站":authorities,
        "機構電話":phones,
        "機構營業時間":school_open_hours,
        "機構總評論數":review_num,
        "機構星數":star_section,
        "爬取日期":today})
        print("基礎機構資訊爬取完成_"+store_name[n])

        # 進階內容
        # 點開更多評論
        try:
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"wNNZR.fontTitleSmall")))
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
            # 建立df
            customer_review=pd.DataFrame({"機構名稱":search,
            "評論者名稱":all_title_review,
            "評論時間":all_time_review,
            "評論內容":all_text_review,
            "評論星數":all_star_review,
            "評論照片":all_photo_review,
            "爬取日期":today})
            print("進階機構消費者資訊爬取完成_"+store_name[n])
            # 輸出csv
            brief.to_csv("./"+ str(i) +"_"+"機構資訊"+"_"+ store_name[n] + ".csv", encoding = 'UTF-8-sig')
            customer_review.to_csv("./"+ str(i) +"_"+"消費者資訊"+"_"+ store_name[n] + '_'+ str(scroll_time)+ "頁_評論.csv", encoding = 'UTF-8-sig')
            i += 1
            print("輸出完成_"+store_name[n])
            browser.close()
            # 點擊返回店家頁面
            # time.sleep(2.5)
            # print('返回機構介面')
            # WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'VfPpkd-icon-LgbsSe.yHy1rc.eT1oJ.mN1ivc')))
            # soup = Soup(browser.page_source,"lxml")
            # BacktoStore_btn = browser.find_elements_by_class_name('VfPpkd-icon-LgbsSe.yHy1rc.eT1oJ.mN1ivc')[0]
            # BacktoStore_btn.click()
           

            # print("返回搜尋結果")
            # WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'hYBOP.FeXq4d')))
            # BacktoSearch_btn = browser.find_elements_by_class_name('hYBOP.FeXq4d')[0]
            # BacktoSearch_btn.click()
           

            print(store_name[n]+"爬取完成")
        except :
            # brief.to_csv("./基礎機構資訊_"+str(search)+"/"+ str(i) +"_"+ store_name[n] + ".csv", encoding = 'UTF-8-sig')
            # print("返回搜尋結果")
            # WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'hYBOP.FeXq4d')))
            # BacktoSearch_btn = browser.find_elements_by_class_name('hYBOP.FeXq4d')[0]
            # BacktoSearch_btn.click()
            browser.close()
            print(store_name[n]+"沒有進階機構消費者資訊")
    move_file(detect_name= '機構資訊', folder_name= '基礎機構資訊_'+search)
    move_file(detect_name= '消費者資訊', folder_name= '進階機構消費者資訊_'+search)

    return print("爬取完畢")

