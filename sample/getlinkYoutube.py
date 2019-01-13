from bs4 import BeautifulSoup
import requests

def saveIntoFile(domain, href):
	txtsavelink = open('dmerm.txt','a')
	txtsavelink.write(domain + href + '\n')

def getPlaylistLinks(url):
	#txtsavelink = open('dmerm.txt','a')
    sourceCode = requests.get(url).text
    soup = BeautifulSoup(sourceCode, 'html.parser')
    domain = 'https://www.youtube.com'
    for link in soup.find_all("a", {"dir": "ltr"}):
        href = link.get('href')[:20]
        if href.startswith('/watch?'):
            print(link.string.strip())
            print(domain + href + '\n')
            saveIntoFile(domain, href)
      #      txtsavelink.write(domain+href+'\n')
   # txtsavelink.close()
getPlaylistLinks('https://www.youtube.com/channel/UCJDep3CS-rfHBCFIxObPChw/videos?flow=grid&view=0&sort=da')