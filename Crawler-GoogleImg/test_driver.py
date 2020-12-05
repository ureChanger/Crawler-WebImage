from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument('--disable-dev-shm-usage')    

url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

driver = webdriver.Chrome(options=options)
driver.get(url.format(q='korea'))

print(driver.find_elements_by_css_selector('img.n3VNCb'))