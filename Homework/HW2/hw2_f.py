### Changing the default encoding the wrong way, because the "right way"
### would not work.  Commands at end of script return default encoding
### to ASCII.

import sys
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

### Strategy to complete lab:

### From main page, want to select every "ul" segment where
### "class="node-readmore first last"".  Then, find the "href"
### segment within the "ul" segment, and the value of the segment
### is the link for the petition.

### Then, on every petition page, want to find the "h1" segment,
### and the text of this segment is the petition title.

### Then, find the "h4" segment where class="petition-attribution",
### and select the text in the string after the word "on."  This
### text segment includes the date on which the petition was
### published

### Then, find the "span" segment where class="signatures-number",
### and the text is the number of signatures that the petition has.

### Then, find the "div" segment where 
### "class="field field-name-field-petition-issues field-type-taxonomy-term-reference field-label-hidden tags""
### Within those divs, find all "h6" segments, and the text within
### each of those segments is the issue tags for the petition.

### Importing necessary modules

from bs4 import BeautifulSoup
import urllib2
import csv 

### Assigning targeted website to object, and scraping text from website

web_address='https://petitions.whitehouse.gov/'
web_page = urllib2.urlopen(web_address)
soup = BeautifulSoup(web_page.read())

### Creating a .csv file to store the targeted information

with open('whpetitions.csv', 'wb') as f:
	my_writer = csv.DictWriter(f, fieldnames=("Title", "Date", "Number of Signatures", "Issue Tags"))
	my_writer.writeheader()

### Identifying the html chunks which contain each of the individual petitions	

petition_segment=soup.find_all('ul', {'class' : 'links inline'})

### Creating an empty list to store the web addresses of each petition
petition_addresses = []

### For loop which obtains the web addresses of each petition and stores
### them in the empty list created above

for i in petition_segment:
	address_segment = i.find('a')
	petition_address =  "https://petitions.whitehouse.gov" + address_segment['href']
	petition_addresses.append(petition_address)

### Creating a function which will obtain the petition title from
### each petition page	

def get_petition_title(petition_soup):
	h1 = petition_soup.find('h1')
	petition_page_title = h1.get_text()
	return petition_page_title
	
### Creating a function which will obtain the petition date from
### each petition page.  Commented out text can be used to obtain
### day, month, and year separately, if so desired (though additional
### coding would be needed to get those separate values to print out
### in the csv).
	
def get_petition_date(petition_soup):
	h4 = petition_soup.find('h4', {'class' : 'petition-attribution'})
	petition_attribution = h4.get_text()
	petition_page_date = petition_attribution.split("on ")[1]
	#petition_month = petition_date.split(" ")[0]
	#petition_day = petition_date.split(" ")[1]
	#petition_day = petition_day.strip(',')
	#petition_year = petition_date.split(" ")[2]
	return petition_page_date
	
### Creating a function which will obtain the petition signatures from
### each petition page

def get_petition_signatures(petition_soup):
	span = petition_soup.find('span', {'class' : 'signatures-number'})
	petition_page_signatures = span.get_text()
	petition_page_signatures = petition_page_signatures.replace(',','')
	return petition_page_signatures

### Creating a function which will obtain the petition tags from
### each petition page

def get_petition_tags(petition_soup):
	petition_page_tags = []
	div = petition_soup.find('div', {'class' : 'field field-name-field-petition-issues field-type-taxonomy-term-reference field-label-hidden tags'})
	h6 = div.find_all('h6')
	for i in h6:
		petition_page_tags.append(i.get_text())
	if len(petition_page_tags)>1:
		petition_page_tags = ", ".join(petition_page_tags)
	else:
		petition_page_tags = str(petition_page_tags[0])
	return petition_page_tags
	
### Creating a function which will use the functions above to obtain
### the petition title, date, number of signatures, and issue tags
### for a petition entered into the function

def petition_info(petition_addresses):
	petition_page=urllib2.urlopen(petition_addresses)
	petition_soup=BeautifulSoup(petition_page.read())
	petition_title=get_petition_title(petition_soup)
	petition_date=get_petition_date(petition_soup)
	petition_signatures=get_petition_signatures(petition_soup)
	petition_tags=get_petition_tags(petition_soup)
	with open('whpetitions.csv', 'ab') as f:
		my_writer = csv.DictWriter(f, fieldnames=("Title", "Date", "Number of Signatures", "Issue Tags"))
		my_writer.writerow({"Title": petition_title, "Date": petition_date, "Number of Signatures": petition_signatures, "Issue Tags": petition_tags})

### Creating a for loop which will create the desired csv
		
for i in petition_addresses:
	try:
		petition_info(i)
	except:
		pass



for i in petition_addresses:
	petition_page=urllib2.urlopen(i)
	petition_soup=BeautifulSoup(petition_page.read())
	petition_page_title = 'NA'
	petition_page_date = 'NA'
	petition_page_signatures = 'NA'
	petition_page_tags = []
	h1 = petition_soup.find('h1')
	petition_title = h1.get_text()
	petition_title = petition_title.replace('\n','')
	h4 = petition_soup.find('h4', {'class' : 'petition-attribution'})
	petition_attribution = h4.get_text()
	petition_date = petition_attribution.split("on ")[1]
	petition_month = petition_date.split(" ")[0]
	petition_day = petition_date.split(" ")[1]
	petition_day = petition_day.strip(',')
	petition_year = petition_date.split(" ")[2]
	span = petition_soup.find('span', {'class' : 'signatures-number'})
	signatures = span.get_text()
	signatures = signatures.replace(',','')
	div = petition_soup.find('div', {'class' : 'field field-name-field-petition-issues field-type-taxonomy-term-reference field-label-hidden tags'})
	h6 = div.find_all('h6')
	for i in h6:
		petition_page_tags.append(i.get_text())
	if len(petition_page_tags)>1:
		petition_page_tags = ", ".join(petition_page_tags)
	else:
		petition_page_tags = str(petition_page_tags[0])
	with open('whpetitions.csv', 'ab') as f:
		my_writer = csv.DictWriter(f, fieldnames=("Title", "Date", "Number of Signatures", "Issue Tags"))
		my_writer.writerow({"Title": petition_title, "Date": petition_date, "Number of Signatures": signatures, "Issue Tags": petition_page_tags})


		
import sys
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('ASCII')