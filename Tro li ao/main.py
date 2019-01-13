import time
from recordAudio import *
from textToSpeech import *
from sampleData import *

class Mivis():
    def __init__(self, data):
        self.data = data


speak("Hi Minh, I am Minvis, what can I do for you?")

# while 1:
# 	data = recordAudio()
# # data = "show me to youtube"
# 	ConverstationAI.connectWeb(data)

# data = "where is HaNoi"
data = input("Type your input")
# ConverstationAI.findInGoogleMap(data)
ConverstationAI.readingNews("https://www.foxnews.com/politics/trump-team-fires-back-at-mueller-probe-hysterical-coverage-of-cohen-deal")