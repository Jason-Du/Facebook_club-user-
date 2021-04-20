import json
import upload
import os
import re
import time
def save_json_file_for_fine_dataset():
    date_list = ["0322","0420"]
    # scratch_time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # time_pattern = r'\d{4}-(\d{2})-(\d{2})(\s)(\d{2}):(\d{2}):\d{2}'
    # time_list = re.findall(time_pattern, scratch_time)[0]
    # finishtime = str(time_list[0] + time_list[1])
    # date_list.append(finishtime)
    with open('fine_dataset.json', 'w') as fp:
        json.dump(date_list, fp,indent=4)

if __name__ == '__main__':
    save_json_file_for_fine_dataset()
    upload.main(is_update_file_function=bool(True), update_drive_service_name='fine_dataset.json',update_file_path=os.getcwd() + '/')