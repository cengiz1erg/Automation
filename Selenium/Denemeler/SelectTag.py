from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})

driver = webdriver.Chrome(options=option, executable_path=r"C:\Program Files (x86)\chromedriver.exe")
driver.get("https://www.teknosa.com/bilgisayar-c-102")
select = Select(driver.find_element_by_id('sortOptions1'))
select.select_by_visible_text("Fiyata Göre (Artan)")
