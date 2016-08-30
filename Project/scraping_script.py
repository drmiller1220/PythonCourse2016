### Defining a class that will encode characters in unicode, as default csv class does not accommodate unicode in Windows

import csv, StringIO

class UnicodeWriter(object):
    """
    Like UnicodeDictWriter, but takes lists rather than dictionaries.
    
    Usage example:
    
    fp = open('my-file.csv', 'wb')
    writer = UnicodeWriter(fp)
    writer.writerows([
        [u'Bob', 22, 7],
        [u'Sue', 28, 6],
        [u'Ben', 31, 8],
        # \xc3\x80 is LATIN CAPITAL LETTER A WITH MACRON
        ['\xc4\x80dam'.decode('utf8'), 11, 4],
    ])
    fp.close()
    """
    def __init__(self, f, dialect=csv.excel_tab, encoding="utf-16", **kwds):
        # Redirect output to a queue
        self.queue = StringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoding = encoding
    
    def writerow(self, row):
        # Modified from original: now using unicode(s) to deal with e.g. ints
        self.writer.writerow([unicode(s).encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = data.encode(self.encoding)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)
    
    def writerows(self, rows):
        for row in rows:
            self.writerow(row)

class UnicodeDictWriter(UnicodeWriter):
    """
    A CSV writer that produces Excel-compatibly CSV files from unicode data.
    Uses UTF-16 and tabs as delimeters - it turns out this is the only way to
    get unicode data in to Excel using CSV.
    
    Usage example:
    
    fp = open('my-file.csv', 'wb')
    writer = UnicodeDictWriter(fp, ['name', 'age', 'shoesize'])
    writer.writerows([
        {'name': u'Bob', 'age': 22, 'shoesize': 7},
        {'name': u'Sue', 'age': 28, 'shoesize': 6},
        {'name': u'Ben', 'age': 31, 'shoesize': 8},
        # \xc3\x80 is LATIN CAPITAL LETTER A WITH MACRON
        {'name': '\xc4\x80dam'.decode('utf8'), 'age': 11, 'shoesize': 4},
    ])
    fp.close()
    
    Initially derived from http://docs.python.org/lib/csv-examples.html
    """
    
    def __init__(self, f, fields, dialect=csv.excel_tab,
            encoding="utf-16", **kwds):
        super(UnicodeDictWriter, self).__init__(f, dialect, encoding, **kwds)
        self.fields = fields
    
    def writerow(self, drow):
        row = [drow.get(field, '') for field in self.fields]
        super(UnicodeDictWriter, self).writerow(row)

### Importing necessary modules

from bs4 import BeautifulSoup
import urllib2
import csv 

### Creating a .csv file to store the targeted information

with open('weekly_speeches.csv', 'wb') as f:
	my_writer = UnicodeDictWriter(f, ["President_Full_Name", "President_Last_Name", "Date", "Title", "Text", "Note", "URL"])
	my_writer.writerow({"President_Full_Name": "President_Full_Name", "President_Last_Name": "President_Last_Name", "Date": "Date", "Title": "Title", "Text": "Text", "Note": "Note", "URL": "URL"})

### Identifying the html chunks which contain each of the address hyperlinks	

### Defining a function which will translate months expressed as strings to months expressed as two-digit numbers

def numerify_month(text_month):
	if text_month == 'January':
		return "01"
	elif text_month == 'February':
		return "02"
	elif text_month == 'March':
		return "03"
	elif text_month == 'April':
		return "04"
	elif text_month == 'May':
		return "05"
	elif text_month == 'June':
		return "06"
	elif text_month == 'July':
		return "07"
	elif text_month == 'August':
		return "08"
	elif text_month == 'September':
		return "09"
	elif text_month == 'October':
		return "10"
	elif text_month == 'November':
		return "11"
	elif text_month == 'December':
		return "12"
	else:
		print "Invalid value for month entered"

### Defining a function which will, once given the link to a given speech, obtain the speech title, speech text, and speech notes, as well as functions which will obtain those individual pieces of data

def address_page_extract(link):
	address_page=urllib2.urlopen(link)
	address_soup=BeautifulSoup(address_page.read())
	Title = get_address_title(address_soup)
	Text = get_address_text(address_soup)
	Note = get_address_note(address_soup)
	return Title, Text, Note		
		
def get_address_title(address_soup):
	paperstitle = address_soup.find('span', {'class':'paperstitle'})
	Title = paperstitle.get_text()
	return Title
	
def get_address_text(address_soup):
	displaytext = address_soup.find('span', {'class':'displaytext'})
	Text = displaytext.get_text()
	return Text
	
def get_address_note(address_soup):
	displaynotes = address_soup.find('span', {'class':'displaynotes'})
	Note = displaynotes.get_text()
	return Note


	

### Assigning targeted website to object, and scraping text from website

web_mainstem = 'http://www.presidency.ucsb.edu/satradio.php?year='
web_maintail = '&Submit=DISPLAY'
years = range(1982,2017)

for i in years:
	year_address = web_mainstem + str(i) + web_maintail
	web_page = urllib2.urlopen(year_address)
	soup = BeautifulSoup(web_page.read())
	address_segment=soup.find_all('tr', {'bgcolor':'#ffffff' or '#f7fafd'})
	for j in address_segment:
		main_line = j.get_text()
		President_Full_Name = main_line.split("\n")[1]
		President_Name_Parts = President_Full_Name.split(" ")
		President_Last_Name = President_Name_Parts[len(President_Name_Parts)-1]
		text_date = main_line.split("\n")[2]
		month = numerify_month(text_date.split()[0])
		day = text_date.split()[1]
		day = day.strip(',')
		year = text_date.split()[2]
		date_components = (month, day, year)
		date_delimiter = "/"
		Date = date_delimiter.join(date_components)
		address_page = j.find('a')['href']
		URL = "http://www.presidency.ucsb.edu" + address_page[2:]
		Title = address_page_extract(URL)[0]
		Text = address_page_extract(URL)[1]
		Note = address_page_extract(URL)[2]
		with open('weekly_speeches.csv', 'ab') as f:
			my_writer = UnicodeDictWriter(f, ["President_Full_Name", "President_Last_Name", "Date", "Title", "Text", "Note", "URL"])
			my_writer.writerow({"President_Full_Name": President_Full_Name, "President_Last_Name": President_Last_Name, "Date" : Date, "Title": Title, "Text": Text, "Note": Note, "URL": URL})

