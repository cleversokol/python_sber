import csv
import operator

DATETIME=2
CRIMETYPE=5

cdict = {}

with open("Crimes.csv") as file:
    reader = csv.reader(file)
    for i in reader:
        year = i[DATETIME].split(" ", maxsplit=1)[0][6:]
        if year == "2015":
            n = cdict.get(i[CRIMETYPE])
            n = n + 1 if n != None else 0
            cdict.update({i[CRIMETYPE]:n})
            #print(year)
sorted_dict = sorted(cdict.items(), key=operator.itemgetter(1))
print(sorted_dict)

