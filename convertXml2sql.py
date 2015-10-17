#!/usr/bin/python -B
from bs4 import BeautifulSoup as Soup
import sys

xml = open(sys.argv[1], "r")
for line in xml:
	soup = Soup (line, "xml")
	print soup.prettify()