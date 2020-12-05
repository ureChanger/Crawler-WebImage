from selenium import webdriver
import time
import urllib

def fetch_image_urls(query, max_links_to_fetch, driver, sleep_between_interactions=1):
    print("2. start fetch_image_urls!")
    
    def scroll_to_end(driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeinght);")
        time.sleep(sleep_between_interactions)
    
    # build the google query
    naver_search_url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query={q}"
    
    #class image, actual_image, load_more_button
    naver_class = ["_img", "_image_source", "btn_more"]
    
    url = naver_search_url
    
    css_class = naver_class
    
    # load the page
    driver.get(url.format(q=urllib.quote(query)))
    
    image_urls = set()
    image_count = 0
    results_start = 0
    while image_count < max_links_to_fetch:
        scroll_to_end(driver)
        
        # get all image thumbnail results
        thumbnail_results = driver.find_elements_by_css_selector("img."+css_class[0])
        number_results = len(thumbnail_results)
        
        #print(str(thumbnail_results)
        print("Found:" + str(number_results) + " search results. Extracting links from - " + str(results_start) + ":" + str(number_results))
        
        for img in thumbnail_results[results_start:number_results]:
            if img.get_attribute('src') and 'http' in img.get_attribute('src'):
                image_urls.add(img.get_attribute('src'))

            image_count = len(image_urls)

            if image_count >= max_links_to_fetch:
                print("Found: {img_num} image links, done!".format(img_num=image_count))
                break
        
        else:
            print("Found:", len(image_urls), "image links, looking for more ...")
            time.sleep(30)
            #return
            load_more_button = driver.find_elements_by_css_selector('.{}'.format(css_class[2]))
            if load_more_button:
                driver.execute_script("document.querySelector('a.{}').click();".format(css_class[2]))
                
        # move the result startpoint further down
        results_start = len(thumbnail_results)
    
    return image_urls