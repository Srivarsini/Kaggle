import csv

with open('../mergedData.csv', 'rb') as f:
    reader = csv.reader(f)
    data_as_list = list(reader)

print data_as_list
