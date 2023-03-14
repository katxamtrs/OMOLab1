import csv

with open("./movies_dataset.csv") as file:
  csvReader = csv.reader(file)
  for row in csvReader:
    print(row)