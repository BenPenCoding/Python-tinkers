#Functions

def readFile(file):

    text = ""

    for line in file:

        text += line

    textArray = text.split("\n")

    for phrase in range(len(textArray)):

        textArray[phrase] += " "

    text = ""

    for phrase in textArray:

        text += phrase

    file.close()
    return text

def writeFile(text):

    file = open("/Users/benpennycook/Library/CloudStorage/OneDrive-DurhamUniversity/Desktop/Git Repos/Python-tinkers/YouTube transcript formatter/TestOutput.txt", "w")
    file.write(text)
    file.close()

def RemoveTimeStamps(text):

    returnText = text

    removeArray = []

    characterNum = 0

    while characterNum < len(text):
        
        removeText = ""

        if text[characterNum].isnumeric():

            removeText += text[characterNum]
            characterNum += 1

            while True:

                if characterNum < len(text):

                    if text[characterNum].isnumeric():

                        removeText += text[characterNum]
                        characterNum += 1
                        continue

                    else:

                        if text[characterNum] == ":":

                            removeText += text[characterNum]
                            characterNum += 1

                            if text[characterNum].isnumeric():

                                removeText += text[characterNum]

                                while True:

                                    characterNum += 1

                                    if characterNum < len(text):

                                        if text[characterNum].isnumeric():

                                            removeText += text[characterNum]
                                            characterNum += 1
                                            continue
                                            
                                        else:

                                            removeArray.append(removeText)
                                            break
                                    
                                    else:
                                        
                                        removeArray.append(removeText)
                                        break

                            else:

                                characterNum += 1
                                break

                        else:

                            characterNum += 1
                            break

                else:

                    break
            
        else:

            characterNum += 1

    for removeText in removeArray:

        returnText = returnText.replace(removeText, "")

    return returnText

def removeDoubleSpaces(text):

    returnText = ""

    for character in range(0,len(text)-1):

        if text[character] == " " and text[character + 1] == " ":

            continue

        else:

            returnText += text[character]

    returnText += text[-1]

    return returnText
    
#Main

file = open("/Users/benpennycook/Library/CloudStorage/OneDrive-DurhamUniversity/Desktop/Git Repos/Python-tinkers/YouTube transcript formatter/TestInput.txt", "r")

text = readFile(file)

text = RemoveTimeStamps(text)

text = removeDoubleSpaces(text)

writeFile(text)

            





