#!/usr/bin/python
# #-*- coding:utf-8 -*-

##################################################################

# 검색할 키워드 입력
name_list = ["First Your Keyword", "Second Your Keyword", "..."]

# 총 다운로드 받을 이미지 수 - 100을 수정
max_image = 100

# 크롤링 할 사이트 입력 - 1. Google 2. Naver 3. Both
crawler_site = "Your Crawling Site"

##################################################################



from Crawler_GoogleImg.main import playGoogleCrawler
from Crawler_NaverImg.main import playNaverCrawler

half_maxImage = max_image//2

crawlerSite_list = {"Google": playGoogleCrawler, "Naver": playNaverCrawler, "Both": [playGoogleCrawler, playNaverCrawler]}

crawler_list = []

if crawler_site == "Both":
    crawler_list = crawlerSite_list[crawler_site]
else:
    crawler_list.append(crawlerSite_list[crawler_site])

num_image = 0

if crawler_site == "Google" or crawler_site == "Naver":
    num_image = max_image
elif crawler_site == "Both":
    num_image = half_maxImage
    
for keyword in name_list:
    for crawler in crawler_list:
        crawler(keyword, num_image)
