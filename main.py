from os import listdir, mkdir
from random import randint
from PIL import Image
import datetime
import argparse
import sys

def main(namespace):
	count_result = namespace.count
	path_input = namespace.input
	path_output = namespace.output
	path_output_gen = path_output + '/' + str(datetime.datetime.now())

	try:
		layers = (listdir(path_input))
	except:
		sys.exit("ERROR: input folder does not exist")
	layers.sort()
	list_images = []

	#getting .png file list from directors
	for i in layers:
			list_temp = (listdir(path_input + '/' + i))
			j = 0
			while j < len(list_temp):
				if not(list_temp[j].endswith(".png")):
					del list_temp[j]
					j = j - 1
				else:
					list_temp[j] = path_input + '/' + i + '/' + list_temp[j]
				j += 1
			list_images.append(list_temp)

	try:
		mkdir(path_output_gen)
	except:
		mkdir(path_output)
		mkdir(path_output_gen)

	count = 0
	#creating a set of layers in a single file
	while count < count_result:
		list_random_images = []
		#getting a random file from each layer
		for i in list_images:
			random_png = (i[randint(0,len(i)-1)])
			list_random_images.append(random_png)
		#layer creation background
		img_bg = Image.open(list_random_images[0]).convert("RGBA")
		x, y = img_bg.size
		#overlaying the next layers on the background
		for i in list_random_images:
			temp = Image.open(i).convert("RGBA")
			img_bg.paste(temp, (0, 0, x, y), temp)
		#save result file
		img_bg.save(path_output_gen + '/' + str(count) + ".png", format="png")
		count += 1
	print (str(count_result) + " images generated to PATH ./" + path_output_gen + "/")

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-c', '--count', default=5, type=int)
    parser.add_argument ('-i', '--input', default='img_input', type=str)
    parser.add_argument ('-o', '--output', default='img_output', type=str)
    return parser

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    print(
    	'set',
    	'--count',namespace.count, '(number of images to generate)',
			'--input',namespace.input, '(input folder with folders-layers containing .png files)',
    	'--output', namespace.output, '(output generated image folder)'
    	)
    main(namespace)
