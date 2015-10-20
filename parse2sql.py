import sys

# from parsed tags to sql tags
def request_sql (tags, data, filename):
	# create table
	print filename
	print ("("),
	for i in range(len(tags)):
		print (tags[i]),
		if i != len(tags) - 1:
			print ("VARCHAR (100), "),
		else:
			print ("VARCHAR (100));")
	# insert rows
	print "INSERT INTO ", filename
	# print column titles
	print "(",
	for i in range(len(tags)):
		print (tags[i]),
		if i != len(tags) - 1:
			print (","),
		else:
			print (") VALUES")
	# print rows
	print ("("),
	for i in range(len(data)):
		print (data[i]),
		if i % len(tags) < len(tags) - 1:
			print (","),
		elif i != len(data) - 1:
			print ("),\n("),
		else:
			print "); "


# from parsed data to sql data
def response_sql (tags, data, filename):
	# set column start point
	start_pt = int(tags[0]) + 1

	print filename
	print ("("),
	#testing
	#print start_pt
	#end testing
	# create table
	for i in range(1, len(tags)):
		print (tags[i]),
		if i != len(tags) -1:
			print ("VARCHAR (100), "),
		else:
			print ("VARCHAR(100));")
	# insert rows
	print "INSERT INTO ", filename
	# print column titles
	print "(",
	for i in range(1, len(tags)):
		print (tags[i]),
		if i != len(tags) - 1:
			print (","),
		else:
			print (") VALUES")
	# print rows. 
	print ("("),
	for i in range(1, len(data)):
		if i % len(data) < start_pt:
			print data[i % len(data)]
			continue
		print (data[i]),
		if i % len(tags) < len(tags) - 1:
			print (","),
		elif i != len(data) - 1:
			print ("),\n("),
		else:
			print "); "


# main
tags = []
data = []

# fail on incorrect cli arguments
if len(sys.argv) < 3:
	sys.exit('Usage: %s tags-file data-file' % sys.argv[0])
#for i in range(1,len(sys.argv)):
#	if not os.path.exists(sys.argv[i]):
#		sys.exit('ERROR: %s does not exist' % sys.argv[i])

# open files, read in values	
with open(sys.argv[1], "r") as fd:
	for line in fd:
		tags.append(line)
with open (sys.argv[2], "r") as fd:
	for line in fd:
		data.append(line)
# remove newlines
for i in range(len(tags)):
	tags[i] = tags[i][:-1]
for i in range(len(data)):
	data[i] = data[i][:-1]

file_type = sys.argv[1][:-5:-1]
file_type = file_type[::-1]
# set filename
i = len(sys.argv[1]) - 1
while sys.argv[1][i] != '/':
	i -= 1
filename = sys.argv[1][i+1:-4]
#testing 
print filename
#end testing

# print sql commands
print "CREATE TABLE IF NOT EXISTS ", 

# call appropriate function based on filetype
if file_type == "form":
	filename += "request"
	request_sql(tags, data, filename)
elif file_type == "head":
	filename += "response"
	response_sql(tags, data, filename)
else:
	print "File type ", file_type, " not accepted."