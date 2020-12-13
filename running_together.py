#!/usr/bin/python
# #-*- coding:utf-8 -*-

from Crawler_GoogleImg.main import playGoogleCrawler
from Crawler_NaverImg.main import playNaverCrawler


#검색할 키워드 입력
name_list = ["Your Keyword"]

#총 다운로드 받을 이미지 수
max_image = 100

for i in name_list:
    playGoogleCrawler(i, max_image//2)
    playNaverCrawler(i,max_image//2)