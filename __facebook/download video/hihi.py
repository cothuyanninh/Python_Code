import requests
import ast

access = 'EAAMIDQTZBYHMBAA7nG2vWj74qR1Hf6V2Sd1Tm5m1pA21f1B74zLFeIEZAq5ihBeWBasDxdH2MEBWjghgQlgUogZAR3qZCTl23tpYsuxAwtALX9ZCjHSgZCvGeoZALOnfAVXF55HHrJBUzZAGLO5MWQKqylCb5bOCIv6ncRUBypJjCAZAlhZCUIKTh7fYDsW3D2xq05nSxZC96VOQWIrKFz5lul4x0mnJ6ZBcfQUZD'
# token cua tran kieu an
# access = 'EAAQbvQSpyngBAL6E3v2WLylLz4oqB6o9YiyT8UIekdtpAbtzHuVg4uUFIvPhfgjZALliBMtc2dATt1wZAhCLq4vPglicKzZBrwBK1ATYED9bWZBZAZB8qYKZCnr1ja2Awdzexh7HNO2UeeH9oZCEkHB2oJyVYShQmQh5w4g3koT8lBB016ZCJD0eQ3lwstPzF8MCiB7GXk4M0VQZDZD'
minh = open('url.txt', 'r').readlines()
linh = open('hihi.txt', 'w')
for i in range(len(minh)):
	dmer = str(minh[i]).index("videos/")
	video_id = minh[i][(dmer+7):]

	result_url = 'https://graph.facebook.com/' + str(video_id) + '?fields=from,description,source&access_token='+ access
	print(result_url)
	# linh.write(result_url)
	html = requests.get(result_url)
	print(html.text)
	result = ast.literal_eval(html.text)
	# print(result['description'].encode())
	minhdeptrai = result['source'].replace("\/", "/")
	linh.write(result['id'])
	linh.write(': ')
	linh.write(minhdeptrai)
	linh.write('\n')



	# video_url = re.search("")
	# urllib.request(result_url)
	# url = minh[i]
	# print(url)
	# html = r.get(url)
	# video_url = re.search('hd_src:"(.+?)"', html.text).group(1)
	# print(video_url)
	# linh.write(video_url)
	# # linh.write("\n")
	# # urllib.request.urlretrieve(video_url, '../video_output/video_name.mp4')
	# # video = '../video_output/video_name.mp4'
	# # url_hihi='https://graph-video.facebook.com/577120059386757/videos?access_token='+str(access)
	# # files={'file':open(video,'rb')}
	# # flag=r.post(url_hihi, files=files).text
	# # print(flag)
