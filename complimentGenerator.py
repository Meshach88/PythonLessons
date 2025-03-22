from random import *

print('Compliment Generator')
print('====================')

running = True
adjectives = ['amazing', 'above-average', 'excellent']
hobbies = ['riding a bike', 'programming', 'playing soccer']

name = input("What is your name? ")

print('''Menu
      c = generate compliment
      a = add hobby to list
      d = delete hobby from list
      p = print hobbies
      q = quit
      ''')
while running == True:
    menuChoice = input("> ").lower()
    
    if menuChoice == 'c':
        print("Here is your compliment", name)
        print("You are", choice(adjectives), 'at', choice(hobbies) )
        print("You are welcome")
    
    elif menuChoice == 'a':
        hobbyToAdd = input("Please enter the hobby you want to add: ")
        hobbies.append(hobbyToAdd)
        
    elif menuChoice == 'd':
        hobbyToDelete = input("Please enter the hobby you want to delete")
        if hobbyToDelete in hobbies:
            hobbies.remove(hobbyToDelete)
        else:
            print("Hobby not in list")
    
    elif menuChoice == 'p':
        print(hobbies)
    
    elif menuChoice == 'q':
        running = False
    
    else:
        print("Invalid Choice   ")
        


