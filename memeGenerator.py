from Phase1.MemeTextGenerator import MemeTextGenerator
from Phase2.imageCraw import get_image_ndarray
from Phase3.main import putcaptions
import random
import os

def remove_file(name):
	if os.path.exists(name):
		os.remove(name)

def memeGenerator(chinese_str:str, keyword:list or str=None,negative_keyword:list or str=None):
	generator = MemeTextGenerator('Phase1/vocabulary3000.txt')
	result = generator.generate(chinese_str)
	index = random.randint(0, len(result[0]) - 1)
	img_arr = get_image_ndarray(result[1][index], keyword, negative_keyword)
	putcaptions(result[0][index], img_arr)	
	img_names = ["phase2.jpg", "my_image.png"]
	for name in img_names:
		remove_file(name)

if __name__ == '__main__':
	s = u'深藏不露'
	memeGenerator(s)