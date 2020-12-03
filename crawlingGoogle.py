from urllib.request import Request, urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import os

#구글 전용입니다!
#사전에 'images' 디렉토리를 만들어주세요!

#검색할 키워드를 입력
keyword = "germany travel"

#키워드와 같은 이름의 디렉토리 생성
#os.makedirs("images_google/"+keyword)

#url 소스를 가져옴
url = "https://www.google.com/search?q="
queryImg = "&tbm=isch"
callDetail = "#imgrc="

req = Request(url+quote_plus(keyword)+queryImg, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'})
res = urlopen(req, timeout=10).read()
print("good!")

soup = BeautifulSoup(res, 'html.parser')
num = 1

for anchor in soup.find_all('div', class_='isv-r PNCib MSM1fd BUooTd'):
    dataID = quote_plus(anchor.get('data-id'))
    imageURL = anchor.find('img').get('data-src')
    
    #개발해야함 - 세부이미지 class로 검색 후 이미지 링크 구하기
    resImg = urlopen(req+callDetail+dataID).read()
    soupImg = BeautifulSoup(resImg, 'html.parser')
    
    
    imageURL = anchor.find('img').get('data-src')
    
    num += 1
        
        #JUexfJqLEcoeeM
# #네이버 이미지 검색에서 이미지 url을 가지고 옴(50개)

# for anchor in soup.find_all('div', class_="img_area _item"):
#     imageURL = anchor.find('img').get('data-source')
#     f = urllib.request.urlopen(imageURL)
#     img = f.read()
    
#     #저장
#     new_file = open("images/"+keyword+"/img"+str(num)+".jpg",'wb')
#     new_file.write(img)
    
#     num += 1
#     print(str(num)+": "+keyword+" download!")
