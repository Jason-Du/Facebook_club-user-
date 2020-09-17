from selenium import webdriver #從library中引入webdriver
from bs4 import BeautifulSoup
import pandas as pd
import os
import time
import re
import json

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
						driver.execute_script("arguments[0].scrollIntoView(false);",j)
						time.sleep(1)
						j.click()
					except:
						print("FAIL CLICK")
			except:
				print("FAIL FIND LOCATION")
		except:
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
def make_post_dict(html_doc,driver):
	soup = BeautifulSoup(html_doc, 'html.parser')
	dataset = []

	body = soup.find('body')
	allpost=body.select('div[class="du4w35lb k4urcfbm l9j0dhe7 sjgh65i0"]')

	print(len(allpost))
	for index_post,post in enumerate(allpost):
		print('POST:{} IS ON GOING'.format(index_post))
		comment_dict_list = []
		reaction_list=[]
		post_dict = {
			'poster': '',
			'post_content': '',
			'post_share_link': '',
			'comment_number': '',
			'comment': comment_dict_list,
			'reaction':reaction_list
		}
		# PO 文者 ID
		poster = post.select('div[class="lzcic4wl"]')[0].get('aria-labelledby')
		poster=post.select('h2[id={}]'.format(str(poster)))[0].select('div[class="nc684nl6"]')
		pattern = r'>(.*?)<'
		poster_list = re.findall(pattern,str(poster))
		poster_name=''.join([str(x) for x in poster_list])
		# print(poster_name)
		# PO文者ID
		post_dict['poster']=poster_name
		#五個標籤名 PO文資訊   label_str
		label_str = post.select('div[class="lzcic4wl"]')[0].get('aria-describedby')
		pattern=r'\w{3}_\w{1}_\w{2}'
		label_list=re.findall(pattern,str(label_str))
		if (len(label_list)!=0):
			label_list.pop(0)
			label_list.pop(2)
			for index,label in enumerate(label_list):
				pass
				post_content=post.select('div[id={}]'.format(label))
				if index==0:
					# PO文內容處理
					pattern=r'>(.*?)<'
					content_list1=re.findall(pattern,str(post_content))
					content=''.join([str(x) for x in content_list1])
					# print(content)
					post_dict['post_content']=content
				if index==1:
					pattern = r'href="(.*?)"'
					# content 分享連結list
					share_link=re.findall(pattern,str(post_content))
					# print(share_link)
					post_dict['post_share_link']=share_link
					pass
				if index==2:
					pattern=r'>(\d+?) Comments<'
					comment_num=re.findall(pattern,str(post_content))
					# comment_num0 為 PO文底下留言數量
					if len(comment_num)!=0:
						post_dict['comment_number']=comment_num[0]
					else:
						post_dict['comment_number']=0
				# print(post_dict)



		# ----------------------------------------------------------Comment---------------------------------------------------------------------------
		# 主留言 與 留言下留言分類區塊
		comment_labellist=['div[class="l9j0dhe7 ecm0bbzt hv4rvrfc qt6c0cv9 dati1w0a lzcic4wl btwxx1t3 j83agx80"]',
						   'div[class="kvgmc6g5 jb3vyjys rz4wbd8a qt6c0cv9 d0szoon8"]']
		for index_label,label in enumerate(comment_labellist):
			if index_label==0:
				# 主留言
				allcomment = post.select(label)
				for comment in allcomment:

					comment_dict = {
						'comment_id': '',
						'comment_content': '',
						'comment_link_num': '',
						'comment_gif_num': '',
						'comment_img_num': '',
						'comment_sticker': '',
						'comment_below': '',
					}
					# comment 為 單個的主流言
					try:
						pass
						pattern = r'div aria-label="Comment by (.+?) '
						pattern_content = r'>(.*?)<'
						comment_main=re.findall(pattern,str(comment))
						# print("comment main name : {}".format(comment_main))

						#  處理留言區塊
						singlecomment=comment.select('div[class="kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql"]')
						comment_content_list1 = re.findall(pattern_content, str(singlecomment))
						comment_content = ''.join([str(x) for x in comment_content_list1])
						# print('comment_main content:{}'.format(comment_content))
						# SAVE TO DICT
						comment_dict['comment_id'] = comment_main[0]
						comment_dict['comment_content'] = comment_content

					except:
						pass
						print("FAIL 1 STAGE")
					try:
						# 處理關於流言有貼圖 link image gif
						pass
						singlecomment_link=comment.select('div[class="_6cuy"]')[0]

						gif1=singlecomment_link.select('img[class="a8c37x1j idiwt2bm d2edcug0"]')
						# print (len(gif1))

						gif2 = singlecomment_link.select('video[class="k4urcfbm datstx6m a8c37x1j"]')
						# print(len(gif2))

						photo = singlecomment_link.select("img[class='img']")
						# print(len(photo1))

						sharelink=singlecomment_link.select("a[class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl i09qtzwb n7fi1qx3 pmk7jnqg j9ispegn kr520xx4 dwzzwef6']")
						pattern=r'<div class="_6cuy"><div aria-label="(.*?)"'

						sticker_type=re.findall(pattern,str(singlecomment_link))
						if len(sticker_type)==0:
							sticker0=''
						else:
							sticker0=sticker_type[0]

						# print(sticker_type)
						# SAVE TO DICT

						comment_dict['comment_gif_num'] = len(gif1) + len(gif2)
						comment_dict['comment_img_num'] = len(photo)
						comment_dict['comment_link_num'] = len(sharelink)
						comment_dict['comment_sticker'] = sticker0

					except:
						print("LINK FAIL")
						pass
					comment_dict_list.append(comment_dict)
			if index_label ==1:
				# 留言下的留言區塊
				allcomment_comment = post.select(label)
				for index_dict,comment_below in enumerate(allcomment_comment):
					comment_below_dict_list = []
					pattern = r'Reply by (.+?) '
					comment_below_name_list=re.findall(pattern,str(comment_below))


					# print('comment_below_name:{}'.format(comment_below_name_list))
				# 	留言下的single留言區塊 姓名
					for index_below,comment_below_name in enumerate(comment_below_name_list):
						comment_below_dict = {'comment_id':'',
											  'comment_content':'',
											  'comment_link_num':'',
											  'comment_gif_num':'',
											  'comment_img_num':'',
											  'comment_sticker':''
											  }
						comment_below_dict['comment_id'] = comment_below_name
				# 		#留言下的single留言區塊 下的留言區塊
						comment_below2 = comment_below.select('div[class="l9j0dhe7 ecm0bbzt hv4rvrfc qt6c0cv9 scb9dxdr lzcic4wl btwxx1t3 j83agx80"]')[index_below]
						try:
							comment_below3=comment_below2.select('div[class="kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql"]')
							pattern_below_content = r'>(.*?)<'
							comment_below_content_list1 = re.findall(pattern_below_content, str(comment_below3))
							comment_below_content = ''.join([str(x) for x in comment_below_content_list1])
							# print('comment_below_content:{}'.format(comment_below_content))
							comment_below_dict['comment_content']=comment_below_content
						except:
							pass
							print("FAIL 2 STAGE")
						try:
							singlecomment_link = comment_below2.select('div[class="_6cuy"]')[0]
							gif1 = singlecomment_link.select('img[class="a8c37x1j idiwt2bm d2edcug0"]')
							# print(len(gif1))
							photo = singlecomment_link.select("img[class='img']")
							# print(len(photo))
							sharelink = singlecomment_link.select("a[class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl i09qtzwb n7fi1qx3 pmk7jnqg j9ispegn kr520xx4 dwzzwef6']")
							# print(len(sharelink))
							gif2 = singlecomment_link.select('video[class="k4urcfbm datstx6m a8c37x1j"]')
							# print(len(gif2))
							pattern = r'<div class="_6cuy"><div aria-label="(.*?)"'
							sticker_type = re.findall(pattern, str(singlecomment_link))
							if len(sticker_type) == 0:
								sticker0 = ''
							else:
								sticker0 = sticker_type[0]
							#
							# SAVE TO DICT
							comment_below_dict['comment_gif_num'] = len(gif1) + len(gif2)
							comment_below_dict['comment_img_num'] = len(photo)
							comment_below_dict['comment_link_num'] = len(sharelink)
							comment_below_dict['comment_sticker'] = str(sticker0)
							pass
						except:
							print("LINK FAIL 2 STAGE")
							pass
						comment_below_dict_list.append(comment_below_dict)
					comment_dict_list[index_dict]['comment_below']=comment_below_dict_list
					# 列印出該則PO文底下的所有留言

					# print(comment_dict_list[index_dict])

		post_dict['comment']=comment_dict_list
		# 列印出該則PO文底下的所有留言以及PO文
		# print(post_dict)



		# -------------------------------------------------------------------GETTING EMOJI-----------------------------------------------------
		reaction_list=get_emoji_list(driver=driver, post_index=index_post)
		post_dict['reaction']=reaction_list
		dataset.append(post_dict)
		print(dataset[index_post]['reaction'])
		# os.system('pause')
		# print(dataset[index_post])
		# os.system('pause')
	# print(dataset)
	return dataset

