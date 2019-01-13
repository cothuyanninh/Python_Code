from textToSpeech import *
from time import ctime
import requests
from bs4 import BeautifulSoup
from gtts import gTTS

website_cmd = ['show me', 'connect to', 'listen to','search for me']
google_search = []
map_search = ["where is"]
music_search = ['listen to']
reading_news = ['read', 'news', 'hot']


class ConverstationAI():

    def __init__(self, data):
        self.data = data

    def Greeting(data):

        if "how are you" in data:
            speak("I am fine")

        if "what is your name" in data:
            speak("My name is Javis. I am a Minh's bot.")

        if "How old arr you" in data:
            speak("one years old")

        if "what time" and "it" in data:
            speak(ctime())

    def connectWeb(data):

        data = data.split(" ")
        website = data[-1]
        speak("Hold on Minh, I will show you now! You are connecting into {0}".format(website))
        os.system("start chrome https://www."+website+".com")


    def findInGoogleMap(data):

        data  = data.split(" ")
        location = data[-1]
        speak("Hold on Minh, I will show you now! You are watching HaNoi")
        os.system("start chrome https://www.google.nl/maps/place/" + location)

    # def listenMusic(data):

    #     for i in range(music_search):
    #         if (music_search[i] in data):


    def findInGoogle(data):

        data = data.split(" ")
        key_words = data[-1]
        speak("OK. You will see the result now!")
        os.system("start chrome ")


    def getLinkFromNews(web, type):
        req = requests.get("https://%s.com/%s"%(web, type))
        soup = BeautifulSoup(req, 'lxml')
        for a in soup.find_all('a', href=True):
            print ("Found the URL:"+ a['href'])
            return a['href']


    def readingNews(link):

        speak("Where do you want to reading news?")
        web_ = input("Web: ")
        type = input("Kind of: ")

        r = requests.get(link).text
        soup = BeautifulSoup(r, 'lxml')
        title = soup.title.text
        content = soup.find_all('p')
        src = ''
        for i in range(len(content)):
          src += content[i].text

        src = src.replace("\n", " ")
        data = title + src
        print(src)

        tts = gTTS(text= src, lang ='en')
        tts.save("good.mp3")
        os.system("good.mp3")


