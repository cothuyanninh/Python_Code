count_file_Word = 0
count_file_Pdf = 0
count_file_Txt = 0

import os, shutil

def counterFile():

	inputFileDir = 'C:\\Users\\vanquangcz\\Desktop\\python\\project\\data\\input'
	fileInInput = os.listdir(inputFileDir)

	for link_file in range(len(fileInInput)):
		link_temp1 = inputFileDir + '\\' + fileInInput[link_file]
		link_word  = inputFileDir + '\\word'
		link_pdf   = inputFileDir + '\\pdf'
		link_txt   = inputFileDir + '\\txt'
		if fileInInput[link_file].endswith('.pdf'):
			shutil.move(link_temp1, link_pdf)
		if fileInInput[link_file].endswith('.docx'):
			shutil.move(link_temp1, link_word)
		if fileInInput[link_file].endswith('.txt'):
			shutil.move(link_temp1, link_txt)
