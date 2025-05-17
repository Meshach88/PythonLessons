#GAME SHOW

from random import *

print("GAME SHOW")
print("=========")

print('''
Choose a door: 1, 2 or 3
________      _________     _________
|      |      |       |     |       |
|      |      |       |     |       |
|   o 1|      |    o 2|     |    o 3|
|      |      |       |     |       |
|      |      |       |     |       |
|______|      |_______|     |_______|

''')

for attempt in range(3):
    chosenDoor = input("Enter your choice: ")
    chosenDoor = int(chosenDoor)

    winningDoor = randint(1,3)

    print("The winning door is", winningDoor)
    print("The chosen door is", chosenDoor)

    if chosenDoor == winningDoor:
        print("Congratulations, you got the price")
    else:
        print("Oh oh! You missed the price")




