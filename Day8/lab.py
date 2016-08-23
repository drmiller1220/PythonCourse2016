import re

# open text file of 2008 NH primary Obama speech
file = open("obama-nh.txt", "r")
text = file.readlines()
file.close()

# compile the regular expression
keyword = re.compile(r"the ")

# search file for keyword, line by line
for line in text:
  if keyword.search(line):
    print line 



# TODO: print all lines that DO NOT contain "the "

not_the = re.compile(r"^((?!the).)*$")

for line_1 in text:
  if not_the.search(line_1):
    print line_1

# TODO: print lines that contain a word of any length starting with s and ending with e

s_e = re.compile(r'\bs*.e\b')

for line_2 in text:
  if s_e.search(line_2):
    print line_2

# date = raw_input("Please enter a date in the format MM.DD.YY: ")
# Print the date input in the following format:
# Month: MM
# Day: DD
# Year: YY

date = "05.07.12"

pattern = re.compile(r'(\d\d).(\d\d).(\d\d)')
mysearch=pattern.search(date)
mysearch.groups() #list of all groups
mysearch.group(0) #the complete match
mysearch.group(1) #the first group
mysearch.group(2) #the second group
mysearch.group(3) #the third group

	print "Month: %s" % mysearch.group(1)
	print "Day: %s" % mysearch.group(2)
	print "Year: %s" % mysearch.group(3)

# TODO: Write a regular expression that finds html tags in example.html and print them.

# TODO: Scrape a website and search for some things...


