#!/usr/bin/env python2.7

import csv
from datetime import datetime

path = "/home/ayousuf/python_code/Oracle PSU%2FBP170718 Rollout - OVERVIEW.csv"
file = open(path)
reader = csv.reader(file)

header = next(reader)
#data = [row for row in reader]
#print(len(data))
#quit(3)

#print(type(reader))
#print(dir(reader))
#print(help(reader))
#quit(3)
#print(reader.line_num)
#print(header)
#print(data[0][6:12])
#print(data[0][6],data[0][7],data[0][8],data[0][9])
#quit(3)
print(header[6:12])

for row in reader:
        if not 'Jeff' or not 'Amyn' in row[8]:
            print(row[6:12])