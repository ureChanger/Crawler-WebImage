from selenium import webdriver
import time

def fetch_image_urls(query, max_links_to_fetch, driver, sleep_between_interactions=1):
    print("2. start fetch_image_urls!")
    
    def scroll_to_end(driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeinght);")
        time.sleep(sleep_between_interactions)
    
    # build the google query
    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"
    
    # load the page
    driver.get(search_url.format(q=query))
    
    image_urls = set()
    image_count = 0
    results_start = 0
    while image_count < max_links_to_fetch:
        scroll_to_end(driver)
        
        # get all image thumbnail results
        thumbnail_results = driver.find_elements_by_css_selector("img.Q4LuWd")
        number_results = len(thumbnail_results)
        
        #print(str(thumbnail_results)
        print("Found:" + str(number_results) + " search results. Extracting links from - " + str(results_start) + ":" + str(number_results))
        
        for img in thumbnail_results[results_start:number_results]:
            # try to click every thumbnail such that we can get the real image behind it
            try:
                img.click()
                time.sleep(sleep_between_interactions)
            except Exception:
                continue
                
            # extract image image urls
            actual_images = driver.find_elements_by_css_selector('img.n3VNCb')
        
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    image_urls.add(actual_image.get_attribute('src'))
                    
            image_count = len(image_urls)
            
            if image_count >= max_links_to_fetch:
                print("Found: {len(image_urls)} image links, done!")
                break
        
        else:
            print("Found:", len(image_urls), "image links, looking for more ...")
            time.sleep(30)
            #return
            load_more_button = driver.find_elements_by_css_selector('.mye4qd')
            if load_more_button:
                driver.execute_script("document.querySelector('.mye4qd').click();")
                
        # move the result startpoint further down
        results_start = len(thumbnail_results)
    
    return image_urls