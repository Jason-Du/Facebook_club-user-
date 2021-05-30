import json
import upload
import os
import re
import time
import facebookapi as fbapi


def save_json_file_for_fine_dataset():
    scratch_time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    time_pattern = r'\d{4}-(\d{2})-(\d{2})(\s)(\d{2}):(\d{2}):\d{2}'
    time_list = re.findall(time_pattern, scratch_time)[0]
    finishtime = str(time_list[0] + time_list[1])
    dataset = fbapi.get_json_from_cloud(date=finishtime)
    # single_post_info= fbapi.get_posts_by_post_id(dataset=dataset, post_id=2)
    # print(single_post_info)
    # userid_list = fbapi.get_all_user_ids(dataset)
    # print(userid_list)
    # post_list = fbapi.get_all_posts_by_type(dataset=dataset, type='Q&A')
    # print(post_list)
    # comment_list = fbapi.get_all_main_comments_by_post_id_user_id(dataset=dataset, post_id=1, user_id='Nicolas Hei')
    # print(comment_list)
    # comment_list=fbapi.get_all_below_comments_by_post_id_user_id(dataset=dataset, post_id=1, user_id='Nicolas Hei')
    # print(comment_list)
    # emoji_list = fbapi.get_post_emojis_by_post_id(dataset=dataset, post_id=1)
    # print(emoji_list)
    user_emojitimes = fbapi.get_all_posts_emojis_times_by_user_id(dataset=dataset, user_id='沈姵昕')
    print(user_emojitimes)
    data = fbapi.get_all_posts_all_user_comments_times(dataset=dataset)
    print(data)
    allemojitimes = fbapi.get_user_emoji_times_by_user_id(dataset=dataset, user_id='沈姵昕')
    print(allemojitimes)
    if (allemojitimes['LIKE'] > 76 and user_emojitimes['LIKE']>33):
        with open('fine_dataset.json', 'r', encoding='utf-8') as f:
            date_list = json.load(f)
        date_list.append(finishtime)
        with open('fine_dataset.json', 'w') as fp:
            json.dump(date_list, fp,indent=4)
    else:
        print("data : {} is fail".format(finishtime))

if __name__ == '__main__':
    save_json_file_for_fine_dataset()
    upload.main(is_update_file_function=bool(True), update_drive_service_name='fine_dataset.json',update_file_path=os.getcwd() + '/')