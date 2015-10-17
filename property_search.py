#!/usr/bin/python -B
# This program parses PropertySearch.xml files
# according to the xml2sql.schema scheme
from bs4 import BeautifulSoup as Soup
import sys

xml = open(sys.argv[1], "r")
prop_list = []
for line in xml:
    soup = Soup(line, "xml")
    # Property Search State -- lvl 1 children and Property
    prop_search = soup.find_all("PropertySearchState")
    for i in prop_search:
        # lvl 1 children
        for child in i.children:
            if child.string is not None:
                #print child.name, " ", child.string
                if child.name == "Token":
                    token_tag = child.string
#                    print token_tag
#        print "\n"
        # Property -- all children
        check_closed = False
        for child in i.children:
            if child.name == "Property":
                prop = child.children
                pr_name = ["Token"]
                pr_str = [token_tag]
                for j in prop:
                    # Property lvl 1 children
                    if j.string is not None:
                        pr_name.append(j.name)
                        pr_str.append(j.string)
                        # pad columns if "availStatus" = "open"
                        if j.name == "AvailabilityStatus":
                            if j.string == "Open":
                                pr_name.append("ClosedReason")
                                pr_str.append("None")
                            else:               # Disallow Closed status
                                pr_name = []
                                pr_str = []
                                break

#                        print j.name, " ", j.string
                    # Property lvl 2+ children
                    elif j.contents > 1:
                        for k in j.children:
                            pr_name.append(k.name)
                            pr_str.append(k.string)
#                            print k.name, " ", k.string
                    prop_list.append(pr_str)
                    if check_closed is False:
                        check_closed = True
#                print "\n"
#        print "\n"
#    print soup.prettify()
xml.close()
i = 0
'''while i < len(pr_name):
    print pr_name[i]
    i += 1
i = 0 '''
# flatten data list
new_pr_str = []
while i < len(prop_list):
    j = 0
    while j < len(prop_list[i]):
        #print prop_list[i][j]
        new_pr_str.append(prop_list[i][j])
        j += 1
    i += 1

print len(pr_name)  # print number of tags
# print tags
for i in pr_name:
    print i
# print data
i = 0
while i < len(new_pr_str):
    print new_pr_str[i]
    i += 1
