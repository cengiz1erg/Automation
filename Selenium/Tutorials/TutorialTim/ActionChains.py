from selenium import webdriver
from selenium.webdriver import ActionChains

PATH = r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

cookies_count = driver.find_element_by_id("cookies")
big_cookie = driver.find_element_by_id("bigCookie")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver=driver)
actions.click(big_cookie)

for i in range(5000):
    actions.perform()
    count = int(cookies_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver=driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
