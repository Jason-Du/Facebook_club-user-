from selenium import webdriver #從library中引入webdriver
from bs4 import BeautifulSoup
import pandas as pd
import os
# browser = webdriver.Chrome()    #開啟chrome browser
import time
import os
class Click_more_comment():
	def __init__(self,
				 Btns_all_comment_path_input,
				 Btns_span_comment_path_s1input,
				 Btns_span_comment_path_s2input,
				 # Btn_below_comment_parent_input,
				 # Btn_sandwich_comment_parent_input,
				 comment_location_path_input,
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

		# self.Btn_below_comment_parent=Btn_below_comment_parent_input
		# self.Btn_sandwich_comment_parent=Btn_sandwich_comment_parent_input

		self.Btn_below_comment = Btn_below_comment_input
		self.Btn_below_name_comment = Btn_below_name_commemt_input
		self.Btn_below_sandwich_comment=Btn_sandwich_comment_input
		self.comment_location_path=comment_location_path_input
		self.post_location_path = post_location_path_input
		self.driver = driver_input
		self.post_num = post_num_input + 1
	def Click_span_all_comment(self):
		pass
		for comment_index in range(1, self.post_num):
			try:
				# solving comment problem for comment span up
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
			except:
				pass
			try:
				# solving comment problem for comment span below
				Btns_all_comment = self.driver.find_element_by_xpath(self.Btns_all_comment_path.format(comment_index))
				Btns_all_comment.click()
				time.sleep(2)
				Btns_span_comment_s2 = self.driver.find_element_by_xpath(self.Btns_span_comment_path_s2.format(comment_index))
				Btns_span_comment_s2.click()
				print("***************************************")
				print("Click_span_all_comment success 2 stage")
				print("***************************************")
			except:
				pass

	def Click_comment_below(self):
		pass
		for comment_index in range(1,self.post_num):
			try:
				if comment_index==2:
					pass
				else:
					# os.system('pause')
					post = self.driver.find_element_by_xpath(self.post_location_path.format(comment_index))
					self.driver.execute_script("arguments[0].scrollIntoView(true);", post)
				print("POST:{} ON GOING".format(comment_index))
				# Btns_all_comment = self.driver.find_element_by_xpath(self.Btns_all_comment_path.format(comment_index))
				# Btns_all_comment.click()
			except:
				print("NO POST")
				continue
			for respondent_index in range(1,30):
				try:
					# 一般型展開留言
					if respondent_index==1:
						pass
					else:
						comment_locate = self.driver.find_element_by_xpath(self.comment_location_path.format(comment_index,respondent_index-1))
						self.driver.execute_script("arguments[0].scrollIntoView(true);", comment_locate)
					print("comment index:{} respondent_index:{} is ongoing".format(comment_index,respondent_index))
					time.sleep(1)
					Btn_below_comment=self.driver.find_element_by_xpath(self.Btn_below_comment.format(comment_index,respondent_index))
					Btn_below_comment.click()
					print("***************************************")
					print("Click_comment_below success comment index:{} respondent_index:{}".format(comment_index,respondent_index))
					print("***************************************")
				except:
					pass
					try:
						# XXX回復型展開留言

						Btn_below_name_comment=self.driver.find_element_by_xpath(self.Btn_below_name_comment.format(comment_index,respondent_index))
						print("capture  Btn_below_name_comment:{}".format(respondent_index))
						# os.system("pause")
						Btn_below_name_comment.click()
						print("***************************************")
						print("Click_below_name index:{} respondent_index:{}".format(comment_index,respondent_index))
						print("***************************************")
						time.sleep(1)
					except:
						pass
						try:
							# 夾層型展開留言
							Btn_below_sandwich_comment=self.driver.find_element_by_xpath(self.Btn_below_sandwich_comment.format(comment_index,respondent_index))
							print("capture  below_sandwich_comment:{}".format(respondent_index))
							Btn_below_sandwich_comment.click()
							print("***************************************")
							print("Click_below_sandwich index:{} respondent_index:{}".format(comment_index, respondent_index))
							print("***************************************")
							time.sleep(1)
						except:
							pass
		htmltext= self.driver.page_source
		return htmltext

class Check_emoji():
	def __init__(self,
				 emoji_span_path_input,
				 emoji_close_path_input,
				 post_num_input,
				 driver_input,
				 post_location_path_input,
				 reaction_s1_path_input,
				 reaction_s2_path_input,
				 reaction_s0_path_input
				 ):
		self.emoji_span_path=emoji_span_path_input
		self.emoji_close_path=emoji_close_path_input
		self.post_location_path = post_location_path_input
		self.post_num = post_num_input+1
		self.driver=driver_input
		self.reaction_s1_path=reaction_s1_path_input
		self.reaction_s2_path=reaction_s2_path_input
		self.reaction_s0_path=reaction_s0_path_input

	def emoji_user_check(self):
		respondent_list=[]
		for post_index in range(2,self.post_num):
			try:
				if post_index==2:
					pass
				else:
					post = self.driver.find_element_by_xpath(self.post_location_path.format(post_index-1))
					post.click()

				time.sleep(1)
				print("post:{} is on going".format(post_index))

				test = self.driver.find_element_by_xpath(self.emoji_span_path.format(post_index))
				print("success capture xpath")
				test.click()
				time.sleep(1)
				print("***************************************")
				print("Click_span_emoji success 1 stage ")
				print("***************************************")
			except:
				print("post {}reaction icon is not exist".format(post_index))
				time.sleep(1)
				continue
			htmltext = self.driver.page_source
			soup = BeautifulSoup(htmltext,'html.parser')
			body = soup.find('body')
			reaction_s0=body.select(self.reaction_s0_path)[0]
			# respondent_list = []
			for index in range(20):
				print("reaction window success 1 stage")
				try:
					reaction_s1 = reaction_s0.select(self.reaction_s1_path)[index]
					print("reaction window success 2 stage")
					reaction_name_class=reaction_s1.select(self.reaction_s2_path)
					print("reaction window success 3 stage")
					reaction_name_class=str(reaction_name_class)
					reaction_name= reaction_name_class.split(">", 1)[1].split("<", 1)[0]
					print(reaction_name)
					respondent_list.append(reaction_name)
				except:
					test_close = self.driver.find_element_by_xpath(self.emoji_close_path)
					test_close.click()
					time.sleep(1)
					break
		return respondent_list

		# return respondent_list
			# for respondent_index in range(1,60):
			# 	try:
			#
			# 		respondent = self.driver.find_element_by_xpath(self.emoji_user_path.format(respondent_index))
			# 		self.driver.execute_script("arguments[0].scrollIntoView(true);", respondent)
			# 		time.sleep(1)
			# 		print("respondent_index :{}".format(respondent_index))
			# 		print("***************************************")
			# 		print("Click_span_emoji success 2 stage")
			# 		print("***************************************")
			# 		respondent_list.append(respondent.text)
			# 	except:
			# 		test_close = driver.find_element_by_xpath(self.emoji_close_path)
			# 		test_close.click()
			# 		time.sleep(1)
			# 		break
		# return respondent_list

class Check_comment():
	def __init__(self,htmltext_input,
				 post_path_input,
				 respondent_path_input,
				 post_num_input,
				 content_path_s1_input,
				 content_path_s2_input
				 ):
		self.htmltext=htmltext_input
		self.post_path=post_path_input
		self.respondent_path=respondent_path_input
		self.post_num=post_num_input
		self.content_s1_path=content_path_s1_input
		self.content_s2_path=content_path_s2_input
		pass
	def respondent_check(self):
		soup = BeautifulSoup(self.htmltext,
							 'html.parser'
							 )
		body = soup.find('body')
		respondent_list = []
		for post_index in range(self.post_num):
			try:
				posts = body.select(self.post_path)[post_index]
				for respondent_index in range(0, 30):
					respondent = posts.select(self.respondent_path)[respondent_index]
					print('success scratch the comment.{} respondent_index:{}'.format(post_index,respondent_index))
					respondent = str(respondent)
					respondent = respondent.split(">", 1)[1].split("<", 1)[0]
					print(respondent)
					respondent_list.append(respondent)
			except:
				continue
		return respondent_list
	def content_check(self):
		soup = BeautifulSoup(self.htmltext,
							 'html.parser'
							 )
		body = soup.find('body')
		content_list = []
		for post_index in range(self.post_num):
			try:
				posts = body.select(self.post_path)[post_index]
				for respondent_index in range(0, 30):
					content_s1 =posts.select(self.content_s1_path)[respondent_index]
					print('success scratch the comment.{} respondent_index:{}'.format(post_index, respondent_index))
					print("stage 1 sucessful scratch")
					print(content_s1)
					content_s2=content_s1.select(self.content_s2_path)
					print("stage 2 sucessful scratch")
					content_s2=str(content_s2)
					content_s2=content_s2.split(">", 1)[1].split("<", 1)[0]
					print(content_s2)
					content_list.append(content_s2)
					# respondent = str(respondent)
					# respondent = respondent.split(">", 1)[1].split("<", 1)[0]
					# print(respondent)
			except:
				pass
		return content_list

def data_analyze_content(respondent_list, content_list):
	df=pd.DataFrame(dict(回復者ID=respondent_list, 回覆留言內容=content_list))
	df.to_csv('content_activity.csv', index=False,encoding="utf_8_sig")





def data_analyze_times(comment_persons_list, emoji_persons_list):
	all_persons = list(set(comment_persons_list+emoji_persons_list))
	comment_times = []
	emoji_times = []
	for p in all_persons:
		comment_times.append(comment_persons_list.count(p))
		emoji_times.append(emoji_persons_list.count(p))

	data=[all_persons,comment_times,emoji_times]
	df=pd.DataFrame(dict(ID=all_persons,回復表情次數=emoji_times, 回覆留言次數=comment_times))
	df.to_csv('member_activity.csv', index=False,encoding="utf_8_sig")



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
	Test = Click_more_comment(
		Btns_all_comment_path_input="/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[2]/div/div[{}]/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[2]/span[2]/div",

		Btns_span_comment_path_s1input="/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[2]/div/div[{}]/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[2]/div/div[2]",

		Btns_span_comment_path_s2input="/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[2]/div/div[{}]/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[3]/div/div[2]",

		post_location_path_input="/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[2]/div/div[{}]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[3]/div",

		Btn_below_comment_input="/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[2]/div/div[{}]/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/ul/li[{}]/div[2]/div/div/div/div[2]",

		Btn_below_name_commemt_input="/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[2]/div/div[{}]/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/ul/li[{}]/div[2]/div/div/div[2]",
		# 						     /html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[2]/div/div[4]/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/ul/li[4]/div[2]/div/div/div[2]

		Btn_sandwich_comment_input="/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[2]/div/div[{}]/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/ul/li[{}]/div[2]/div/div[1]/div[2]",

		comment_location_path_input="/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[2]/div/div[{}]/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/ul/li[{}]/div[1]/div/div[2]/div/div[2]/div/div",
		# 							/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[2]/div/div[4]/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/ul/li[4]/div[1]/div/div[2]/div
		post_num_input=5,

		driver_input=driver
		)
	emojiTest=Check_emoji(
		emoji_span_path_input="/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[2]/div/div[{}]/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[1]/div/div[1]/span[2]/div",
		# 					  /html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[1]/div/div[1]/span[2]/div

		emoji_close_path_input="/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div",

		post_location_path_input="/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[2]/div/div[{}]/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[2]/span[2]/div",
		post_num_input=5,
		driver_input=driver,

		reaction_s0_path_input='div[class="l9j0dhe7 tkr6xdv7"]',

		reaction_s1_path_input="div[data-visualcompletion='ignore-dynamic']",

		reaction_s2_path_input='a[class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p"]',

			)

	Test.Click_span_all_comment()
	driver.execute_script("window.scroll(0, 0);")
	time.sleep(1)
	htmltext=Test.Click_comment_below()



























	# Comment_test = Check_comment(htmltext_input=htmltext,
	#
	# 							 post_path_input='div[class="du4w35lb k4urcfbm l9j0dhe7 sjgh65i0"]',
	#
	# 							 respondent_path_input='span[class="oi732d6d ik7dh3pa d2edcug0 hpfvmrgz qv66sw1b c1et5uql a8c37x1j hop8lmos enqfppq2 e9vueds3 j5wam9gi lrazzd5p oo9gr5id"]',
	#
	# 							 content_path_s1_input="span[class='oi732d6d ik7dh3pa d2edcug0 hpfvmrgz qv66sw1b c1et5uql a8c37x1j muag1w35 ew0dbk1b jq4qci2q a3bd9o3v knj5qynh oo9gr5id']",
	# 							 content_path_s2_input="div[dir='auto']",
	#
	# 							 post_num_input=5
	# 							 )
	# time.sleep(1)


	# respondent_list=Comment_test.respondent_check()
	# comment_list=Comment_test.content_check()
	#
	#
	# print("comment user length{}".format(len(comment_list)))
	# print("content user length{}".format(len(respondent_list)))
	#
	#
	# data_analyze_content(respondent_list=respondent_list, content_list=comment_list)
	#
	#
	# driver.execute_script("window.scroll(0, 0);")
	#
	# emoji_list=emojiTest.emoji_user_check()
	# data_analyze_times(comment_persons_list=respondent_list,emoji_persons_list=emoji_list)