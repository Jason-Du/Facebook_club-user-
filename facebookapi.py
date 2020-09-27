import json
import download as d
import os

def get_json_from_cloud():
	d.main(is_download_file_function=bool(True), download_drive_service_name='dataset.json', download_file_path=os.getcwd() + '/')
	with open('dataset.json', 'r', encoding='utf-8') as f:
		dataset = json.load(f)
	return dataset
def get_user_id(dataset):
	'''
	:param dataset:dataset file from get_json_from_cloud
	:return: List for Facebook Club user id
	'''
	return dataset['member_info']

def show_all_post(dataset):
	"""
	Show the content of all post
	:param dataset:dataset file from get_json_from_cloud
	"""
	for index, comment in enumerate(dataset['post_info']):
		print('post id:{}'.format(index))
		print(dataset['post_info'][index])


def get_post_by_post_id(dataset, post_id):
	'''
	:param dataset:
	:param post_id:
	:return: Dict ;the specific post info according to the post id
	'''
	return dataset['post_info'][post_id]



def show_all_comments_by_post_id(dataset, post_id):
	'''
	:param dataset: dataset file from get_json_from_cloud
	:param post_id:
	:return: NONE
	'''
	for index, comment in enumerate(dataset['post_info'][post_id]['comment']):
		print('post id :{} comment id:{}'.format(post_id, index))
		print(comment)


def get_comment_by_post_id_comment_id(dataset, post_id, comment_id):
	'''

	:param dataset:
	:param post_id:
	:return: List ;the comment list according to the post id
	'''
	return dataset['post_info'][post_id]['comment'][comment_id]


def show_all_comments_below_by_post_id_comment_id(dataset, post_id, comment_id):
	"""

	:param dataset:
	:param post_id:
	:param comment_id:
	:return: NONE
	"""
	for index, comment_below in enumerate(dataset['post_info'][post_id]['comment'][comment_id]['comment_below']):
		print('Post id {}  comment id:{}  comment below id:{}'.format(post_id, comment_id, index))
		print(comment_below)


def get_comment_below_by_post_id_comment_id_comment_below_id(dataset, post_id, comment_id, comment_below_id):
	"""

	:param dataset:
	:param post_id:
	:param comment_id:
	:param comment_below_id:
	:return: DICT;dict according to postid commentid commentbelowid
	"""
	return dataset['post_info'][post_id]['comment'][comment_id]['comment_below'][comment_below_id]


## { id: xxxx,
##   author_id:xxxx,
##   data:{
##   }
## }

if __name__ == '__main__':
	pass
	dataset = get_json_from_cloud()
	# print(get_user_id(dataset=dataset))


	# show_all_post(dataset)
	#
	#
	# print('------------')
	#
	#
	# test=get_post_by_post_id(dataset=dataset,post_id=2)
	#
	#
	# print(test)

	show_all_comments_by_post_id(dataset=dataset,post_id=4)
	# print('------------------')
	# test=get_comment_by_post_id_comment_id(dataset=dataset,post_id=2,comment_id=5)
	# print(test)


	# show_all_comments_below_by_post_id_comment_id(dataset=dataset,post_id=3,comment_id=6)
	# print('------------------')
	# test=get_comment_below_by_post_id_comment_id_comment_below_id(dataset=dataset,post_id=3,comment_id=6,comment_below_id=0)
	# print(test)
