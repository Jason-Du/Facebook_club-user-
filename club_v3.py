from selenium import webdriver #從library中引入webdriver
from bs4 import BeautifulSoup
import pandas as pd
import os
import time
import re
import json
import random

def click_more_comment(driver):
	pass
	post=driver.find_elements_by_xpath("//div[@class='du4w35lb k4urcfbm l9j0dhe7 sjgh65i0']")
	print("CLICK MORE COMMENT ON GOING")
	print("POST NUMBER:{}".format(len(post)))
	# cookie test##########################################
	# driver.delete_all_cookies()
	# time.sleep(2)
	# lst = driver.get_cookies()
	# for cookie in lst:
	# 	print(cookie)
	# cookie test##########################################
	for i in post:
		try:
			driver.execute_script("arguments[0].scrollIntoView(false);", i)
			time.sleep(2)
			more_comment=i.find_elements_by_xpath('.//div[@class="oajrlxb2 bp9cbjyn g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 '
												  'rq0escxv nhd2j8a9 pq6dq46d mg4g778l btwxx1t3 g5gj957u p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys p8fzw8mz qt6c0cv9 a8nywdso '
												  'l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh gpro0wi8 m9osqain buofh1pr"]'
												  )
			for j in more_comment:
				try:
					driver.execute_script("arguments[0].scrollIntoView(false);",j)
					time.sleep(2)
					j.click()
					time.sleep(2)
				except:
					print("FAIL CLICK more_comment")
		except:
			print("NO more_comment BUTTON")
			pass
			# print("FAIL FIND LOCATION")



def click_more_content(driver):
	post = driver.find_elements_by_xpath("//div[@class='du4w35lb k4urcfbm l9j0dhe7 sjgh65i0']")
	print("CLICK MORE CONTENT ON GOING")
	print("POST NUMBER:{}".format(len(post)))
	for i in post:
		try:
			driver.execute_script("arguments[0].scrollIntoView(false);", i)
			time.sleep(2)
			more_content = i.find_elements_by_xpath('.//div[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv'
												   ' nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 '
												   'a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p"]')
			for j in more_content:
				try:
					driver.execute_script("arguments[0].scrollIntoView(false);",j)
					time.sleep(2)
					j.click()
					time.sleep(2)
				except:
					print("FAIL CLICK more_content BUTTON")
		except:

			print("NO more_content BUTTON")
			pass
