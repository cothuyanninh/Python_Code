import requests as r
import re
import sys
import urllib.request

access = 'EAAQbvQSpyngBADKmxlWkGhZAZCZCEy8kB9ccfFQRcRnTcaXX0pR3hHZB5adZCO7XSkirZBgvQ9OIBOlYj9RRbTXXMXetgwIlFi23vPkwZBf7FjBPIQZCkiVaIZBEYKk3kzdvFmz4ZBaK9bqWX1nLcUlxTCWHTuPEzy6uFolrkwJ5YugZCqrtRXPmI3WuWLk5MtXknhdawG1PtqfiAZDZD'
minh = open('url.txt', 'rb').readlines()
linh = open('hihi.txt', 'a')
for i in range(len(minh)):
	url = minh[i]
	print(url)
	html = r.get(url)
	# print(html.text)
	video_url = re.search('hd_src:"(.+?)"', html.text).group(1)
	# print(video_url)
	# linh.write(video_url)
	# linh.write("\n")
	# urllib.request.urlretrieve(video_url, '../video_output/video_name.mp4')
	# video = '../video_output/video_name.mp4'
	# url_hihi='https://graph-video.facebook.com/577120059386757/videos?access_token='+str(access)
	# files={'file':open(video,'rb')}
	# flag=r.post(url_hihi, files=files).text
	# print(flag)
