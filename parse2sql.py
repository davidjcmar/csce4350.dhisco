#!/usr/bin/python -B
# This program accepts a .schema file and outputs a
# mysql file to add a table to "dhiscodb"
import sys

f_read = open(sys.argv[1], "r")
# read number of columns
col_number = f_read.readline()
col_number = col_number[:-1]
#print col_number, " columns\n"
# read column values
columns = []
for i in range(int(col_number)):
    columns.append(f_read.readline())
for i in range(len(columns)):
    columns[i] = columns[i][:-1]
    #print columns[i]
# create db
print "USE dhiscodb; \n"
print "CREATE TABLE ", sys.argv[1][5:-5], " ("
# write columns
for i in range(len(columns)):
    print columns[i]
    if int(i) != len(columns) - 1:
        print(", ")
    else:
        print ");\n"
# insert rows
print "INSERT INTO ", sys.argv[1][5:-5], " ("
for i in range(len(columns)):
    print columns[i]
    if int(i) != len(columns) - 1:
        print ", "
    else:
        print ")\nVALUES("
i = 0
line = f_read.readline()
while(line != ''):
    if i % len(columns) >= 5 and i % len(columns) <= 7:
        print line
    elif i % len(columns) >= 13 and i % len(columns) <= 14:
        print line
    else:
        print '"'
        print line
        print '"'
    line = f_read.readline()
    if line == '':
        print ");"
        break
    else:
        print ", "
    i += 1
f_read.close()
