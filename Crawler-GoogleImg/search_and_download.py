import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from get_image_links import fetch_image_urls
from download_image import persist_image

def search_and_download(search_term, target_path='images', number_images=40):
    target_name = '-'.join(search_term.split())
    target_folder = os.path.join(str(target_path)+ '/'+target_name)
    
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        
    with webdriver.Chrome(options=options) as driver:
        res = fetch_image_urls(search_term, number_images, driver=driver, sleep_between_interactions=0.5)
        print("4. Get linkes: "+str(res))
    
    for elem in res:
        persist_image(target_folder, elem)
    
    print("5. finish")

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument('--disable-dev-shm-usage') 