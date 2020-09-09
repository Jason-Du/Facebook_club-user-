from selenium import webdriver #從library中引入webdriver
from bs4 import BeautifulSoup
import pandas as pd
import os
# browser = webdriver.Chrome()    #開啟chrome browser
import time
class Click_more_comment():
	def __init__(self,
				 Btns_all_comment_path_input,
				 Btns_span_comment_path_s1input,
				 Btns_span_comment_path_s2input,
				 Btn_below_comment_parent_input,
				 Btn_sandwich_comment_parent_input,
				 Btn_below_comment_input,
				 Btn_below_name_commemt_input,
				 Btn_sandwich_comment_input,
				 post_location_path_input,
				 post_num_input,
				 driver_input
				 ):
		self.Btns_all_comment_path = Btns_all_comment_path_input
		self.Btns_span_comment_path_s1 = Btns_span_comment_path_s1input
		self.Btns_span_comment_path_s2 = Btns_span_comment_path_s2input

		self.Btn_below_comment_parent=Btn_below_comment_parent_input
		self.Btn_sandwich_comment_parent=Btn_sandwich_comment_parent_input

		self.Btn_below_comment = Btn_below_comment_input
		self.Btn_below_name_comment = Btn_below_name_commemt_input
		self.Btn_below_sandwich_comment=Btn_sandwich_comment_input
		self.post_location_path = post_location_path_input
		self.driver = driver_input
		self.post_num = post_num_input + 1
	def Click_span_all_comment(self):
		pass
		for comment_index in range(1, self.post_num):
			try:
				post = self.driver.find_element_by_xpath(self.post_location_path.format(comment_index))
				self.driver.execute_script("arguments[0].scrollIntoView(true);", post)
				print("post index:{}".format(comment_index))
				Btns_all_comment = self.driver.find_element_by_xpath(self.Btns_all_comment_path.format(comment_index))
				Btns_all_comment.click()
				time.sleep(1)
				for span_index in range(2):
					Btns_span_comment_s1 = self.driver.find_element_by_xpath(self.Btns_span_comment_path_s1.format(comment_index))
					Btns_span_comment_s1.click()
					print("Click_span_all_comment success 1 stage times:{}".format(span_index))
					time.sleep(2)
				try:
					Btns_all_comment = self.driver.find_element_by_xpath(self.Btns_all_comment_path.format(comment_index))
					Btns_all_comment.click()
					time.sleep(1)
					Btns_span_comment_s2 = self.driver.find_element_by_xpath(self.Btns_span_comment_path_s2)
					Btns_span_comment_s2.click()
					print("***************************************")
					print("Click_span_all_comment success 2 stage")
					print("***************************************")
					time.sleep(1)
				except:pass
			except:
				time.sleep(1)
				continue

	def Click_comment_below(self):
		pass
		for comment_index in range(1, self.post_num):
			for respondent_index in range(20):
				try:
					post = self.driver.find_element_by_xpath(self.post_location_path.format(comment_index))
					self.driver.execute_script("arguments[0].scrollIntoView(true);", post)
					print("comment index:{} respondent_index:{} is ongoing".format(comment_index, respondent_index))
					time.sleep(1)
					try:

						ISSANDWICH
						ISNORMAL_ISNAME
						Btn_below_comment = self.driver.find_element_by_xpath(
							self.Btn_below_comment.format(comment_index, respondent_index))
						Btn_below_comment.click()
						print("***************************************")
						print("Click_comment_below success comment index:{} respondent_index:{}".format(comment_index,
																										respondent_index))
						print("***************************************")
					except:
						continue
				except:
					continue
				try:
					Btn_below_comment = self.driver.find_element_by_xpath(
						self.Btn_below_multiple_comment.format(comment_index, respondent_index))
					Btn_below_comment.click()
					print("***************************************")
					print("Click_MULTIPLE comment index:{} respondent_index:{}".format(comment_index,
																					   respondent_index))
					print("***************************************")
					time.sleep(1)
				except:
					continue
		htmltext = self.driver.page_source
		return htmltext


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
	driver.get("https://www.facebook.com/groups/421125691712808")
	time.sleep(2)
	Test = Click_more_comment(
		Btns_all_comment_path_input="/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[2]/div/div[{}]/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[2]/span[2]/div",

		Btns_span_comment_path_s1input="/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[2]/div/div[{}]/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[2]/div/div[2]",

		Btns_span_comment_path_s2input="/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[2]/div/div[{}]/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[3]/div/div[2]",

		post_location_path_input="/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[2]/div/div[{}]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[3]/div",

		Btn_below_comment_input="",
		Btn_below_name_commemt_input="",

		Btn_sandwich_comment_input="",

		post_num_input=89,

		driver_input=driver
		)


	Test.Click_span_all_comment()
	Test.Click_comment_below()