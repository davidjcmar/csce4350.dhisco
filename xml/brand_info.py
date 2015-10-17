#!/usr/bin/python -B
# This program parses BrandInformation.xml files
# according to the xml2sql.schema scheme
from bs4 import BeautifulSoup as Soup
import sys

xml = open(sys.argv[1], "r")
brand_list = []
for line in xml:
    soup = Soup(line, "xml")
    brand = soup.find_all("Brand")
    for i in brand:
        if len(i.contents) > 1:
            ch_name = []    # tags
            ch_str = []     # strings buffer
#            print "brand: ", str(len(i.contents))  #testing
            for child in i.children:
                if child.string is not None:
                    ch_name.append(child.name)
                    ch_str.append(child.string)
#                    print child.name, " ", child.string    #testing
#            print "\n"
            brand_list.append(ch_str)   # strings full list

i = 0
new_tag = []    # final tags
new_data = []   # final data
# cut email tag
while i < len(ch_name):
    if ch_name[i] != 'Email':
        new_tag.append(ch_name[i])
    i += 1
# cut email data and flatten data list
i = 0
while i < len(brand_list):
    j = 0
    while j < len(brand_list[i]):
        if ch_name[j] != 'Email':
            new_data.append(brand_list[i][j])
        j += 1
    i += 1
print len(new_tag)  # print number of tags
# print tags
for i in new_tag:
    print i
# print data
i = 0
while i < len(new_data):
    print new_data[i]
    i += 1