#
def make_post_dict(html_doc,driver):
	soup = BeautifulSoup(html_doc, 'html.parser')
	dataset = []


	body = soup.find('body')
	allpost=body.select('div[class="du4w35lb k4urcfbm l9j0dhe7 sjgh65i0"]')
	real_index_post=0
	print(len(allpost))
	for index_post,post in enumerate(allpost):
		print('POST:{} IS ON GOING'.format(real_index_post))
		comment_dict_list = []
		reaction_list=[]
		post_dict = {
			'post_id':'',
			'poster': '',
			'post_content': '',
			'post_share_link': '',
			'comment_number': '',
			'comment': comment_dict_list,
			'reaction':reaction_list
		}
		# PO 文者 ID
		poster = post.select('div[class="lzcic4wl"]')[0].get('aria-labelledby')
		try:
			poster=post.select('h2[id={}]'.format(str(poster)))[0].select('div[class="nc684nl6"]')
		except:
			print('post num{} is not a post discard it and jump to next post'.format(real_index_post))
			real_index_post = real_index_post
			continue
		pattern = r'>(.*?)<'
		poster_list = re.findall(pattern,str(poster))
		poster_name=''.join([str(x) for x in poster_list])
		# print(poster_name)
		# PO文者ID
		post_dict['post_id']=real_index_post
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
		#  DEBUG
		# 主留言 l9j0dhe7 ecm0bbzt hv4rvrfc qt6c0cv9 dati1w0a lzcic4wl btwxx1t3 j83agx80

		# 1001 主留言 l9j0dhe7 ecm0bbzt hv4rvrfc qt6c0cv9 dati1w0a j83agx80 btwxx1t3 lzcic4wl

		# 1030 主留言 l9j0dhe7 ecm0bbzt rz4wbd8a qt6c0cv9 dati1w0a j83agx80 btwxx1t3 lzcic4wl
		#
		comment_labellist=['div[class="l9j0dhe7 ecm0bbzt rz4wbd8a qt6c0cv9 dati1w0a j83agx80 btwxx1t3 lzcic4wl"]',
						   'div[class="kvgmc6g5 jb3vyjys rz4wbd8a qt6c0cv9 d0szoon8"]']
		for index_label,label in enumerate(comment_labellist):

			if index_label==0:
				# print('debug stage1')
				# 主留言
				allcomment = post.select(label)
				for comment_main_index,comment in enumerate(allcomment):

					comment_dict = {
						'comment_id': '',
						'comment_content': '',
						'comment_link_num': '',
						'comment_gif_num': '',
						'comment_img_num': '',
						'comment_sticker': '',
						'comment_below': '',
						'comment_reaction': [],
					}
					# comment 為 單個的主流言
					# print('debug stage2')
					try:

						pass
						# 抓取留言者姓名
						comment_main_name_path = comment.select('span[class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb mdeji52x e9vueds3 j5wam9gi lrazzd5p oo9gr5id"]')
						pattern=r'>(.*?)<'
						pattern_content = r'>(.*?)<'
						comment_main=re.findall(pattern,str(comment_main_name_path))
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
					# l9j0dhe7 ecm0bbzt hv4rvrfc qt6c0cv9 dati1w0a j83agx80 btwxx1t3 lzcic4wl
					# l9j0dhe7 ecm0bbzt hv4rvrfc qt6c0cv9 dati1w0a lzcic4wl btwxx1t3 j83agx80
					# l9j0dhe7 ecm0bbzt rz4wbd8a qt6c0cv9 dati1w0a j83agx80 btwxx1t3 lzcic4wl
					comment_main_reaction_list=get_comment_emoji_list(driver=driver,
																	  mode=1,
																	  post_index=real_index_post,
																	  comment_segment_path='.//div[@class="l9j0dhe7 ecm0bbzt rz4wbd8a qt6c0cv9 dati1w0a j83agx80 btwxx1t3 lzcic4wl"]',
																	  comment_segment_index=comment_main_index,
																	  comment_below_segment_path='',
																	  comment_below_segment_index=''
																	  )
					comment_dict['comment_reaction']=comment_main_reaction_list
					comment_dict_list.append(comment_dict)
					# print('debug comment_dict_list'.format(comment_dict_list))
					# 列印出主留言
					# print(comment_dict_list[comment_main_index])
					# print('--------------------------------------------------------')

			if index_label==1:

				# 留言下的留言區塊
				allcomment_comment = post.select(label)
				for index_dict,comment_below in enumerate(allcomment_comment):

					comment_below_dict_list = []
					pattern = r'Reply by (.*?) to'
					comment_below_name_list=re.findall(pattern,str(comment_below))


					# print('comment_below_name:{}'.format(comment_below_name_list))
				# 	留言下的single留言區塊 姓名
					for index_below,comment_below_name in enumerate(comment_below_name_list):
						comment_below_dict = {'comment_id':'',
											  'comment_content':'',
											  'comment_link_num':'',
											  'comment_gif_num':'',
											  'comment_img_num':'',
											  'comment_sticker':'',
											  'comment_reaction':[]
											  }
						comment_below_dict['comment_id'] = comment_below_name
				# 		#留言下的single留言區塊 下的留言區塊 debug
				# 	09	l9j0dhe7 ecm0bbzt hv4rvrfc qt6c0cv9 scb9dxdr lzcic4wl btwxx1t3 j83agx80
				#  1001 l9j0dhe7 ecm0bbzt hv4rvrfc qt6c0cv9 scb9dxdr j83agx80 btwxx1t3 lzcic4wl
				#  1030 l9j0dhe7 ecm0bbzt rz4wbd8a qt6c0cv9 scb9dxdr j83agx80 btwxx1t3 lzcic4wl
						comment_below2 = comment_below.select('div[class="l9j0dhe7 ecm0bbzt rz4wbd8a qt6c0cv9 scb9dxdr j83agx80 btwxx1t3 lzcic4wl"]')[index_below]
						# print('debug index below comment{} comment_below2 {}'.format(index_below,comment_below2))
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
						comment_below_reaction_list = get_comment_emoji_list(driver=driver,
																			mode=2,
																			post_index=real_index_post,
																			comment_segment_path='.//div[@class="l9j0dhe7 ecm0bbzt rz4wbd8a qt6c0cv9 scb9dxdr j83agx80 btwxx1t3 lzcic4wl"]',
																			comment_segment_index=index_below,
																			comment_below_segment_path='.//div[@class="kvgmc6g5 jb3vyjys rz4wbd8a qt6c0cv9 d0szoon8"]',
																			comment_below_segment_index=index_dict
																			)
																							# 'div[class="kvgmc6g5 jb3vyjys rz4wbd8a qt6c0cv9 d0szoon8"]'
						comment_below_dict['comment_reaction']=comment_below_reaction_list
						comment_below_dict_list.append(comment_below_dict)


					print('debug index_dict{}'.format(index_dict))
					comment_dict_list[index_dict]['comment_below']=comment_below_dict_list
					# # 列印出該則PO文底下的所有留言
					# print(comment_dict_list[index_dict])

				# print('*************************************')


					# print(comment_dict_list[index_dict])

		post_dict['comment']=comment_dict_list
		# 列印出該則PO文底下的所有留言以及PO文
		# print(post_dict)



		# -------------------------------------------------------------------GETTING EMOJI-----------------------------------------------------
		reaction_list=get_post_emoji_list(driver=driver, post_index=real_index_post)
		post_dict['reaction']=reaction_list
		dataset.append(post_dict)
		# print(dataset[index_post]['reaction'])
		# os.system('pause')
		print(dataset[real_index_post])
		real_index_post=real_index_post+1
		# os.system('pause')
	# print(dataset)
	# 	print(dataset[index_post]['comment'])
	return dataset

