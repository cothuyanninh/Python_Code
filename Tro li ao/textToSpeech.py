from gtts import gTTS
import os


def speak(audioString):
	
    # print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("audio.mp3")
    # os.system("del audio.mp3")