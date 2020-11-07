import club_v3 as cl
import upload
import os
import re
import  time

if __name__ == '__main__':
	# USERNAME = "a00264487@yahoo.com.tw"
	# PASSWORD = "a00264478"
	# USERNAME = "dushiun@gmail.com"
	# PASSWORD = "jason870225"
	USERNAME = 'jason21125@yahoo.com.tw'
	PASSWORD = 'jason870213'
	LINK = 'https://www.facebook.com/groups/315124296585941'
	# https://www.facebook.com/groups/342191540266126
	# 'https://www.facebook.com/groups/315124296585941'
	driver = cl.set_up(
		USERNAME=USERNAME,
		PASSWORD=PASSWORD,
		LINK=LINK,
		scroling_times=11


	)

	cl.click_more_comment(driver=driver)

	cl.click_more_comment(driver=driver)

	cl.click_more_comment(driver=driver)

	cl.click_more_content(driver=driver)

	htmltext = driver.page_source

	postlist = cl.make_post_dict(html_doc=htmltext, driver=driver)

	memberlist=cl.get_club_member_list(LINK,driver=driver)

	announcement_list = cl.get_club_announcement_list(LINK=LINK, driver=driver)

	dataset=cl.make_dataset(post_info=postlist,member_info=memberlist,announcement_info=announcement_list)

	cl.save_json_file(dataset=dataset)
	scratch_time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
	time_pattern = r'\d{4}-(\d{2})-(\d{2})(\s)(\d{2}):(\d{2}):\d{2}'
	time_list = re.findall(time_pattern, scratch_time)[0]
	finishtime = str(time_list[0] + time_list[1])

	upload.main(is_update_file_function=bool(True), update_drive_service_name=finishtime+'.json',update_file_path=os.getcwd() + '/')