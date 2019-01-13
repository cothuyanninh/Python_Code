import re
import webbrowser, requests, bs4
from getAvatarFromLink import getLinkPicture
def scanFromTXT(linkfile):
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
			listFromCV[link_i].append('txt')
			listFromCV[link_i].append(converSoup.select('#cvo-profile-fullname')[0].getText())
			listFromCV[link_i].append(converSoup.select('#cvo-profile-phone')[0].getText())
			listFromCV[link_i].append(converSoup.select('#cvo-profile-email')[0].getText())
			listFromCV[link_i].append(filetxtreading[link_i].split('\n')[0])
			# getLinkPicture(filetxtreading[link_i].split('\n')[0])

	getLinkPicture(linkfile)
	
	return listFromCV



#print(scanFromTXT())	


