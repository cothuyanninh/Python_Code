import requests
username = "UCT0VTJX2dbq_kQ9D8lKdhMw"
url = "https://www.youtube.com/channel/{0}/videos".format(username)
page = requests.get(url).content
data = str(page).split(' ')
item = 'href="/watch?'
vids = [line.replace('href="', 'youtube.com') for line in data if item in line] # list of all videos listed twice
minh = open('ahihi.txt', 'a')
linh = open('database.txt', 'r')
kinh = open('database.txt', 'a')
b = linh.readlines()
for i in range(len(vids)):
	if str(vids[i]) not in b:
		kinh.write(vids[i] + '\n')
for i in range(len(vids)):
	minh.write(('https://www.' + vids[i]).split('"')[0] + '\n')