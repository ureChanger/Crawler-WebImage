from urllib.request import Request, urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import os

#Google
#Create a Directory 'images' in advance

keyword = "spain travel"
shortKeyword = '-'.join(keyword.split())

os.makedirs("images_google/"+shortKeyword)

#url source
url = "https://www.google.com/search?q="
queryImg = "&tbm=isch"
callDetail = "#imgrc="

req = Request(url+quote_plus(keyword)+queryImg, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'})
res = urlopen(req).read()
print("good!")

soup = BeautifulSoup(res, 'html.parser')
num = 0

#get the google search image(max: 80)
for anchor in soup.find_all('div', class_="isv-r PNCib MSM1fd BUooTd"):
    imageURL = anchor.find('img', class_='rg_i Q4LuWd').get('data-src')
    
    if not imageURL == None:
        f = urlopen(imageURL)
        img = f.read()

        #save
        new_file = open("images_google/"+shortKeyword+"/img"+str(num)+".jpg",'wb')
        new_file.write(img)
    
        num += 1
        print(str(num)+": "+keyword+" download! "+"URL: "+str(imageURL))
