textSpeakDict = {"lol":"laugh out loud",
                 "idk": "i dont know"}

text = input("What would you like to translate?: ")
print(text, "=", textSpeakDict[text])

#Translate a sentence
sentence = input("Enter a sentence to translate: ")

words = sentence.split()

translatedSentence = ""

for word in words:
    if word in textSpeakDict:
        translatedSentence = translatedSentence + textSpeakDict[word] + " "
    
    else:
        translatedSentence = translatedSentence + word + " "
print(translatedSentence)





