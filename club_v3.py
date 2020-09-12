from selenium import webdriver #從library中引入webdriver
from bs4 import BeautifulSoup
import pandas as pd
import os
# browser = webdriver.Chrome()    #開啟chrome browser
import time
import os

def click_more_comment(driver):
    pass
    driver











if __name__ == '__main__':
	profile = webdriver.FirefoxProfile() # 新增firefox的設定
	profile.set_preference("dom.webnotifications.enabled", False) # 將頁面通知關掉
	profile.update_preferences() # 需要再更新目前firefox新的偏好設定
	driver = webdriver.Firefox(firefox_profile=profile)
	driver.get("http://www.facebook.com")
	time.sleep(2)

	driver.find_element_by_id("email").send_keys("dushiun@gmail.com") # 將USERNAME改為你的臉書帳號
	driver.find_element_by_id("pass").send_keys("jason870225") # 將PASSWORD改為你的臉書密碼
	driver.find_element_by_id("u_0_b").click()

	time.sleep(2)
	driver.get("https://www.facebook.com/groups/342191540266126")
	time.sleep(2)