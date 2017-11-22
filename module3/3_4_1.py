import csv

with open("example.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open("example.tsv") as file:
    reader = csv.reader(file)
    #writer = csv.writer(file)
    for row in reader:
        print(row)
        #writer.write(row)