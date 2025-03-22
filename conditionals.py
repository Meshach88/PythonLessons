#Conditionals
# if - to check if a condition is true and do something.
# if/else - to check if a condition is true and do something and do something else if the condition is false.
# if/elif/else - to check for multiple conditions

age = input("Enter your age: ")
age = int(age)

if age >= 18:
    print("You are old enough to vote.")
elif age == 17:
    print("You can vote next year.")
else:
    print("You are not old enough to vote.")
    
#Project Quiz
print("In Python, what do you call a 'box' used to store data?")
answer = input("Enter your answer: ")
if answer == "variable":
    print(":)" * 100)
else:
    print(":(" * 100)

print("Thank you for playing.")




