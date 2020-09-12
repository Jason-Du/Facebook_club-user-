from selenium import webdriver #從library中引入webdriver
from bs4 import BeautifulSoup
import pandas as pd
import os
# browser = webdriver.Chrome()    #開啟chrome browser
import time
import os
from selenium.webdriver.remote.webelement import WebElement

def click_more_comment(driver):
	pass
	post=driver.find_elements_by_xpath("//div[@class='du4w35lb k4urcfbm l9j0dhe7 sjgh65i0']")
	print(len(post))
	for i in post:
		try:
			try:
				driver.execute_script("arguments[0].scrollIntoView(false);", i)
				time.sleep(1)
				more_comment=i.find_elements_by_xpath('.//div[@class="oajrlxb2 bp9cbjyn g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw '
													  'mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 pq6dq46d mg4g778l btwxx1t3 g5gj957u p7hjln8o kvgmc6g5 '
													  'cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys p8fzw8mz qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh gpro0wi8 m9osqain buofh1pr"]'
													  )
				for j in more_comment:
					try:
						driver.execute_script("arguments[0].scrollIntoView(false);", j)
						time.sleep(1)
						j.click()
					except:
						print("FAIL CLICK")
			except:
				print("FAIL FIND LOCATION")
		except:
			print("NO more_comment BUTTON")
			pass


def click_more_content(driver):
	post = driver.find_elements_by_xpath("//div[@class='du4w35lb k4urcfbm l9j0dhe7 sjgh65i0']")
	print(len(post))
	for i in post:
		try:
			driver.execute_script("arguments[0].scrollIntoView(false);", i)
			time.sleep(1)
			more_content = i.find_element_by_xpath('.//div[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p"]')
			try:
				driver.execute_script("arguments[0].scrollIntoView(false);", more_content)
				time.sleep(1)
				more_content.click()
			except:
					print("FAIL CLICK")
		except:
			print("NO more_content BUTTON")
			pass
def make_post_dict():
	post = driver.find_elements_by_xpath("//div[@class='du4w35lb k4urcfbm l9j0dhe7 sjgh65i0']")
	post_dict={}
	print(len(post))
	for i in post:
		driver.execute_script("arguments[0].scrollIntoView(false);", i)
		try:
			pass
		except:
			pass




	pass














if __name__ == '__main__':

	profile = webdriver.FirefoxProfile() # 新增firefox的設定
	profile.set_preference("dom.webnotifications.enabled", False) # 將頁面通知關掉
	profile.update_preferences() # 需要再更新目前firefox新的偏好設定
	driver = webdriver.Firefox(firefox_profile=profile)
	driver.get("http://www.facebook.com")
	time.sleep(2)

	driver.find_element_by_id("email").send_keys("dushiun@gmail.com") # 將USERNAME改為你的臉書帳號
	driver.find_element_by_id("pass").send_keys("jason870225") # 將PASSWORD改為你的臉書密碼
	try:
		driver.find_element_by_id("u_0_b").click()
	except:
		driver.find_element_by_id("u_0_2").click()

	time.sleep(2)
	driver.get("https://www.facebook.com/groups/342191540266126")
	time.sleep(2)
	post=4
	for i in range(post):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(1)
	# click_more_comment(driver=driver)
	click_more_content(driver=driver)