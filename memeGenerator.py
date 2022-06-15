from Phase1.MemeTextGenerator import MemeTextGenerator
from Phase2.imageCraw import get_image_ndarray
from Phase3.main import putcaptions
import random
import os

def remove_file(name):
	if os.path.exists(name):
		os.remove(name)

def memeGenerator(chinese_str:str, keyword:list or str = None,negative_keyword:list or str = None, img_id:str = '0'):
	generator = MemeTextGenerator('Phase1/vocabulary3000.txt')
	result = generator.generate(chinese_str)
	if result == None:
		generator = MemeTextGenerator('Phase1/vocabulary7000.txt')
		result = generator.generate(chinese_str)
	if result == None:
		print("單字庫無匹配單字")
		return
	index = random.randint(0, len(result[0]) - 1)
	img_arr = get_image_ndarray(result[1][index], keyword, negative_keyword, img_id)
	putcaptions(result[0][index], img_arr, img_id)	
	img_names = ['phase2_' + img_id + '.jpg', './phase3_tmp_' + img_id + '.png']
	for name in img_names:
		remove_file(name)

if __name__ == '__main__':
	chinese_str = u'有備而來'
	keyword = u'卡通'
	negative_keyword = u'背景'
	memeGenerator(chinese_str, keyword, negative_keyword)