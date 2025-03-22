#Conditionals

#if, if/else, if/elif/else

# A program that screens people for a class based on their age

age = input("How old are you? ")

age = int(age)

if age < 8 :
    print("You are too young to be in Year 4 class")
elif age > 10:
    print("You are too old to be in Year 4 class")
else:
    print("You can join Year 4 class")

#Write a quiz program that asks a question with options and use conditionals to print "correct" when
#the correct answer is chosen and "wrong" when the incorrect answer is chosen.
#E.g:
# answer = input("Which of these is a noun? a. eat  b. dog  c. play ")
