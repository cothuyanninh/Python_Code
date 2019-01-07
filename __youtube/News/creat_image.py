import os
import creat_audio

def creat_image(link_):

	jsonn = creat_audio.creat_audio(link_)
	keyword = jsonn['title']
	# a = keyword
	# keyword['title'] = keyword['title'].replace(" ", '+')
	keyword= keyword.replace("'",'')
	keyword = keyword.replace("’",'')
	keyword = keyword.replace("‘",'')
	keyword = keyword.replace("|",'')	
	keyword = keyword.replace(",",'')
	keyword = keyword.replace(":",'')
	keyword = keyword.replace("?",'')
	keyword = keyword.replace("!",'')

	os.system("rmdir /s /q downloads")
	os.system('googleimagesdownload -k "%s" -l 10 '%keyword)
	print(keyword)
	
	return jsonn

# creat_image("https://www.foxnews.com/us/seagram-heiress-is-secretly-paying-sex-cults-legal-fees-prosecutors")