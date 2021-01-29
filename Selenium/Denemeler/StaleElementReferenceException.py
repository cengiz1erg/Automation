# Bu hatadan kurtulmak için bir alternatif. Muhtemelen açılır kutuya her tıklayışta XPATH değişti ve bu nedenle güvenilir bir XPATH yaratıldı.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})

driver = webdriver.Chrome(options=option, executable_path=r"C:\Program Files (x86)\chromedriver.exe")
driver.get("https://www.teknosa.com/bilgisayar-c-102")
box_element = driver.find_element_by_id("sortOptions1")
liste = [i for i in box_element.find_elements_by_tag_name("option")]
for a in range(1, len(liste)):
    element = driver.find_element_by_xpath('//*[@id="sortOptions1"]/option[{b}]'.format(b=a))
    print("{b}. döngü başladı".format(b=a))
    print(element.text.strip())
    element.click()
    print("{b}. sayfa yüklendi".format(b=a))
    print("-------------------")
