textSpeakDictionary = {'lol': 'laugh out loud', 'idk':'i dont know'}

#Function is a block of code that performs a specific task

#create a function to translate a word
def translateText():
    text = input("Enter the text you want to translate: ")
    meaning = textSpeakDictionary[text]
    print(text, " = ", meaning)

#create a function to add text to the dictionary
def addText():
    textToAdd = input("Enter a text to add: ")
    meaningOfText = input("Enter the meaning of the text: ")
    textSpeakDictionary[textToAdd] = meaningOfText
    print(textSpeakDictionary)

#create a function to delete text from the dictionary
def deleteText():
    textToDelete = input("Enter the text you want to delete: ")
    del textSpeakDictionary[textToDelete]
    print(textSpeakDictionary)

#create a function to translate a sentence
def translateSentence():
    sentence = input("Enter a sentence to translate: ")  #idk what to eat
    listOfWords = sentence.split()          #['idk', 'what', 'to', 'eat']
    translatedSentence = ""
    for word in listOfWords:
        if word in textSpeakDictionary: 
            translatedSentence = translatedSentence + textSpeakDictionary[word] + " "
        else:
            translatedSentence = translatedSentence + word + " "
    print(translatedSentence)