from bs4 import BeautifulSoup
import requests

link_web = {'us': 'https://www.foxnews.com/us',
			'world': 'https://www.foxnews.com/world',
			'opinion': 'https://www.foxnews.com/opinion',
			'politics': 'https://www.foxnews.com/politics',
			'entertainment': 'https://www.foxnews.com/entertainment',
			'lifestyle':'https://www.foxnews.com/lifestyle',
			'shows':'https://www.foxnews.com/shows',
			'business':'https://www.foxbusiness.com/',
			'science':'https://www.foxnews.com/science',
			'tech':'https://www.foxnews.com/tech',
			'health':'https://www.foxnews.com/health',
			}

def run(var_one,_link):
	r = requests.get(_link).text
		
	soup = BeautifulSoup(r, 'lxml')
	a = soup.find_all('a')
	a = list(set(a))
	minh = open("./file/link.txt", 'a')
	kkk = open("./file/link.txt", 'r').readlines()
	for i in range(len(a)):
		try:
			temp_link = "https://www.foxnews.com" + a[i]['href']
			for i in range(len(link_web)):
				if link_web[list(link_web.keys())[i]] in temp_link and len(temp_link) > 40 :
					minh.write(temp_link)
					minh.write('\n')
		except:
			pass

for k,v in link_web.items():
	run(k, v)