def emoji_data_dealing(emoji_dict_list,driver):
	# 點開EMOJI視窗後使用beautifulsoup 解析
	emoji_htmltxt = driver.page_source
	soup_emoji = BeautifulSoup(emoji_htmltxt, 'html.parser')

	emoji_window = soup_emoji.select('div[class="l9j0dhe7 tkr6xdv7"]')[0]

	# 單一EMOJI USER 區塊
	emoji_individual_row = emoji_window.select('div[data-visualcompletion="ignore-dynamic"]')
	for row in emoji_individual_row:
		emoji_dict = {'emoji_id': '',
					  'emoji_type': ''
					  }
		# label1 為選取姓名區塊   label2為選取表情符號區塊
		emoji_label_list = ['div[class="q9uorilb"]', 'img[class="hu5pjgll bixrwtb6"]']

		for emoji_label_index, emoji_label in enumerate(emoji_label_list):
			try:
				print("emoji deal label:{}".format(emoji_label_index))
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
#1029 debug for clicking close button fail thus twice click
	try:
		close_button = driver.find_elements_by_xpath('//div[@class="oajrlxb2 tdjehn4e qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn s45kfl79 emlxlaya bkmhp75w spb7xbtv rt8b4zig n8ej3o3l agehan2d sk4xxmp2 taijpn5t tv7at329 thwo4zme"]')[0]
		close_button.click()

		time.sleep(random.randint(2, 4))
	except:
		print(" debug FAIL FINDIND BUTTON")
		# close_button = driver.find_elements_by_xpath('//div[@class="oajrlxb2 tdjehn4e qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn s45kfl79 emlxlaya bkmhp75w spb7xbtv rt8b4zig n8ej3o3l agehan2d sk4xxmp2 taijpn5t tv7at329 thwo4zme"]')[0]

	return emoji_dict_list





