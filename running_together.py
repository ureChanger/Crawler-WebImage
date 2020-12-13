#!/usr/bin/python
# #-*- coding:utf-8 -*-

from Crawler_GoogleImg.main import playGoogleCrawler
from Crawler_NaverImg.main import playNaverCrawler


#이철산-스테파니 리는 기존 파일 사용
name_list = ["노혜리"]
max_image = 100

for i in name_list:
    playGoogleCrawler(i, max_image)
    playNaverCrawler(i,max_image)