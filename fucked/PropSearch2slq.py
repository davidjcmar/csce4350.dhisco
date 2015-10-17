#!/usr/bin/python -B
import sys

tag_in = "./tags/"
tag_in += sys.argv[1][5:-5]
tag_in = tag_in + ".tags"
# form mysql command
str_out = "USE dhiscodb;"
print str_out
# create table
str_out = "CREATE TABLE " + tag_in[7:-5]
str_out = str_out + "("
# enter id
tags = ["id INT(11) NOT NULL AUTO_INCREMENT\n"]
with open(tag_in, "r") as fd:
    for line in fd:
        tags.append(line)
column_num = tags[1][:-1]
tags.remove(str(column_num) + '\n')
#print column_num
for i in range(len(tags)):
    tags[i] = tags[i][:-1]
#    print tags[i]
# Form Create Table Colmuns
for i in range(len(tags)):
    str_out += str(tags[i]) + ", "
str_out += "PRIMARY KEY (id)"
str_out += ");"
print str_out
# insert into table
print "\n\n"
column = []
data = []
with open(sys.argv[1], "r") as fd:
    column_num = fd.readline()
    column_num = int(column_num[:-1])
    #print column_num   #testing
    # read in columns
    str_out = "INSERT into " + str(tag_in[7:-5]) + " ("
    for i in range((int(column_num))):
        column.append(fd.readline())
        str_out += column[i][:-1]
        if i < column_num - 1:
            str_out += ", "
        #print column[i]    #testing
    str_out += ") VALUES "
    first = False
    # print values
    while line != '':
        if first is False:
            first = True
        else:
            str_out += ","
        str_out += "("
        for i in range(int(column_num)):
            line = fd.readline()
            #print line
            #data.append(line)
            if i == 5 or i == 6 or i == 7 or i == 13 or i == 14:
                str_out += line[:-1]
            else:
                str_out += '"' + line[:-1] + '"'
            if i < column_num - 1:
                str_out += ", "
        str_out += ")"
    str_out += ";"
    # read in data in for loop,
    # print out after every column_num
    # times
print str_out
