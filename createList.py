# need to run in terminal
import speech_recognition as sr


def chooseName():
    name = input("Enter the name of the person you are speaking to: ")
    return name


# To control user input
def confirmName(name):
    while True:
        confirm = input("Confirm that's how you say " + name + "? Input Y/N: ")
        if confirm == "Y":
            return True
        elif confirm == "N":
            return False
        else:
            print("Please enter 'Y' or 'N' ")


def recordSimilarNames(speech, nameList):  # returns word with similar sounding names
    if speech in nameList:
        # print("no need to add, name = speech") # prints if word already exists
        pass  # don't need to add into list because name is already there
        return False
    else:  # user said name 'incorrectly' (not as per google's speech recognition)
        # print("adding " + speech + " into " + name) # shows word said
        return speech


def soundAlikeName(name):
    count = 0
    nameList = []
    nameList.append(name)
    while count < 3:
        input("Press enter to record")
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

            # print(nameList) # prints nameList as it is updated
        except:
            print("Sorry, there was an error. Please try again")
            continue
        count += 1
    return nameList


def checkUpdates(readList, finalList):
    if "\n" in readList[-1]:
        lastWord = readList[-1][:-1]
        readList[-1] = lastWord
    for element in finalList:
        if element in readList:
            pass
        else:
            readList.append(element)
    # print(readList) # prints updated list of names associated with the name
    line = ",".join(readList) + "\n"
    return line


def updateDatabase(name, finalList):
    file = open("nameList.txt", "r")
    content = []
    added = False
    empty = True
    for lines in file:
        empty = False
        readList = lines.split(",")
        if readList[0] == name:
            updateLine = checkUpdates(
                readList, finalList
            )  # check if there is new elements
            content.append(updateLine)
            added = True
        else:
            content.append(lines)  # continue to append
    file.close()
    if added == False:  # handles if name is not in database
        if empty == True:
            finalListStr = ",".join(finalList)
        if empty == False:
            finalListStr = "\n" + ",".join(finalList)
        content.append(finalListStr)
    print("writing...")
    filewrite = open("nameList.txt", "w+")
    contentStr = "".join(content)
    filewrite.write(contentStr)


# main
name = chooseName()
finalList = soundAlikeName(name)
updateDatabase(name, finalList)
print(name + " added to database")
