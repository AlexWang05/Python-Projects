#  converting Java projects to Python # 3
#  written by Alex Wang


def getKeyCharacter():  # why doesn't python have do-while loops smh
    charInput = 0  # initializing character input for while loop

    while charInput != 1:  # checking for invalid input
        stringInput = input("Please enter a SINGLE character to act as key: ")
        charInput = len(stringInput)

    charInput = stringInput[0]
    return charInput


def getString():
    min_size = 4
    textLength = 0  # initializing text length

    while textLength < min_size:
        stringText = input("Please enter a phrase or sentence >= 4 and <= 500 characters: ")
        textLength = len(stringText)

    return stringText


#  takes string & character as param. and replace w/ '$'
def maskCharacter(stringText, charInput):
    stringLength = len(stringText)
    maskedString = ""  # initializing new String

    for i in range(stringLength):  # loooping through text
        if stringText[i] == charInput:  # checking if character is key
            maskedString += '$'  # adds $ to returned text

        elif stringText[0] != charInput:  # if character is not key
            maskedString += stringText[i]  # adds original text to return

    return maskedString  # return masked text


# function that removes key character in text
def removeCharacter(stringText, charInput):
    stringLength = len(stringText)
    removedString = ""  # initializing new string

    for i in range(stringLength):  # looping through text
        if stringText[i] != charInput:
            removedString += stringText[i]

    return removedString


def countKey(stringText, charInput):
    stringLength = len(stringText)
    charCount = 0

    for i in range(stringLength):
        if stringText[i] == charInput:
            charCount += 1

    return charCount


#  main method in java
charInput = getKeyCharacter()
stringText = getString()
maskedString = maskCharacter(stringText, charInput)
removedString = removeCharacter(stringText, charInput)
charCount = countKey(stringText, charInput)

# printing results
print("Stringwith " + (charInput) + " masked:\n" + maskedString)
print("\nString with " + charInput + " removed:\n" + removedString)
print("\n# " + charInput + "s: " + str(charCount))
