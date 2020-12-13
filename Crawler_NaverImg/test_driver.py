#!/usr/bin/python
#-*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument('--disable-dev-shm-usage')    

google_search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"
naver_search_url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query={q}"

driver = webdriver.Chrome(options=options)
driver.get(naver_search_url.format(q=urllib.quote('스타트업 수지')))

thumbnail_results = driver.find_elements_by_css_selector('img._img')
print('find results: {result}'.format(result=len(thumbnail_results)))
for img in thumbnail_results:
    print(img.get_attribute('src'))
    try:
        img.click()
        print('click!')
        
        time.sleep(1)
    except Exception:
        print('no')
        continue
        