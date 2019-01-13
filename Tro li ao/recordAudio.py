import speech_recognition as sr

def recordAudio():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening: ")
        audio = r.listen(source)

    data = ""

    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data