def get_post_emoji_list(driver, post_index):
	emoji_dict_list=[]
	try:
		post = driver.find_elements_by_xpath("//div[@class='du4w35lb k4urcfbm l9j0dhe7 sjgh65i0']")[post_index]
		driver.execute_script("arguments[0].scrollIntoView(false);", post)
		time.sleep(2)
		emoji_button=post.find_elements_by_xpath('.//div[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 a8c37x1j p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l gmql0nx0 ce9h75a5 ni8dbmo4 stjgntxs"]')[0]
		driver.execute_script("arguments[0].scrollIntoView(false);", emoji_button)
		try:
			time.sleep(2)
			emoji_button.click()

			time.sleep(2)
		except:
			print("FAIL CLICK POST EMOJI BUTTON")
	except:
		# print("NO POST EMOJI BUTTOM")
		pass
	else:
		emoji_dict_list=emoji_data_dealing(emoji_dict_list=emoji_dict_list,driver=driver)
	return emoji_dict_list




def get_comment_emoji_list(mode,driver,post_index,comment_below_segment_path,comment_below_segment_index,comment_segment_path,comment_segment_index):
	emoji_dict_list = []
	try:
		post = driver.find_elements_by_xpath("//div[@class='du4w35lb k4urcfbm l9j0dhe7 sjgh65i0']")[post_index]
		driver.execute_script("arguments[0].scrollIntoView(false);", post)
		time.sleep(2)
		if mode==1:
			# 主留言
			comment_emoji_stage1 = post.find_elements_by_xpath(comment_segment_path)[comment_segment_index]
		else:
			# 留言下的留言區塊分區
			comment_segment0=post.find_elements_by_xpath(comment_below_segment_path)[comment_below_segment_index]

			driver.execute_script("arguments[0].scrollIntoView(false);", comment_segment0)
			time.sleep(2)
			# 留言下的留言INDEX
			comment_emoji_stage1=comment_segment0.find_elements_by_xpath(comment_segment_path)[comment_segment_index]

		driver.execute_script("arguments[0].scrollIntoView(false);", comment_emoji_stage1)
		time.sleep(2)
		# 預防出現連結 造成emoji class 位置不同
		try:
			comment_emoji_stage2 = comment_emoji_stage1.find_elements_by_xpath(".//div[@class='_6cuq _680_']")[0]

		except:
			comment_emoji_stage2 = comment_emoji_stage1.find_elements_by_xpath(".//div[@class='_6cuq']")[0]

		driver.execute_script("arguments[0].scrollIntoView(false);", comment_emoji_stage2)
		time.sleep(2)
		# emoji button 位置
		emoji_button=comment_emoji_stage2.find_elements_by_xpath(".//span[@class='tojvnm2t a6sixzi8 abs2jz4q a8s20v7p t1p8iaqh k5wvi7nf q3lfd5jv pk4s997a bipmatt0 cebpdrjk qowsmv63 owwhemhu dp1hu0rb dhp61c6y iyyx5f41']")[0]
		# 																		=
		driver.execute_script("arguments[0].scrollIntoView(false);", emoji_button)
		# print('emojitest2')
		try:
			time.sleep(2)
			emoji_button.click()
			time.sleep(2)
		except:
			print("FAIL CLICK COMMENT EMOJI BUTTON")
	except:
		# print("NO COMMENT EMOJI BUTTON")
		pass
	else:
		print("debug postindex {}    comment_segment_index {} ".format(post_index,comment_segment_index))
		emoji_dict_list=emoji_data_dealing(emoji_dict_list=emoji_dict_list,driver=driver)
	return emoji_dict_list

def set_up(USERNAME,PASSWORD,LINK,scroling_times):
	pass
	profile = webdriver.FirefoxProfile()# 新增firefox的設定
	# DEBUG 新增設定 清除CACHE
	profile.set_preference("browser.cache.disk.enable", False)
	profile.set_preference("browser.cache.memory.enable", False)
	profile.set_preference("browser.cache.offline.enable", False)
	profile.set_preference("network.http.use-cache", False)
	profile.set_preference("network.dns.disableIPv6", True)
	profile.set_preference("dom.webnotifications.enabled", False)# 將頁面通知關掉
	profile.update_preferences()# 需要再更新目前firefox新的偏好設定
	driver = webdriver.Firefox(firefox_profile=profile)
	# options = webdriver.ChromeOptions()
	# prefs = {'profile.default_content_settings.popups': 0}
	# options.add_experimental_option('prefs', prefs)
	# options.add_argument("--disable-extensions")
	# options.add_argument("--disable-notifications")
	# # // to	disable	browser	extension	popup
	# driver = webdriver.Chrome(chrome_options=options)

	driver.get("http://www.facebook.com")
	time.sleep(2)
	driver.find_element_by_id("email").send_keys(USERNAME) # 將USERNAME改為你的臉書帳號
	driver.find_element_by_id("pass").send_keys(PASSWORD) # 將PASSWORD改為你的臉書密碼
	try:
		# driver.find_element_by_id("u_0_d_aK").click()
		python_button=driver.find_elements_by_xpath("//*[@class='_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy']")[0]
		# python_button=driver.find_element_by_class_name('_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy')
		# time.sleep(1)
		print(python_button)
		python_button.click()
	except:
		print("LOGIN BUTTON FAIL")
		os.system("pause")
		# driver.find_element_by_id("u_0_d_51").click()
	time.sleep(2)
	driver.get(LINK)
	time.sleep(3)
	for i in range(scroling_times):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(2)
	return driver

