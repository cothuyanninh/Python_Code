import re
import webbrowser, requests, bs4

def downloadImage(pic_url, namepicture):
	name_of_people = '../data/temp/'+ namepicture+'.jpg'
	with open(name_of_people, 'wb') as handle:
		response = requests.get(pic_url)
		if not response.ok:
			print(response)
		for block in response.iter_content(1024):
			if not block:
				break
			handle.write(block)


def getLinkPicture(linkfile):
	filetxtreading = open(linkfile, 'r').readlines()
	listFromCV = []
	for link_i in range(len(filetxtreading)):
		res = requests.get(filetxtreading[link_i].split('\n')[0])
		if res.status_code == requests.codes.ok :
			listFromCV.append([])

	for link_i in range(len(filetxtreading)):
		res = requests.get(filetxtreading[link_i].split('\n')[0])
		if res.status_code == requests.codes.ok:
			converSoup = bs4.BeautifulSoup(res.text, "lxml")
			img = converSoup.select('img')
			for i in range(len(img)):
				if 'cvo-profile-avatar' in str(img[i]) and 'src=' in str(img[i]):
					name_of_person = converSoup.select('#cvo-profile-fullname')[0].getText()
					imgpicture = str(img[i])
					var_start = imgpicture.index('src=')+5
					var_end = imgpicture.index('.jpg?')
					link_img = ''
					for i in range(var_start, var_end+5):
						link_img += imgpicture[i]
						
					listFromCV[link_i].append(link_img)
					downloadImage(link_img, name_of_person)

# print(getLinkPicture('../data/input/txt/linkCV.txt'))