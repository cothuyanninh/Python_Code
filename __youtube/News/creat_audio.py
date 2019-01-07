import requests
from bs4 import BeautifulSoup
from gtts import gTTS

trash = '''This material may not be published, broadcast, rewritten,       or redistributed. ©2018 FOX News Network, LLC. All rights reserved.       All market data delayed 20 minutes.'''
trash2 = 'This material may not be published, broadcast, rewritten, or redistributed. ©2018 FOX News Network, LLC. All rights reserved. All market data delayed 20 minutes.'

def creat_audio(link):

	r = requests.get(link).text
	
	soup = BeautifulSoup(r, 'lxml')
	title = soup.title.text

	content = soup.find_all('p')
	src = ''
	for i in range(len(content)):
		src += content[i].text

	src = src.replace("\n", " ")
	data = title + src
	data = data.replace(trash, " ")
	data = data.replace(trash2, " ")

	# tts = gTTS(text= data, lang ='en')
	# tts.save("good.mp3")
	json_reuslt = {'title': title, 'comment': data}

	return json_reuslt