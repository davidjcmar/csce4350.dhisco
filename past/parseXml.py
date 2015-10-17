#!/usr/bin/python -B
import sys
import aux_funcs
from bs4 import BeautifulSoup

assert (len(sys.argv) > 1), "Parsing requires a filepath as an argument."

i = 1
while i < len(sys.argv):
    # test input 
    try:
        xml = open(sys.argv[i], "r")
    except:
        print sys.argv[i], " is not a valid filepath."
        break
    # soupify
    soup = BeautifulSoup(xml,'xml')
    # set filename for tag and data files
    f_tag = "./tags/"
    f_data = "./data/"
    f_tag = f_tag + aux_funcs.set_filename(sys.argv[i], ".tags")
    f_data = f_data + aux_funcs.set_filename(sys.argv[i], ".data")
    print f_tag, " ", f_data  #testing
    # open tag/data file descriptors for write
    fd_tag = open(f_tag, "w")
    fd_data = open(f_data, "w")

    # soupify
    id_soup = soup.hotelml
    tag_list = []
    #get tag list
    while id_soup.next_element != None:
        # if string (leaf tag) write id.parent.name (tag)
        if id_soup.name == None:
            par_id = id_soup.parent
            temp_id = "<"
            temp_id = temp_id + par_id.name
            temp_id = temp_id + ">"
            tag_list.append(temp_id)
        id_soup = id_soup.next_element

    # remove duplicates from tag listing
    tag_list=aux_funcs.remove_dups(tag_list)

    #write tags to file
    for id in tag_list:
        fd_tag.write(id)
        fd_tag.write("\n")

    #get data list
    id_soup = soup.hotelml
    id = 0
    while id_soup.next_element != None:
        # if string (leaf) write id.name (data)
        if id_soup.name == None:
            # write tag
            fd_data.write(str(id))   #testing
            fd_data.write(" ") #testing
            fd_data.write(str(len(tag_list)))    #testing
            fd_data.write(" ")  #testing
            fd_data.write(str(id % len(tag_list)))  #testing
            fd_data.write(" ")  #testing
            fd_data.write(tag_list[id % len(tag_list)])
            fd_data.write("\t")
            # write data
            fd_data.write(id_soup.string)
            fd_data.write("\n")
            id += 1
        id_soup = id_soup.next_element
    # close file descriptors
    fd_tag.close()
    fd_data.close()
    i += 1
    #end while i < len(sys.argv)
