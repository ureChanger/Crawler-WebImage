# Crawler-WebImage
Google과 Naver의 검색 이미지들을 한번에 원하는 수 만큼 다운로드해주는 크롤링 프로젝트
> ARMY 11개월 기념 파이썬 프로젝트
>
>![content](https://user-images.githubusercontent.com/56578913/101244919-a4642200-374c-11eb-850c-9bc6f873e142.png)
>
>![goormIDE_badge](https://img.shields.io/badge/goormIDE-FREE-blue)
>![python_badge](https://img.shields.io/badge/-ver_2.7-blue?logo=Python&logoColor=white)
>![Python_badge](https://img.shields.io/badge/-ver_3.6-blue?logo=Python&logoColor=white)

- 기간: 2020.12.01 ~ 2020.12.13
- [참고 기술블로그](https://towardsdatascience.com/image-scraping-with-python-a96feda8af2d)

## Example
### For Static Site
![image](https://user-images.githubusercontent.com/56578913/101244452-053e2b00-374a-11eb-88aa-7b50aa256ad1.png)
![image](https://user-images.githubusercontent.com/56578913/101244478-2141cc80-374a-11eb-924f-c559f6d4d9a8.png)

### For Dynamic Site (Recommendation)
![image](https://user-images.githubusercontent.com/56578913/102014987-161b1c00-3d9c-11eb-815f-176fc3085c8d.png)
![image](https://user-images.githubusercontent.com/56578913/101245328-687e8c00-374f-11eb-9986-fd826e7611c6.png)

## Dependency Module - 사용 전에 꼭 ! 😆
>정적 페이지를 위한 크롤링 파일은 Beautiful Soup, urllib를, 동적 페이지를 위한 크롤링 디렉토리는 Selenium, Pillow를 주로 이용함

When Use on Static Site(crawlingGoogle.py, crawlingNaver.py)
``` 
pip install urllib
pip install bs4
```

When Use on Dynamic Site(Crawler-GoogleImg, Crawler-NaverImg)
```
pip install selenium
pip install urllib
pip install Pillow
```
 
```
install Chrome
install ChromeDriver
```

#### ChromeDriver Download
https://chromedriver.chromium.org/

#### ChromeDriver Download on groomIDE
https://help.goorm.io/en/goormide/18.faq/language-and-environment/selenium-chromewebdriver#check-the-chrome-version

## How to use
- 정적 사이트에서의 크롤링: Crawler-WebImage/Crawler_StaticSiteImg/crawlingGoogle.py, crawlingNaver.py 
```
0. images 디렉토리를 생성
1. crawlingGoogle.py 또는 crawlingNaver.py의 keyword에 검색어를 입력
2. 터미널에 python crawlingGoogle.py 또는 crawlingNaver.py를 입력
3. 이미지 다운로드 확인
```
#### Example
```python
keyword = "your keyword"
```

- 동적 사이트에서의 크롤링: Crawler-WebImage/main.py
```
0. images 디렉토리를 생성
1. main.py 파일 열기
2. 검색할 키워드, 다운로드 받을 이미지 수, 크롤링 할 사이트를 입력
3. 터미널에 python main.py 입력
```
#### Example
```python
# 검색할 키워드 입력
name_list = ["서울"]

# 총 다운로드 받을 이미지 수 - 100을 수정
max_image = 200

# 크롤링 할 사이트 입력 - 1. Google 2. Naver 3. Both
crawler_site = "Both"
```

## Architecture
main > search_and_download > get_image_links > download_image

## Functions
```python
from search_and_download import search_and_download
from get_image_links import fetch_image_urls
from download_image import persist_image
```

|Name|Description|
|---|---|
|`main`|검색할 키워드와 이미지 수를 입력|
|`search_and_download`|이미지 검색, 저장 함수를 호출하는 함수|
|`fetch_image_urls`|이미지의 url을 가져오는 함수|
|`persist_image`|이미지를 정해진 경로에 저장하는 함수|


## Developer
- [박길현](https://github.com/ureChanger)
