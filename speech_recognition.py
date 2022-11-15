import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone()as source:
    print("speak Anything:")
    audio=r.listen(source,timeout=5,phrase_time_limit=25)
    print('Done,please wait we are processing what you said...')
    try:
        text=r.recognize_google(audio)
        print("you said:{}".format(text))
        except:
            print("sorry we could not recognize what you said.you can try again...")