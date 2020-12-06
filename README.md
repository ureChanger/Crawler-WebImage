# Crawler-WebImage
Google과 Naver의 검색 이미지들을 한번에 원하는 수 만큼 다운로드해주는 크롤링 프로젝트
> ARMY 11개월 기념 파이썬 프로젝트
>
>![content](https://user-images.githubusercontent.com/56578913/101244919-a4642200-374c-11eb-850c-9bc6f873e142.png)
>
>![goormIDE_badge](https://img.shields.io/badge/goormIDE-FREE-blue)
>![python_badge](https://img.shields.io/badge/-ver_2.7-blue?logo=Python&logoColor=white)
>![Python_badge](https://img.shields.io/badge/-ver_3.6-blue?logo=Python&logoColor=white)

- 기간: 2020.12.01 ~ 2020.12.05
- [참고 기술블로그](https://towardsdatascience.com/image-scraping-with-python-a96feda8af2d)

## Example
### For Static Site
![image](https://user-images.githubusercontent.com/56578913/101244452-053e2b00-374a-11eb-88aa-7b50aa256ad1.png)
![image](https://user-images.githubusercontent.com/56578913/101244478-2141cc80-374a-11eb-924f-c559f6d4d9a8.png)

### For Dynamic Site
![image](https://user-images.githubusercontent.com/56578913/101245308-4be25400-374f-11eb-8365-ba71fcfbc328.png)
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

## How to use
- 정적 사이트에서의 크롤링: crawlingGoogle.py, crawlingNaver.py 
```
0. images 디렉토리를 생성
1. crawlingGoogle.py 또는 crawlingNaver.py의 keyword에 검색어를 입력
2. 터미널에 python crawlingGoogle.py 또는 crawlingNaver.py를 입력
3. 이미지 다운로드 확인
```
>Example
```python
keyword = "your keyword"
```

- 동적 사이트에서의 크롤링: Crawler-GoogleImg, Crawler-NaverImg 
```
0. images 디렉토리를 생성
1. Google, Naver 중 이미지를 얻을 곳을 선택하고 그에 맞는 디렉토리를 선택
2. Crawler/main.py의 search_term에 검색어를 입력
3. Crawler/main.py의 max_image에 다운로드 할 이미지 수를 입력
4. 터미널에 python main.py 입력
```
>Example
```python
search_term = "your keyword"
max_image = 150
```

## Architecture
main.py > search_and_download > get_image_links > download_image

## Developer
- [박길현](https://github.com/ureChanger)
