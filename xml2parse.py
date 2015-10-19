#!/usr/bin/python -B
from bs4 import BeautifulSoup as Soup
import sys

xml = open(sys.argv[1], "r")

# containers for specified tags in ./tags
tags_form = []
tags_head = []
# output files
form_parsed = sys.argv[4] + ".request"
head_parsed = sys.argv[4] + ".response"
# open form tags file
with open(sys.argv[2], "r") as fp:
	for line in fp:
		tags_form.append(line)
# open head tags file
with open(sys.argv[3], "r") as fp:
	for line in fp:
		tags_head.append(line)

# remove newlines
for i in range(len(tags_form)):
	tags_form[i] = tags_form[i][:-1]
#	print i, " ", tags_form[i]
for i in range(len(tags_head)):
	tags_head[i] = tags_head[i][:-1]
#	print i, " ", tags_head[i]

for line in xml:
	temp_form = []
	temp_head = []
	soup = Soup (line, "xml")
#testing
#	print soup.prettify()
#end testing
	head = soup.HotelML
	tag = head.contents[0]
#testing	
#	print tag.name		
#	for child in tag.children:
#		print child, "\n"
#	print head.name		
#end testing
	# parse form tags
	if tag.name == "Form":
		tag = tag.parent
		form_it = 0
		for child in tag.descendants:
			# tags are leaf tags, contain string values
			if child.string is not None:
				# expected tag
				if child.name == tags_form[form_it % len(tags_form)]:
					temp_form.append(child.string)
					form_it += 1
				# out of order tag, ignore
				else:
					for i in range(form_it, len(tags_form)):
						if child.name == tags_form[i]:
							temp_form.append("NULL")
							form_it += 1
							break
				if form_it == len(tags_form):
					form_it = 0

	#parse head tags
	else:
		tag = tag.parent
#		print tag.name
		head_it = 1 # set start position including header only tags
		# read in tags
		for child in tag.descendants:
#			print child.name
			# tags are leaf tags, contain string values
			if child.string is not None:
				# expected tag
				if child.name == tags_head[head_it]:
					temp_head.append(child.string)
					head_it += 1
				# out of order tag, ignore
				else:
					for i in range(head_it, len(tags_head)):
						if child.name == tags_head[i]:
							temp_head.append("NULL")
							head_it += 1
							break
				# reset counter
				if head_it == len(tags_head):
					head_it = int(tags_head[0]) + 1
	# append to file
	with open(form_parsed, "a") as fd:
		for i in temp_form:
			fd.write(i)
			fd.write("\n")
	with open(head_parsed, "a") as fd:
		for i in temp_head:
			fd.write(i)
			fd.write("\n")
# testing
#	for j in temp_form:
#		print "form: ", j
#	for j in temp_head:
#		print "head: ",j
# end testing
