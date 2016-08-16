#Go to https://polisci.wustl.edu/faculty/specialization

from bs4 import BeautifulSoup
import urllib2 
import random
import time
import os
import re
import csv

web_address='https://polisci.wustl.edu/faculty/specialization'
web_page = urllib2.urlopen(web_address)

# Parse it
soup = BeautifulSoup(web_page.read())
soup.prettify()

#Go to the page for each of the professors.

### Identify specializations
soup.find_all('h3')

#Create a .csv file with the following information for each professor:
# 	-Specialization
# 	-Name
# 	-Title
# 	-E-mail
# 	-Web page
	
faculty=soup.find_all('a',{'class':"person-view-primary-field" })
for i in range(0, len(faculty)):
		member = faculty[i]
		member_name = member.get_text()
		#member_name = member_name.replace('\n', ' ').replace('\r', '')
		member_page = "polisci.wustl.edu" + member['href']
		#member_page = member_page.replace('\n', ' ').replace('\r', '')
		#member_page_proper = urllib2.urlopen(member_page).read()
		#member_page_proper = BeautifulSoup(member_page_proper.read())
		#page_email=soup.find_all('a',{'href':"mailto" })
		if i ==0:
			with open('specializations.csv', 'w') as f:
				my_writer = csv.DictWriter(f, fieldnames=("Name", "Specialization", "Title", "Email", "Web page"))
				my_writer.writeheader()
				my_writer.writerow({"Name":member_name, "Web page":member_page})
		else:
			with open('specializations.csv', 'a+') as f:
				my_writer = csv.DictWriter(f, fieldnames=("Name", "Specialization", "Title", "Email", "Web page"))
				my_writer.writerow({"Name":member_name, "Web page":member_page})
				
###################################33
				
faculty_1=soup.find_all('div',{'class':"views-row"})	
for i in range(0, len(faculty_1)):
		faculty=faculty_1[i]
		member = faculty.find('a',{'class':"person-view-primary-field" })
		member_name = member.get_text()
		member_name = member_name.replace('\n', '')
		member_page = "http://polisci.wustl.edu" + member['href']
		member_title = faculty.get_text()
		#member_title = member_title.split("\n")
		member_title = member_title[2]
		member_title = member_title.replace(' ', '')
		#member_page = member_page.replace('\n', ' ')
		member_page_proper = urllib2.urlopen(member_page)
		member_page_proper = BeautifulSoup(member_page_proper.read())
		member_specialization = member_page_proper.find_all('a',{'property':"rdfs:label skos:prefLabel"})	
		for i in member_specialization:
			if i.get_text() != 'Faculty':
				member_specialization = i.get_text()
			else:
				member_specialization.remove(i)
		#page_email = member_page_proper.find_all('a',{'href':"mailto:"})
		#if "mailto:" in member_page_proper['href'] and "polisci@wustl.edu" not in member_page_proper['href']:
		#	page_email = page_email.get_text()
		#page_website=member_page_proper.find_all('div',{'class':"field field-name-field-person-website field-type-link-field field-label-inline clearfix"})
		#page_website=page_website.find('a')
		#if page_website != '':
		#	page_website = page_website
		#else:
		#	page_website = member_page 
		if i ==0:
			with open('specializations.csv', 'w') as f:
				my_writer = csv.DictWriter(f, fieldnames=("Name", "Specialization", "Title", "Email", "Web page"))
				my_writer.writeheader()
				my_writer.writerow({"Name":member_name, "Specialization":member_specialization, "Web page":member_page})
		else:
			with open('specializations.csv', 'a+') as f:
				my_writer = csv.DictWriter(f, fieldnames=("Name", "Specialization", "Title", "Email", "Web page"))
				my_writer.writerow({"Name":member_name, "Specialization":member_specialization, "Web page":member_page})