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
			time.sleep(1)
			more_content = i.find_element_by_xpath('.//div[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv'
												   ' nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 '
												   'a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p"]')
			try:
				driver.execute_script("arguments[0].scrollIntoView(false);", more_content)
				time.sleep(1)
				more_content.click()
			except:
					print("FAIL CLICK")
		except:
			print("NO more_content BUTTON")
			pass
def make_post_dict(html_doc):
	soup = BeautifulSoup(html_doc, 'html.parser')
	# post dict list
	dataset=[]
	comment_below_dict_list=[]
	comment_dict_list=[]
	label_list=[]
	comment_below_dict={'comment id':'',
		'comment content':'',
		'comment link':'',
		'comment sticker':'',
		'comment img':''

	}
	comment_dict={
		'comment id':'',
		'comment content':'',
		'comment link':'',
		'comment sticker':'',
		'comment img':'',
		'comment_below':comment_below_dict_list
	}
	# reaction_dict={
	# 	'like id': '',
	# 	'angry id':'',
	# 	'haha id': '',
	# 	'care id':'',
	# 	'love id':'',
	# 	'sad id': '',
	# 	'wow id': '',
	# 	}

	body = soup.find('body')
	allpost=body.select('div[class="du4w35lb k4urcfbm l9j0dhe7 sjgh65i0"]')

	print(len(allpost))
	for post in allpost:
		post_dict = {
			'poster': '',
			'post content': '',
			'post_share_link': '',
			'comment number': '',
			'reaction':'',
			'comment': comment_dict_list
		}
		# PO 文者 ID
		# poster = post.select('div[class="lzcic4wl"]')[0].get('aria-labelledby')
		# poster=post.select('h2[id={}]'.format(str(poster)))
		# # print(poster)
		# pattern = r'<span>(\w+)</span>'
		# poster = re.search(pattern, 'r'+str(poster))
		# # print(poster.group(1)) PO文者ID
		# post_dict['poster']=poster.group(1)
		# #五個標籤名 PO文資訊   label_str
		# label_str = post.select('div[class="lzcic4wl"]')[0].get('aria-describedby')
		# pattern=r'\w{3}_\w{1}_\w{2}'
		# label_list=re.findall(pattern,str(label_str))
		# if (len(label_list)!=0):
		# 	label_list.pop(0)
		# 	label_list.pop(2)
		# 	for index,label in enumerate(label_list):
		# 		pass
		# 		post_content=post.select('div[id={}]'.format(label))
		# 		if index==0:
		# 			# PO文內容處理
		# 			pattern=r'>(.*?)<'
		# 			content_list1=re.findall(pattern,str(post_content))
		# 			content=''.join([str(x) for x in content_list1])
		# 			# print(content)
		# 			post_dict['post content']=content
		# 		if index==1:
		# 			pattern = r'href="(.*?)"'
		# 			# content 分享連結list
		# 			share_link=re.findall(pattern,str(post_content))
		# 			# print(share_link)
		# 			post_dict['post_share_link']=share_link
		# 			pass
		# 		if index==2:
		# 			pattern=r'>(\d+?) Comments<'
		# 			comment_num=re.findall(pattern,str(post_content))
		# 			# comment_num0 為 PO文底下留言數量
		# 			if len(comment_num)!=0:
		# 				post_dict['comment number']=comment_num[0]
		# 			else:
		# 				post_dict['comment number']=0
		# 		print(post_dict)
		# comment
		comment_labellist=['div[class="l9j0dhe7 ecm0bbzt hv4rvrfc qt6c0cv9 dati1w0a lzcic4wl btwxx1t3 j83agx80"]',
						   'div[class="kvgmc6g5 jb3vyjys rz4wbd8a qt6c0cv9 d0szoon8"]']
		for index,label in enumerate(comment_labellist):
			if index==0:
				# 主留言
				allcomment = post.select(label)
				for comment in allcomment:
					try:
						pattern=r'div aria-label="Comment by (.*?) '
						pattern_content = r'>(.*?)<'
						comment_main=re.findall(pattern,str(comment))
						comment_main_content_list=re.findall(pattern_content,str(comment))
						comment_main_content=''.join([str(x) for x in comment_main_content_list])
						print(comment_main)
						pattern2=r'{}(Author)?(.+?)\d?\s·'.format(comment_main[0])
						comment_main_content2=re.findall(pattern2,comment_main_content)[0][1]
						print('content:{}'.format(comment_main_content2))
					except:
						print("FAIL 1 STAGE")
						# print(comment_main_content)
			if index ==1:
				# 留言下的留言
				allcomment_comment = post.select(label)

				for comment_below in allcomment_comment:
					pattern = r'Reply by (.*?) '
					comment_below_name_list=re.findall(pattern,str(comment_below))
					print('comment_below_name:{}'.format(comment_below_name_list))
					for index,comment_below_name in enumerate(comment_below_name_list):
						try:
							comment_below2=comment_below.select('div[class="_6cuy"]')[index]
							pattern_below_content = r'>(.*?)<'
							comment_below_content_list1 = re.findall(pattern_below_content, str(comment_below2))
							comment_below_content = ''.join([str(x) for x in comment_below_content_list1])
							pattern2 =r'{}(Author)?(.*)'.format(comment_below_name)
							comment_below_content2=re.findall(pattern2,comment_below_content)[0][1]
							# comment_below_content2=re.findall(pattern_below_content,comment_below2)
							print('comment_below_content:{}'.format(comment_below_content2))
						except:
							print("FAIL 2 STAGE")
							comment_below_content2=[]



		# dataset.append(post_dict)




	# print(dataset)




def get_emoji_list():
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
	click_more_comment(driver=driver)
	# click_more_content(driver=driver)
	htmltext = driver.page_source
	#
	make_post_dict(html_doc=htmltext)