import speech_recognition as sr
# obtain audio from the microphone
r = sr.Recognizer()
m = sr.Microphone()
def removeLineBreak(lst):
    lastWord = lst[-1]
    removedWord = lastWord[:-1]
    lst[-1] = removedWord
    return lst
def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        speech = recognizer.recognize_google(audio)
        print(speech)
        with open("nameList.txt","r") as nameList:
            for lines in nameList:
                pieces = lines.split(",")
                correctLst = removeLineBreak(pieces)
                for words in correctLst:
                    if words in speech:
                        print(correctLst[0],"pay attention!")
        if "stop" in speech:
            stop_listening(wait_for_stop=False)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    

def checkBg():
    input("Press enter to input background noise:")
    with m as source:
        r.adjust_for_ambient_noise(source)
"""
def SpeechToText():    
    with sr.Microphone() as source:
        r.phrase_threshhold = 0
        print("Say something!")
        audio = r.listen_in_background(source,callback,phrase_time_limit = 2)
        #print(len(audio.get_raw_data()))
        #if 170000 < len(audio.get_raw_data()) < 200000 :
        #    print("Success")
        #    pass
        #else:
           #print("Too long")
        #   return
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        speech = r.recognize_google(audio)
        #print(speech)
        with open("nameList.txt","r") as nameList:
            for lines in nameList:
                pieces = lines.split(",")
                correctLst = removeLineBreak(pieces)
                for words in correctLst:
                    if words in speech:
                        print(correctLst[0],"pay attention!")
        global allowed
        if "stop" in speech:
            allowed=False
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
"""
allowed = True
#checkBg()
#input("Press enter to start application:")
#while allowed:
    #SpeechToText()
    #print(r.energy_threshold)

stopListening = r.listen_in_background(m,callback,phrase_time_limit = 2)


