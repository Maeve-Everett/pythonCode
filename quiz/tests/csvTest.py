import csv

test = open('userProfiles.csv', 'r')
read = csv.reader(test, delimiter = ',')
for row in read:
    print(row[1])
