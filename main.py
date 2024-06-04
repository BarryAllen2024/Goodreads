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