def emoji_data_dealing(emoji_dict_list):
	emoji_htmltxt = driver.page_source
	soup_emoji = BeautifulSoup(emoji_htmltxt, 'html.parser')

	emoji_window = soup_emoji.select('div[class="l9j0dhe7 tkr6xdv7"]')[0]

	emoji_individual_row = emoji_window.select('div[data-visualcompletion="ignore-dynamic"]')
	for row in emoji_individual_row:
		emoji_dict = {'emoji_id': '',
					  'emoji_type': ''
					  }
		# label1 為選取姓名區塊   label2為選取表情符號區塊
		emoji_label_list = ['div[class="q9uorilb"]', 'img[class="hu5pjgll bixrwtb6"]']

		for emoji_label_index, emoji_label in enumerate(emoji_label_list):
			try:
				emoji_stage1 = row.select(emoji_label)
				# print("SELECTING SUCCESS {}".format(emoji_label_index))
				if emoji_label_index == 0:
					name_pattern = r'>(.*?)<'
					emoji_name_list = re.findall(name_pattern, str(emoji_stage1))
					emoji_name = ''.join([str(x) for x in emoji_name_list])
					# print(emoji_name)
					emoji_dict['emoji_id'] = emoji_name

				if emoji_label_index == 1:
					label_response = {
						'https://static.xx.fbcdn.net/rsrc.php/v3/yv/r/dOJFaVZihS_.png': 'LIKE',
						'https://static.xx.fbcdn.net/rsrc.php/v3/yf/r/p_-PTXnrxIv.png': 'CARE',
						'https://static.xx.fbcdn.net/rsrc.php/v3/yP/r/dhZwLwMz9U7.png': 'SAD',
						'https://static.xx.fbcdn.net/rsrc.php/v3/yH/r/i6eZvvUMZW5.png': 'ANGRY',
						'https://static.xx.fbcdn.net/rsrc.php/v3/yj/r/yzxDz4ZUD49.png': 'HAHA',
						'https://static.xx.fbcdn.net/rsrc.php/v3/yn/r/qZOYbiV8BHS.png': 'WOW',
						'https://static.xx.fbcdn.net/rsrc.php/v3/yq/r/emi3_1IpGVz.png': 'LOVE',
					}
					type_pattern = r'src="(.*?)"'
					emoji_type2 = re.findall(type_pattern, str(emoji_stage1))[0]
					emoji_decode = label_response[str(emoji_type2)]
					# print(emoji_decode)
					emoji_dict['emoji_type'] = emoji_decode
			except:
				print("EMOGI STAGE - {}  FAIL".format(emoji_label_index + 1))

		emoji_dict_list.append(emoji_dict)
	close_button = driver.find_elements_by_xpath('//div[@class="oajrlxb2 tdjehn4e qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn s45kfl79 emlxlaya bkmhp75w spb7xbtv rt8b4zig n8ej3o3l agehan2d sk4xxmp2 taijpn5t tv7at329 thwo4zme"]')[0]
	close_button.click()
	return emoji_dict_list





