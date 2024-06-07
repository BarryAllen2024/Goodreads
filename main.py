import csv
import random

file = open("goodreads_library_export.csv", "r")
data = list(csv.DictReader(file, delimiter=","))
file.close()
#reads the csv file and stores it as a list of dictionaries

allShelvesList = [(row["Exclusive Shelf"]) for row in data]
allTitlesList = [(row["Title"]) for row in data]
#creates a list of all the shelves and titles

tbrCount = 0
toReadList = []
#creates a list of all the titles that are currently in the "to read" list

for i in range(len(allShelvesList)):
  if allShelvesList[i] == "to-read":
    toReadList.append(allTitlesList[i])
#goes through the list of titles and adds them to the toReadList if they are in the tbr

for i in range(len(allShelvesList)):
  if allShelvesList[i] == "to-read":
    tbrCount = tbrCount + 1
#goes through the list of titles and adds 1 to tbrCount if they are in the "to read"

print(random.choice(toReadList))
#prints a random title from the toReadList

print("\n")

answer = input("How many more do you want? Please type a number: \n")
for i in range(int(answer)):
  print("\n")
  print(random.choice(toReadList))
  print("\n")
#prints however many more random books you want

#print(tbrCount) / optional if you want to count number of TBR books