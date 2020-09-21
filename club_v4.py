import club_v3 as cl
import quickstart
import os



if __name__ == '__main__':
    USERNAME = "dushiun@gmail.com"
    PASSWORD = "jason870225"

    LINK = 'https://www.facebook.com/groups/315124296585941'
    # https://www.facebook.com/groups/342191540266126
    # 'https://www.facebook.com/groups/315124296585941'
    driver = cl.set_up(
        USERNAME=USERNAME,
        PASSWORD=PASSWORD,
        LINK=LINK,
        scroling_times=6

    )
    cl.click_more_comment(driver=driver)

    cl.click_more_comment(driver=driver)

    cl.click_more_content(driver=driver)

    htmltext = driver.page_source

    dataset = cl.make_post_dict(html_doc=htmltext, driver=driver)

    cl.save_json_file(dataset=dataset)

    quickstart.main(is_update_file_function=bool(True), update_drive_service_name='dataset.json',update_file_path=os.getcwd() + '/')