def get_emoji_list(driver, post_index):
	emoji_dict_list=[]
	try:
		post = driver.find_elements_by_xpath("//div[@class='du4w35lb k4urcfbm l9j0dhe7 sjgh65i0']")[post_index]
		driver.execute_script("arguments[0].scrollIntoView(false);", post)
		emoji_button=post.find_elements_by_xpath('.//div[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 a8c37x1j p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l gmql0nx0 ce9h75a5 ni8dbmo4 stjgntxs"]')[0]
		driver.execute_script("arguments[0].scrollIntoView(false);", emoji_button)
		time.sleep(1)
		emoji_button.click()
		time.sleep(1)
	except:
		print("NO EMOJI BUTTOM")
		pass
	else:
		emoji_dict_list=emoji_data_dealing(emoji_dict_list=emoji_dict_list)
	return emoji_dict_list




def get_comment_emoji_list(driver,post_index):
	emoji_dict_list = []
	post = driver.find_elements_by_xpath("//div[@class='du4w35lb k4urcfbm l9j0dhe7 sjgh65i0']")[post_index]
	comment_labellist = ['.//div[class="l9j0dhe7 ecm0bbzt hv4rvrfc qt6c0cv9 dati1w0a lzcic4wl btwxx1t3 j83agx80"]',
						 './/div[class="kvgmc6g5 jb3vyjys rz4wbd8a qt6c0cv9 d0szoon8"]']
	for label_index,label in enumerate(comment_labellist):
		comment_segment=post.find_elements_by_xpath(label)[0]
		try:
			emoji_button=comment_segment.find_elements_by_xpath(".//div[class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l']")[0]
			emoji_button.click()

		except:
			print("NO EMOJI BUTTON")
		else:
			emoji_dict_list=emoji_data_dealing(emoji_dict_list=emoji_dict_list)
	return emoji_dict_list



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
	# https://www.facebook.com/groups/342191540266126
	# https://www.facebook.com/groups/315124296585941
	#
	time.sleep(2)
	post=5
	for i in range(post):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(2)
	# click_more_comment(driver=driver)
	# click_more_content(driver=driver)
	htmltext = driver.page_source
	#
	dataset=make_post_dict(html_doc=htmltext,driver=driver)

	# with open('result.json', 'w') as fp:
	# 	json.dump(dataset, fp)


