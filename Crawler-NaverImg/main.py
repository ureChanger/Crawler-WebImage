#!/usr/bin/python
#-*- coding:utf-8 -*-
from search_and_download import search_and_download

search_term = "스타트업 서달미"
max_image = 50
    
print("1. start search_and_download!")
    
search_and_download(search_term=search_term, number_images=max_image)