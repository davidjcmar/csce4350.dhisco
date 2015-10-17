#!/usr/bin/python -B
# This program prints a pretty schema for any hotelml file
from bs4 import BeautifulSoup as Soup
import sys

xml = open(sys.argv[1], "r")
for line in xml:
    soup = Soup(line, "xml")
    print soup.prettify()
