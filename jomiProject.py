from random import*
score = 0
score1 = 0
score2 = 0
score3 = 0
score4 = 0

playing = True
names = []
players = input("How many players? ")

players = int(players)
if players > 5:
    print("Maxium players is five")
else:
    for player in range(players):
        name = input("Enter name of player: ")
        names.append(name)
        
while playing == True:
    chosenName = choice(names)
    print(chosenName, "has been selected.")
    if chosenName == names[0]:
        score = score + 1
    elif chosenName == names[1]:
        score1 = score1 + 1
    elif chosenName == names[2]:
        score2 = score2 + 1
    elif chosenName == names[3]:
        score3 = score3 + 1
    elif chosenName == names[4]:
        score4 = score4 + 1
    response = input("Would you like to continue the game?Y/N ").lower()
    if response == 'n':
        playing = False
        
print("Thank you for playing,I will now proceed to show your final scores.")
print(names[0], "=", score)
print(names[1], "=", score1)
print(names[2], "=", score2)
print(names[3], "=", score3)
print(names[4], "=", score4)