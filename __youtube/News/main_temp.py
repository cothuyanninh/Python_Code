import creat_audio
import creat_image
import os
import ast

def upload():
	minh = open('./file/content.txt', 'r').read()
	abc = ast.literal_eval(minh)
	b = abc['title']
	c = abc['comment']

	# start_days = dt.datetime(2018,thang,ngay,gio,00,00)
	# temp = 0
	# temp_days = 0

	# e = start_days.replace( month = thang ,day = ngay, minute = start_days.minute + temp ).isoformat() + '.0Z'
	a =  u'dm.py --file %s --title "%s" --description "%s"'%('1.mp4',b, c)
	# print(a)
	os.system(a)


def writeInput():
	# os.system('del video-input-list.txt')
	mm = open("video-input-list.txt", "w")
	a = os.listdir("./downloads")
	for i in range(len(a)):
		if (a[i][-3:] == "jpg"):
			mm.write("file './downloads/")
			mm.write(a[i])
			mm.write("\n")

def ReadingNews(link):

	json = creat_image.creat_image(link)

	with open("./file/content.txt", "w") as minh:
		minh.write(str(json))
		minh.write("\n")
	if (len(os.listdir("./downloads")) != 0):
		#doi ten folder 1	
		a = os.listdir("./downloads")[0]
		os.rename("./downloads/%s"%a, "./downloads/1")

		#xoa db
		b = os.listdir("./downloads/1")
		for i in range(len(b)):
			if b[i].endswith(".db") == True:
				os.system("del %s"%b[i])

		# chuyen thu muc file anh
		for i in range(len(b)):
			os.rename("./downloads/1/%s"%b[i], "./downloads/1/%d.jpg"%(i+1))

		for i in range(len(b)):
			if(b[i].endswith("jpg") == True):
				os.system('ffmpeg -i "./downloads/1/%d.jpg" -vf scale="1080:720" "./downloads/%d.jpg"'%(i, i))

		os.system('ffmpeg -r 0.24 -f concat -safe 0 -y -i "video-input-list.txt" -i "good.mp3" -c:v libx264 -c:a aac -pix_fmt yuv420p -crf 23 -r 24 -y 1.mp4')


kk = open("./file/link.txt", "r").readlines()
for i in range(len(kk)):
	writeInput()
	ReadingNews(kk[i].split("\n")[0])
	upload()