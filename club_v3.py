from selenium import webdriver #從library中引入webdriver
from bs4 import BeautifulSoup
import pandas as pd
import os
import time
import re

def click_more_comment(driver):
	pass
	post=driver.find_elements_by_xpath("//div[@class='du4w35lb k4urcfbm l9j0dhe7 sjgh65i0']")
	for i in post:
		try:
			try:
				driver.execute_script("arguments[0].scrollIntoView(false);", i)
				time.sleep(1)
				more_comment=i.find_elements_by_xpath('.//div[@class="oajrlxb2 bp9cbjyn g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 '
													  'rq0escxv nhd2j8a9 pq6dq46d mg4g778l btwxx1t3 g5gj957u p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys p8fzw8mz qt6c0cv9 a8nywdso '
													  'l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh gpro0wi8 m9osqain buofh1pr"]'
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
			time.sleep(2)
			more_content = i.find_element_by_xpath('.//div[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv'
												   ' nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 '
												   'a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p"]')
			try:
				driver.execute_script("arguments[0].scrollIntoView(false);", more_content)
				time.sleep(2)
				more_content.click()
			except:
					print("FAIL CLICK")
		except:
			print("NO more_content BUTTON")
			pass
def make_post_dict(html_doc):
	soup = BeautifulSoup(html_doc, 'html.parser')
	comment_id_list=[]
	comment_content_list=[]
	like_id_list=[]
	angry_id_list=[]
	haha_id_list=[]
	care_id_list=[]
	love_id_list=[]
	sad_id_list=[]
	wow_id_list=[]
	all_data={}
	label_list=[]
	comment_dict={
		'comment id':comment_id_list,
		'comment content':comment_content_list
	}
	reaction_dict={
		'like id': like_id_list,
		'angry id': angry_id_list,
		'haha id': haha_id_list,
		'care id': care_id_list,
		'love id': love_id_list,
		'sad id': sad_id_list,
		'wow id': wow_id_list
		}
	post_dict={
		'poster':'',
		'post content':'',
		'post_share_link':'',
		'reaction':reaction_dict,
		'comment':comment_dict
	}
	body = soup.find('body')
	allpost=body.select('div[class="du4w35lb k4urcfbm l9j0dhe7 sjgh65i0"]')

	print(len(allpost))
	for post in allpost:
		# PO 文者 ID
		poster = post.select('div[class="lzcic4wl"]')[0].get('aria-labelledby')
		poster=post.select('h2[id={}]'.format(str(poster)))
		# print(poster)
		pattern = r'<span>(\w+)</span>'
		poster = re.search(pattern, 'r'+str(poster))
		print(poster.group(1))
		post_dict['poster']=poster
		#
		label_str = post.select('div[class="lzcic4wl"]')[0].get('aria-describedby')
		pattern=r'\w{3}_\w{1}_\w{2}'
		print(label_str)
		label_list=re.findall(pattern,str(label_str))
		label_list.pop(0)
		for index,label in enumerate(label_list):
			pass
			try:
				print(label)
				post_content=post.select('div[id={}]'.format(label))
			except:
				continue
			if index==0:
				pattern1=r'>(\w+)</div>'
				pattern2=r'>(\w+)<br>'
				content_list1=[]
				content_list2=[]
				str1=''
				#內容
				try:
					post_content=post_content.select('div[class="kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q"]')[0]
					try:
						content_list1=re.findall(pattern1,post_content)
					except:
						pass
					try:
						content_list2=re.findall(pattern2,post_content)
					except:
						pass
					content1=''.join([str(x) for x in content_list1])
					content2=''.join([str(x) for x in content_list2])
					pass
				except:
					print("FAIL GET content")
					pass
			if index==1:
				try:
					pass
				except:
					pass
			if index==2:
				try:
					pass
				except:
					pass
			if index==3:
				try:
					pass
				except:
					pass















if __name__ == '__main__':
	profile = webdriver.FirefoxProfile()# 新增firefox的設定
	profile.set_preference("dom.webnotifications.enabled", False)# 將頁面通知關掉
	profile.update_preferences()# 需要再更新目前firefox新的偏好設定
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
	post=5
	for i in range(post):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(2)
	# click_more_comment(driver=driver)
	# click_more_content(driver=driver)
	htmltext = driver.page_source
	#
	make_post_dict(html_doc=htmltext)