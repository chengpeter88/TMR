import requests, bs4
import urllib.request
url= 'https://www.ptt.cc/bbs/Gossiping/index.html'
headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 '}
cookies = {'over18':'1'}    
htmlfile = requests.get(url, headers = headers, cookies = cookies) 

if htmlfile.status_code == 200:
    print('成功')
    print("網頁內容:\n",htmlfile.text)    
else:    
    print('失敗')
    print("失敗原因:\n",htmlfile.raise_for_status())

#  ptt 八卦版實際爬蟲演練
import requests, bs4
url =  'https://www.ptt.cc/bbs/Gossiping/index.html'
headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'}
cookies = {'over18':'1'}    
htmlfile = requests.get(url, headers = headers, cookies = cookies)
objsoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')  

articles = objsoup.find_all('div', class_='r-ent')  
# 尋找文章區塊
num = 0 
for article in articles:
    num += 1
    print('第', num, '篇文章')
    title = article.find('div', 'title').text.strip()
    print('標題:', title)
    try:
        url = 'https://www.ptt.cc' + article.find('div', 'title').a['href']
    except:
        url = None
    print('網址:', url)
    date = article.find('div', 'date').text
    print('日期:', date)
    author = article.find('div', 'author').text
    print('作者:', author)
    print()


number = 0
for article in articles:
    title = article.find('a')  
    # 超聯連結下的文字
    author = article.find('div', class_='author')  
    date = article.find('div', class_='date')  

    if title == None:
        continue
    else:
        number = number + 1 
        print("文章編號:", number)  
        print("文章標題:", title.text)
        print("作者:", author.text)
        print("日期:", date.text)
        print("="*100)
#######!SECTION
import requests, bs4
url1 = 'https://www.ptt.cc'
url2 = "/bbs/Gossiping/index.html"


headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'}
cookies = {'over18':'1'}    
htmlfile = requests.get(url1+url2, headers = headers, cookies = cookies)
objsoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')  

articles = objsoup.find_all('div', class_='r-ent')  
# 尋找文章區塊

number = 0
for article in articles:
    title = article.find('a')  
    # 超聯連結下的文字
    author = article.find('div', class_='author')  
    date = article.find('div', class_='date')  

    if title == None:
        continue
    else:
        number = number + 1 
        print("文章編號:", number)  
        print("文章標題:", title.text)
        print("作者:", author.text)
        print("日期:", date.text)
        print("="*100)

before = objsoup.find_all('a', class_='btn wide')   
url2 = before[1].get('href')  
print("上頁網址",url1+url2)


##!SECTION
import requests, bs4

page = int(input("請輸入要爬取的頁數:"))
url1 = 'https://www.ptt.cc' 
url2 = "/bbs/Gossiping/index.html"

counter = 0 
number = 0  

while counter < page:
    headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'}   
    cookies = {'over18':'1'}
    htmlfile = requests.get(url1+url2, headers = headers, cookies = cookies)
    objsoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')
    articles = objsoup.find_all('div', class_='r-ent')
    for article in articles:
        title = article.find('a')  
        author = article.find('div', class_='author')  
        date = article.find('div', class_='date')  
        if title == None:
            continue
        else:
            number = number + 1 
            print("文章編號:", number)  
            print("文章標題:", title.text)
            print("作者:", author.text)
            print("日期:", date.text)
            print("="*100)  

    before = objsoup.find_all('a', class_='btn wide')   
    url2 = before[1].get('href')
    counter += 1

### 
import requests, bs4
url = "https://new.ntpu.edu.tw/"
response=requests.get(url)
bs4Obj = bs4.BeautifulSoup(response.text, 'lxml')

print(bs4Obj.prettify())    
print(bs4Obj.title)
if bs4Obj.title :
    print(bs4Obj.title.text)

