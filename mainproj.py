# need to run in terminal
import speech_recognition as sr


# To control user input
def confirmName(name):
    while True:
        confirm = input("Confirm that's how you say " + name + "? Input Y/N")
        if confirm == 'Y':
            return True
        elif confirm == 'N':
            return False
        else:
            print("Please enter 'Y' or 'N'")


def recordSimilarNames(speech,
                       nameList):  # returns word with similar sounding names
    if speech in nameList:
        print('no need to add, name = speech')
        pass  # don't need to add into list because name is already there
        return False
    else:  # user said name 'incorrectly' (not as per google's speech recognition)
        print('adding ' + speech + ' into ' + name)
        return speech


def soundAlikeName(name):
    count = 0
    nameList = []
    nameList.append(name)
    while count < 3:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say " + name)
            audio = r.listen(source)
        try:
            speech = r.recognize_google(audio, language="en-US")
            # prompt user to confirm that that is how he says the name
            validYN = confirmName(name)
            if validYN:  # if user says that its a correct recording
                pass
            else:  # if user says that he recorded wrongly
                continue

            newName = recordSimilarNames(speech, nameList)
            if newName:  # if speech = name, don't bother
                nameList.append(newName)  # add the new 'incorrect' name

            print(nameList)
        except:
            print('Sorry, there was an error. Please try again')
            continue


# What name are we looking for
name = 'Max'
print(soundAlikeName(name))
'''
with sr.Microphone() as source:
    print("Say " + name)
    audio = r.listen(source)

try:
    # recognize speech
    speech = r.recognize_google(audio, language="en-US")
    # print("Google Speech Recognition thinks you said " + speech)
    # prompt user to confirm that that is how he says the name
    confirm = input("Confirm that's how you say " + name + "? Input Y/N")
    if confirm == 'Y':
        pass
    elif confirm == 'N':
        pass
    if name in speech:
        pass
    else:
        pass
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(
        "Could not request results from Google Speech Recognition service; {0}"
        .format(e))
'''