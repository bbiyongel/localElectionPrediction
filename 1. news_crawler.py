# -*- coding: utf-8 -*- 
from datetime import datetime
import os
import urllib.request
import urllib.parse

from bs4 import BeautifulSoup


now = datetime.now()

bs = BeautifulSoup
# Naver Open API(for Searching a word) 
defaultURL = 'https://openapi.naver.com/v1/search/news.xml?'
sort = 'sort=sim'
start = '&start=1'
display = '&display=100'
query = '&query=' + urllib.parse.quote_plus(str("선거"))  
fullURL = defaultURL + sort + start + display + query
print("\n# 네이버 검색 Open API 사용 \n# " + fullURL + "\n")

def record_news():
    print( now )
    file.write(str(now))
    headers = {
        'Host' : 'openapi.naver.com',
        'User-Agent' : 'curl/7.43.0',
        'Accept' : '*/*',
        'Content-Type' : 'application/xml',
        'X-Naver-Client-Id' : '',
        'X-Naver-Client-Secret' : ''
    }
    req = urllib.request.Request(fullURL, headers=headers)
    f = urllib.request.urlopen(req)
    xmlsoup = bs(f.read(), 'html.parser')
    items = xmlsoup.find_all('item')
    for item in items:
        # <title> 내용
        file.write(item.title.get_text(strip=True) + '\n') 
        # <description> 내용
        file.write(item.description.get_text(strip=True) + '\n')
    file.close()
    print("\n# 뉴스 내용을 저장했습니다.")

if (os.path.exists("/.../naver_news.txt")):
    print("\n# 이미 텍스트파일이 존재합니다, 뉴스 내용을 추가합니다...\n")
    file = open("/.../naver_news.txt", "a", encoding='utf-8')
    record_news()
    
else:
    print("\n# 현재 해당 경로에 저장할 파일이 없습니다... \n텍스트파일을 생성해서 저장합니다...\n")
    file = open("/.../naver_news.txt", "w", encoding='utf-8')
    record_news()