import speech_recognition as sr

def removeLineBreak(lst):
    lastWord = lst[-1]
    removedWord = lastWord[:-1]
    lst[-1] = removedWord
    return lst


def callback(recognizer, audio):
    try:
        speech = recognizer.recognize_google(audio)
        print(speech)
        with open("nameList.txt", "r") as nameList:
            for lines in nameList:
                pieces = lines.split(",")
                correctLst = removeLineBreak(pieces)
                for words in correctLst:
                    if words in speech:

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(
                e
            )
        )


def checkBg():
    input("Press enter to input background noise:")
    with m as source:
        r.adjust_for_ambient_noise(source)



checkBg()
stopListening = r.listen_in_background(m, callback, phrase_time_limit=2)


