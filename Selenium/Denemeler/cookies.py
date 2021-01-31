from selenium import webdriver

PATH = r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)

driver.get("https://www.amazon.com/")

# Returns a list of dictionaries, corresponding to cookies visible in the current session
cookies_list = driver.get_cookies()

# Get a single cookie by name. Returns the cookie if found, None if not.
cookie = driver.get_cookie("ubid-main")

# Adds a cookie to your current session.
driver.add_cookie({
    'name': 'blabla',  # name ve value
    'value': 'blablabla'
})

# ------------------------
# for cookie in cookies_list:
#     print(cookie['domain'])
# .amazon.com
# www.amazon.com
# .amazon.com
# .amazon.com
# .amazon.com
# .amazon.com
# .amazon.com
# .amazon.com
# -------------------------

#----------------------------------
# print(cookie_list)
# [{'domain': '.amazon.com', 'expiry': 1643621643, 'httpOnly': False, 'name': 'ubid-main', 'path': '/', 'secure': True, 'value': '135-4986093-0796620'},
#  {'domain': 'www.amazon.com', 'expiry': 1642325642, 'httpOnly': False, 'name': 'csm-hit', 'path': '/', 'secure': False, 'value': 'tb:s-XF1CFDQY7TXQ5SKHMJNW|1612085641333&t:1612085642235&adb:adblk_no'},
#  {'domain': '.amazon.com', 'httpOnly': False, 'name': 'skin', 'path': '/', 'secure': False, 'value': 'noskin'},
#  {'domain': '.amazon.com', 'expiry': 1643621640, 'httpOnly': True, 'name': 'sp-cdn', 'path': '/', 'secure': True, 'value': '"L5Z9:TR"'},
#  {'domain': '.amazon.com', 'expiry': 1643621643, 'httpOnly': False, 'name': 'session-id-time', 'path': '/', 'secure': False, 'value': '2082787201l'},
#  {'domain': '.amazon.com', 'expiry': 1643621640, 'httpOnly': False, 'name': 'i18n-prefs', 'path': '/', 'secure': False, 'value': 'USD'},
#  {'domain': '.amazon.com', 'expiry': 1643621643, 'httpOnly': False, 'name': 'session-token', 'path': '/', 'secure': True, 'value': 'O1bqnCqALUgR5HplgdybowljtZL6g55wPmt7M60xHnKqb+b/TD/BjqKe0UQxhY7m3p2RnibOJE42gzZhTfRi0lU7KkFv8yYDX1ZVTkZVhjaItFvVzvyRYZzDaF1ELP0oyrd0ICu7qRFG44SLcaofGhpCBQm2aG4raiEufhY09j+ypPTwYuXBu171Tg1wVkjUF3a+qpINfUUrBB+7jdYnADwVW1ORpws2ooiHM3gy+daQxW7sWCwiLWXNHD/gGZYt'},
#  {'domain': '.amazon.com', 'expiry': 1643621643, 'httpOnly': False, 'name': 'session-id', 'path': '/', 'secure': True, 'value': '131-7151519-4420113'}]
#----------------------------------
