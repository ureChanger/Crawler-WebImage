#!/usr/bin/python
#-*- coding:utf-8 -*-
from search_and_download import search_and_download

def playGoogleCrawler(keyword, max_image):
    search_term = keyword

    print("1. start search_and_download!")

    search_and_download(search_term=search_term, number_images=max_image)