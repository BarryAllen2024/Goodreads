import csv
import random

file = open("goodreads_library_export.csv", "r")
data = list(csv.DictReader(file, delimiter=","))
file.close()

allShelvesList = [(row["Exclusive Shelf"]) for row in data]
allTitlesList = [(row["Title"]) for row in data]
# print(allShelvesList)
# print(allTitlesList)

tbrCount = 0
toReadList = []

for i in range(len(allShelvesList)):
  if allShelvesList[i] == "to-read":
    toReadList.append(allTitlesList[i])

for i in range(len(allShelvesList)):
  if allShelvesList[i] == "to-read":
    tbrCount = tbrCount + 1

# print(toReadList)
print(random.choice(toReadList))

#asks if you want another book

answer = input("Do you want another book?"'\n')

if answer == "no" or answer == "n":
  print("Okay, have a nice day!")
elif answer == "yes" or answer == "y":
  while answer == "yes" or answer == "y":
    if answer == "yes" or answer == "y":
      print(random.choice(toReadList))
      print()
      print("Do you want another book?")
      answer = input()
      if answer == "no" or answer == "n":
        print("Okay, have a nice day!")
      if answer != "no" and answer != "n" and answer != "yes" and answer != "y":
        print("Sorry, I didn't understand that. Please try again.")
    elif answer == "no" or answer == "n":
      print("Okay, have a nice day!")
    else:
      print("Sorry, I didn't understand that. Reload the code.")
else:
  print("Sorry, I didn't understand that. Reload the code.")



#not fully working code, will edit later
# if answer == "no" or answer == "n":
#   print("Okay, have a nice day!")
# elif answer == "yes" or answer == "y":
#   while answer == "yes" or answer == "y":
#     if answer == "yes" or answer == "y":
#       print(random.choice(toReadList))
#       print("Do you want another book?")
#       answer = input()
#       if answer == "no" or answer == "n":
#         print("Okay, have a nice day!")
#     elif answer == "no" or answer == "n":
#       print("Okay, have a nice day!")
#   else:
#     print("Sorry, I didn't understand that. Try again?")
#     answer = input()
#     if answer == "no" or answer == "n":
#       print("Okay, have a nice day!")
# else:
#   print("Sorry, I didn't understand that. Try again?")
#   answer = input()
#   if answer == "no" or "n":
#     print("Okay, have a nice day!")
#   while answer == "yes" or answer == "y":
#     if answer == "yes" or answer == "y":
#       print(random.choice(toReadList))
#       print("Do you want another book?")
#       answer = input()
#       if answer == "no" or answer == "n":
#         print("Okay, have a nice day!")
#     elif answer == "no" or answer == "n":
#       print("Okay, have a nice day!")
#   else:
#     print("Sorry, I didn't understand that. Try again?")
#     answer = input()
#     if answer == "no" or answer == "n":
#       print("Okay, have a nice day!")
  



# tells how many books are in the to-read list
# print("Do you want to know how many books are in your tbr shelf?")
# answer = input()

# if answer == "yes" or answer == "y":
#  print(tbrCount)
# elif answer == "no" or answer == "n":
#  print("Okay, have a nice day!")
# else:
#  print("Sorry, I didn't understand that. Have a nice day!")