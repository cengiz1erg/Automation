
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = r"C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.google.com/")
print(driver.title) # Google
# print(driver.page_source) -> sayfanın kaynak kodunu çıktı olarak verir

arama_cubugu = driver.find_element_by_name("q")
arama_cubugu.send_keys("cengiz ergün")
arama_cubugu.send_keys(Keys.RETURN)


# main = driver.find_elements_by_id("main") 
# Riskli kod, muhtemelen çalışmayacak. Çünkü bu kodun çalışması için bir önceki kodun oluşturacağı sayfanın şuan aradığımız ögeyi yüklemiş
# olması gerekir. Bunun yerine aşağıda "explicit waits" yapıp işi sağlama alalım.


try:
    main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "hide-focus-ring")))
except Exception:
    print("Bir şeyler yanlış gitti...")
else:
    print(main.text) # Haberler
finally:
    driver.quit()

# /// find_elements_by_tag_name liste veri tipi döndürür. Tag'a göre arama yaparsan bunu kullanabilirsin.

# /// önemli!
# Great tutorial for Selenium. It's important to note that Selenium is very slow, 
# and for any large scale project, it would take minutes (sometimes hours) to finish running, 
# so this web scraping approach should be the last option to be used for websites with heavy JavaScript. 
# The practical approach would be to send a GET request to the URL of the website and adding the search query to the end of 
# the URL and then parsing the response. You can see at 5:30, the URL has the query add "?s=test". 
# This is the same approach but maybe 100 times faster than using Selenium.
