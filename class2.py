# #Strings
# # #Looking into strings - access the characters in a string
# # print("programming"[0])   #zero based index
# # print("programming"[1])
# # print("programming"[2])
# # print("programming"[6])
# # print("programming"[0:3])  #slicing - to take a part of a string 
# # print("programming"[3:7])
# print("programming"[3:])
# print("programming"[:4])
# print("programming"[:])

# #Length of a string - number of characters
# print(len("programming"))

# #Change case
# print("programming".upper())  #to uppercase
# print("pROGrammiNg".lower())    #to lowercase

#Integers and floats
# print(25 + 30)
# print(12.2 - 5)
# print(4.5 * 5)
# print(8/2)

#Project 2025
#To calculate the age of a person in the year 2025
# birthYear = input("Enter your birthyear: ")
# birthYear = int(birthYear)
# age = 2025 - birthYear
# print("You are", age, "years old")


#Assignment
#To calculate the age of a person in dog years.
age = input("Enter your age: ")
age = int(age)
age_in_dog_years = 7 * age
print("You are", age_in_dog_years, "years in dog years.")