def save_json_file(dataset):
	scratch_time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
	time_pattern = r'\d{4}-(\d{2})-(\d{2})(\s)(\d{2}):(\d{2}):\d{2}'
	time_list = re.findall(time_pattern, scratch_time)[0]
	finishtime = str(time_list[0] + time_list[1])
	print(finishtime)
	with open(finishtime+'.json', 'w') as fp:
		json.dump(dataset, fp,indent=4)

def get_club_member_list(LINK,driver):
	# 抓取社團名單
	time.sleep(2)
	driver.get(LINK+'/members')
	time.sleep(2)
	for i in range(8):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(2)

	html_doc = driver.page_source
	memberlist=[]
	soup = BeautifulSoup(html_doc, 'html.parser')
	body = soup.find('body')
	# 選取member區段
	member_list_section = body.select('div[class="b20td4e0 muag1w35"]')[4]
	member_row=member_list_section.select('div[data-visualcompletion="ignore-dynamic"]')
	for single_member_row in member_row:
		member_name=single_member_row.select('a[class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 '
								 'nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso '
								 'i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p"]')
		pattern=r'>(.*?)<'
		member_name=re.findall(pattern,str(member_name))[0]
		memberlist.append(member_name)
	return memberlist
	pass
def get_club_announcement_list(LINK,driver):
	# 抓取社團名單
	time.sleep(2)
	driver.get(LINK+'/announcements')
	time.sleep(2)
	for i in range(5):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(2)
	click_more_comment(driver=driver)

	click_more_comment(driver=driver)

	click_more_content(driver=driver)

	click_more_content(driver=driver)

	htmltext = driver.page_source

	post_info=make_post_dict(html_doc=htmltext,driver=driver)

	return post_info
	pass
def make_dataset(post_info,member_info,announcement_info):
	dataset={'post_info':[],
			 'member_info':[],
			 'announcement_info':[]

	}
	dataset['post_info']=post_info
	dataset['member_info']=member_info
	dataset['announcement_info']=announcement_info
	return dataset


if __name__ == '__main__':

	USERNAME = "dushiun@gmail.com"
	PASSWORD = "jason870225"
	# USERNAME = 'jason21125@yahoo.com.tw'
	# PASSWORD = 'jason870213'


	LINK='https://www.facebook.com/groups/342191540266126'
	# https://www.facebook.com/groups/342191540266126
	# 'https://www.facebook.com/groups/315124296585941'
	# https://www.facebook.com/groups/315124296585941/members

	driver=set_up(
		USERNAME=USERNAME,
		PASSWORD=PASSWORD,
		LINK=LINK,
		scroling_times=2

	)
	click_more_comment(driver=driver)
	#

	#
	click_more_content(driver=driver)
	#
	htmltext = driver.page_source

	post_info=make_post_dict(html_doc=htmltext,driver=driver)
	print(post_info)

	# memberlist=get_club_member_list(LINK,driver=driver)
	# print(memberlist)
	#
	# announcement_list=get_club_announcement_list(LINK=LINK,driver=driver)

	# make_dataset(post_info=post_info,member_info=memberlist,announcement_info=announcement_list)
	# print(announcement_list)

	# save_json_file(dataset=dataset)



