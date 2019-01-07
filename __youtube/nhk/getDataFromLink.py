import requests, bs4
from saveIntoCSV import saveIntoCsv
from upload.downloadvideo import downloadVideo
open_file = open('./data/urlfile.txt', 'r').readlines()
minh_option = input("Co muon down khong? : y/n: ")
for i in range(len(open_file)):
	res = requests.get(open_file[i].split('\n')[0])
	if res.status_code == requests.codes.ok:
		converSoup = bs4.BeautifulSoup(res.text, "lxml")
		# comment_ = converSoup.find("meta",  name="description", content=True)
		# title
		title_ = converSoup.select('title')[0].getText()
		# comment
		# comment_list= []
		temp_cmt = ' '
		for j in range(len(converSoup.select('p'))):
			temp_cmt  = temp_cmt + str(converSoup.select('p')[j].getText()) 
			# comment_list.append(str(converSoup.select('p')[j].getText()))
		#tag
		tag_list = []
		for tag in converSoup.find_all("meta"):
			if tag.get("name", None) == "description":
				temp_cmt  = temp_cmt + str(tag.get("content", None)) 
				# comment_list.append(tag.get("content", None))
				# print(tag.get("content", None))
			if tag.get("name", None) == "keywords":
				tag_list.append(tag.get("content", None))
		index_1 = open_file[i].index('_id')
		index_2 = open_file[i][index_1+4:index_1+12]
		index_3 = open_file[i][index_1+4:index_1+21]
		linkm3u8_= []
		linkm3u8_ = 'https://nhk-vh.akamaihd.net/i/das/' + index_2 +'/' + index_3 + '_V_000.f4v/master.m3u8'
		if minh_option == 'y':
			downloadVideo(linkm3u8_, i)
		# saveIntoCsv(i,title_[0], title_[0], str(comment_list), str(tag_list), open_file[i].split('\n')[0], linkm3u8_, i)
		# txt
		file_txt = './upload/results.txt'
		linh =  open(file_txt,'a',encoding='utf8')
		temp =  {'index': str(i),
		# 'file_name': title_[0],
		'title' : title_,
		'coment': temp_cmt,
		'tag': str(tag_list),
		# 'link': open_file[i],
		'linkm3u8': linkm3u8_
		}
		linh.write(str(temp))
		linh.write('\n')
		linh.close()








# print(comment_['content'])
		# open_file_2.write(img[0].text)
