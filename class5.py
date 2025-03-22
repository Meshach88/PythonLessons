#GAMESHOW
from random import *
score = 0
print('''
      Gameshow!
      ==========
      There's a prize behind one of the three doors.
      Guess the correct door to win the prize.
      _______   ______  _______
      |  [1]|   | [2]|  |  [3]|
      |   o |   |   o|  |    o|
      |_____|   |____|  |_____|
      
      Choose a door (1,2 or 3)
      ''')
playing = True

#for attempt in range(3):
while playing == True:
      chosenDoor = input("Enter your choice: ")
      chosenDoor = int(chosenDoor)
      winningDoor = randint(1,3)
      print("The chosen door is", chosenDoor)
      print("The winning door is", winningDoor)
      if chosenDoor == winningDoor:
            score = score + 1
            print("Congratulations! You chose the right door")
      else:
            print("Oops, you chose the wrong door")
            
      response = input("Do you want to play again? (y/n): ")
      if response == 'n':
            playing = False

print("Thank you for playing")
print("Your final score is", score)