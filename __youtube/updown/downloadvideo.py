from pytube import YouTube, Playlist
openfile = open('kkk.txt', 'r')
links = openfile.readlines()
path_video = './video'

def dowloadvideo(link):
	if link[24:32] != 'playlist': #la video
		try:
			YouTube(link).streams.filter(progressive=True, file_extension='mp4').first().download(path_video)
		except :
			print("Loi cai nay roi {0}".format(link))
			return
	else :
		Playlist(link).download_all(path_video)
		
for link in links:
	print("Dang download video : " + str(link))
	dowloadvideo(link)
openfile.close()