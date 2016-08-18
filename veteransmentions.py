### Before running python, run the following line of code to
### set Sunlight API:
### $env:SUNLIGHT_API_KEY = "(Insert API Key)"

import sunlight
import csv 

from __future__ import print_function
from sunlight import capitolwords

with open('veterans_mentions.csv', 'wb') as f:
	my_writer = csv.DictWriter(f, fieldnames=("BioguideID","Veterans Mentions"))
	my_writer.writeheader()

for person in capitolwords.phrases_by_entity(
    "legislator",
    phrase="veterans",
    sort="count",
	per_page="50",
	page=10,
	start_date="2013-01-03",
	end_date="2013-11-13"
):
    with open('veterans_mentions.csv', 'ab') as f:
		my_writer = csv.DictWriter(f, fieldnames=("BioguideID","Veterans Mentions"))
		my_writer.writerow({"BioguideID": person['legislator'], "Veterans Mentions": person['count']})