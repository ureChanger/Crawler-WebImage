import urllib.request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import os

#네이버 전용입니다!
#사전에 'images' 디렉토리를 만들어주세요!

#검색할 키워드를 입력
keyword = "지수"

#키워드와 같은 이름의 디렉토리 생성
os.makedirs("images/"+keyword)

#url 소스를 가져옴
url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query="
response = urllib.request.urlopen(url+quote_plus(keyword))

soup = BeautifulSoup(response, 'html.parser')
num = 0

#네이버 이미지 검색에서 이미지 url을 가지고 옴(50개)
for anchor in soup.find_all('div', class_="img_area _item"):
    imageURL = anchor.find('img').get('data-source')
    f = urllib.request.urlopen(imageURL)
    img = f.read()
    
    #저장
    new_file = open("images/"+keyword+"/img"+str(num)+".jpg",'wb')
    new_file.write(img)
    
    num += 1
    print(str(num)+": "+keyword+" download!")
