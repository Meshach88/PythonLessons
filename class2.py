textSpeakDict = {"lol" : "laugh out loud", "idk" : "i dont know"}


def translateText():
    text = input("Enter a text to translate: ")
    print(textSpeakDict[text])

def translateSentence():
    sentence = input("Enter a sentence to translate: ")
    words = sentence.split()

    translatedSentence = ""

    for word in words:
        if word in textSpeakDict:
            translatedSentence = translatedSentence + textSpeakDict[word] + " "
        else:
            translatedSentence = translatedSentence + word + " "
        
    print(translatedSentence)
    
#to add text to the dictionary
def addText():
    textToAdd = input("What text would you like to add to the dictionary: ")
    meaningOftext = input("What is the meaming of the text: ")
    textSpeakDict[textToAdd] = meaningOftext
    print(textSpeakDict)

#to delete text from the dictionary
def deleteText():
    textToDelete = input("What text would you like to delete from the dictionary: ")
    del textSpeakDict[textToDelete]
    print(textSpeakDict)

def displayMenu():
    print('''
          Menu:
          t = translate text
          s = translate sentence
          a = add text
          d = delete text
          q = quit
          ''')

running = True

while running == True:
    displayMenu()
    menuChoice = input("Enter your choice: ").lower()
    
    if menuChoice == "t":
        translateText()
        
    elif menuChoice == "s":
        translateSentence()
        
    elif menuChoice == "a":
        addText()
    
    elif menuChoice == "d":
        deleteText()
    
    elif menuChoice == "q":
        running = False
    
    else:
        print("Invalid choice! Please try again")