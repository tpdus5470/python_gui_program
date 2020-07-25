# 크롤링을 통해 필요한 정보를 띄우기 위한 테스트 입니다.
from urllib.request import urlopen, Request
import urllib
import bs4
from bs4 import BeautifulSoup

location = '성남시'  # 도시 입력
enc_location = urllib.parse.quote(location + '+날씨')

url_a = 'https://search.naver.com/search.naver?ie=utf8&query='+ enc_location
# 날씨 정보를 나타내는 네이버 url
req = Request(url_a)
page = urlopen(req)
html = page.read()
soup_a = bs4.BeautifulSoup(html,'html5lib')
print('현재 ' + location + ' 날씨는 ' +
      soup_a.find('p', class_='info_temperature').find('span', class_='todaytemp').text
      + "도 " + soup_a.find('p',class_='cast_txt').text  )
# 필요한 부분만 크롤링함
url_b = 'https://m.news.naver.com/rankingList.nhn'  # 네이버 뉴스 url
response=urllib.request.urlopen(url_b)
soup_b=BeautifulSoup(response,'html.parser')
results=soup_b.select("div.commonlist_tx_headline")   
i=1
for result in results:
    print(str(i)+ ". " +result.string)
    i+=1

# 헤드라인만 순차적으로 출력


