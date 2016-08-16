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

with open('specializations.csv', 'w') as f:
				my_writer = csv.DictWriter(f, fieldnames=("Name", "Specialization", "Title", "Email", "Web page"))
				my_writer.writeheader()
				
faculty_1=soup.find_all('div',{'class':"views-row"})	
for i in range(0, len(faculty_1)):
		faculty=faculty_1[i]
		member = faculty.find('a',{'class':"person-view-primary-field" })
		member_name = member.get_text()
		member_name = member_name.replace('\n', '')
		member_page = "http://polisci.wustl.edu" + member['href']
		member_title = faculty.get_text()
		member_title = member_title.split("\n")
		member_title = member_title[2]
		member_title = member_title.replace(' ', '')
		#member_page = member_page.replace('\n', ' ')
		member_page_proper = urllib2.urlopen(member_page)
		member_page_proper = BeautifulSoup(member_page_proper.read())
		member_specialization_spots = member_page_proper.find_all('a',{'property':"rdfs:label skos:prefLabel"})	
		for i in member_specialization_spots:
			fields = ["Political Theory", "American", "Methodology", "Comparative", "International Political Economy", "Formal Theory"]
			if i.get_text() in fields:
				member_specialization = i.get_text()
		page_email_spot = member_page_proper.find("div",{'class':"field field-name-field-person-email field-type-email field-label-inline clearfix"})
		page_email_spot_2 = page_email_spot.find_all("div", {"class" : "field-item even"})
		for i in page_email_spot_2:
			if i.find("a",href=True):
				page_email = i.get_text()
		page_website_spot=member_page_proper.find('div',{'class':"field field-name-field-person-website field-type-link-field field-label-inline clearfix"})
		if page_website_spot:
			page_website = page_website_spot.find("a",href=True)['href']
		else:
			page_website = member_page
		#page_website=page_website.find('a')
		#if page_website != '':
		#	page_website = page_website
		#else:
		#	page_website = member_page 
		
		with open('specializations.csv', 'a') as f:
			my_writer = csv.DictWriter(f, fieldnames=("Name", "Specialization", "Title", "Email", "Web page"))
			my_writer.writerow({"Name":member_name, "Specialization":member_specialization, "Title":member_title, "Email": page_email, "Web page":page_website})