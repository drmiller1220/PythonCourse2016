### importing necessary modules

import tweepy
import time
import csv

### working interactively, insert necessary keys here:

#Get access to API
auth = tweepy.OAuthHandler('your consumer key', 'your consumer secret') ##Never put these in public code! Do NOT push keys to GitHub. Keep a private file that you can simply import
auth.set_access_token('your access token', 'your access token secret')    
api = tweepy.API(auth)

### create an empty CSV to store the data

with open('lltwitter_1.csv', 'wb') as f:
	my_writer = csv.DictWriter(f, fieldnames=("follower id", "screen name", "tweets", "total followers", "followers list", "first degree follower", "first degree friend", "second degree follower", "second degree friend"))
	my_writer.writeheader()

### create a function which will cope with the limits; function will
### run any Twitter-related function, and will sleep when a rate limit
### is hit,then try to run the function again	

def RateLimitHandler(cursor):
	not_finished = True
	while not_finished:
		try:
			yield cursor.next()
			print "successfully scraping"
			not_finished=False
		except tweepy.RateLimitError:
			time.sleep(1)
			print "sleeping"

api.rate_limit_status()

### obtaining the user information of the target account

CWLL_Tourney = api.get_user('@910EasternRgnl')

### creating a function which will obtain the user ID numbers
### for all first-degree followers of the target

def fd_follower_scraper(target):
	for i in tweepy.Cursor(api.followers, target).items():
		CWLL_Tourney_followers.append(i.id)

		
### Creating an empty list to store the FD followers, then scraping
### the ids of the FD followers

CWLL_Tourney_followers = []

fd_follower_scraper('@910EasternRgnl')

### creating a function which will scrape the user information for each
### FD follower.  For each user, the function will obtain their ID number,
### total number of tweets, total number of followers, and their screen name.
### The function will also mark that the user is a FD follower, and not a 
### FD friend, or SD follower or friend, with True/False statements.
### Then, the function wil write this information to the csv created
### above.

def fd_followers_info_scraper(idlist):
	for i in idlist:
		not_finished = True
		while not_finished:
			try:
				user = api.get_user(i)
				if user.protected == False:
					userid = user.id
					tweets = user.statuses_count
					followers = user.followers_count
					followerslist = user.followers_ids()
					screenname = user.screen_name
					fd_follower = True
					fd_friend=False
					sd_follower=False
					sd_friend=False
					with open('lltwitter_1.csv', 'ab') as f:
						my_writer = csv.DictWriter(f, fieldnames=("follower id", "screen name", "tweets", "total followers", "followers list", "first degree follower", "first degree friend", "second degree follower", "second degree friend"))
						my_writer.writerow ({"follower id":userid, "screen name": screenname, "tweets": tweets, "total followers": followers, #"followers list": followerslist, 
							"first degree follower": fd_follower, "first degree friend": fd_friend, "second degree follower": sd_follower, "second degree friend": sd_friend})		
					print "successfully scraping"
				not_finished=False
			except tweepy.RateLimitError:
				time.sleep(1*60)
				print "sleeping"
				

### Running the user info scraping function

fd_followers_info_scraper(CWLL_Tourney_followers)

### Once information has been collected, opening the csv to find
### the most active and most popular users.

f = open('lltwitter_1.csv', 'rb')
my_reader = csv.DictReader(f, fieldnames=("follower id", "screen name", "tweets", "total followers", "followers list", "first degree follower", "first degree friend", "second degree follower", "second degree friend"))

### creating an empty list to insert the user dictionaries into from
### the csv.  Creating empty lists for experts and laymen to facilitate
### next step with SD followers.

fd_followers_list = []
fd_followers_expert_list = []
fd_followers_layman_list =[]

### inserting the user dictionaries from the CSV

for i in my_reader:
	fd_followers_list.append(i)
fd_followers_list = fd_followers_list[1:len(fd_followers_list)]

### finding the most active folower

fd_followers_most_active = max(fd_followers_list, key=lambda x:int(x['tweets']))
fd_followers_most_active

### finding the most popular follower

fd_followers_most_friends = max(fd_followers_list, key=lambda x:int(x['total followers']))
fd_followers_most_friends

### obtaining lists of expert and layman followers to facilitate SD search

for i in fd_followers_list:
	if int(i["total followers"])<1001 and int(i["tweets"])>100:
		fd_followers_expert_list.append(i)

for i in fd_followers_list:
	if int(i["total followers"])<101:
		fd_followers_layman_list.append(i)

### creating a function to scrape FD friends		

def fd_friends_scraper(target):
	for i in tweepy.Cursor(api.friends, target).items():
		CWLL_Tourney_friends.append(i.id)

### creating an empty list to score FD friends
		
CWLL_Tourney_friends = []

### executing the function to scrape for FD friends.

fd_friends_scraper('@910EasternRgnl')

### creating a function to scrape the user info for FD friends.  Works
### identically to the function to scrape user infor for FD followers.

def fd_friends_info_scraper(idlist):
	for i in idlist:
		not_finished = True
		while not_finished:
			try:
				user = api.get_user(i)
				if user.protected == False:
					userid = user.id
					tweets = user.statuses_count
					followers = user.followers_count
					followerslist = user.followers_ids()
					screenname = user.screen_name
					fd_follower = False
					fd_friend=True
					sd_follower=False
					sd_friend=False
					with open('lltwitter_1.csv', 'ab') as f:
						my_writer = csv.DictWriter(f, fieldnames=("follower id", "screen name", "tweets", "total followers", "followers list", "first degree follower", "first degree friend", "second degree follower", "second degree friend"))
						my_writer.writerow ({"follower id":userid, "screen name": screenname, "tweets": tweets, "total followers": followers, #"followers list": followerslist, 
							"first degree follower": fd_follower, "first degree friend": fd_friend, "second degree follower": sd_follower, "second degree friend": sd_friend})		
					print "successfully scraping"
				not_finished=False
			except tweepy.RateLimitError:
				time.sleep(1*60)
				print "sleeping"

### executing the function
				
fd_friends_info_scraper(CWLL_Tourney_friends)

### opening the csv to identify friends that are most active and most
### popular.  Because we need to subset celebrities/experts/friends,
### the main difference between how this step is executed here as to
### how it was executed with FD followers is that we use for loops
### to subset on the basis of the true/false values

f = open('lltwitter_1.csv', 'rb')
my_reader = csv.DictReader(f, fieldnames=("follower id", "screen name", "tweets", "total followers", "followers list", "first degree follower", "first degree friend", "second degree follower", "second degree friend"))

fd_friends_list = []
fd_friends_expert_list = []
fd_friends_layman_list =[]
fd_friends_celebrity_list = []

for i in my_reader:
	if i["first degree friend"]=="True":
		fd_friends_list.append(i)
fd_friends_list = fd_friends_list[1:len(fd_friends_list)]

for i in fd_friends_list:
	if int(i["total followers"])>1000:
		fd_friends_celebrity_list.append(i)

for i in fd_friends_list:
	if int(i["total followers"])<1001 and int(i["tweets"])>100:
		fd_friends_expert_list.append(i)

for i in fd_friends_list:
	if int(i["total followers"])<101:
		fd_friends_layman_list.append(i)


fd_friends_most_friends = max(fd_friends_list, key=lambda x:int(x['total followers']))
fd_friends_most_friends

fd_friends_most_active_celebrity = max(fd_friends_celebrity_list, key=lambda x:int(x['tweets']))
fd_friends_most_active_celebrity
fd_friends_most_active_expert = max(fd_friends_expert_list, key=lambda x:int(x['tweets']))
fd_friends_most_active_expert
fd_friends_most_active_layman = max(fd_friends_layman_list, key=lambda x:int(x['tweets']))
fd_friends_most_active_layman

############################

### starting the process for SD followers/friends

### creating empty lists in which to store the ids of FD followers who
### are experts and laymen, and to store the ids of SD followers

sd_followers = []

fd_targets = []

for i in fd_followers_expert_list:
	fd_targets.append(i["follower id"])

for i in fd_followers_layman_list:
	fd_targets.append(i["follower id"])

### function which will scrape user info for SD followers.  Works the
### same as analogous functions above for FD friends/followers	

def sd_followers_info_scraper(idlist):
	for i in idlist:
		not_finished = True
		while not_finished:
			try:
				user = api.get_user(int(i))
				if user.protected == False:
					userid = user.id
					tweets = user.statuses_count
					followers = user.followers_count
					followerslist = user.followers_ids()
					screenname = user.screen_name
					fd_follower = False
					fd_friend=False
					sd_follower=True
					sd_friend=False
					with open('lltwitter_1.csv', 'ab') as f:
						my_writer = csv.DictWriter(f, fieldnames=("follower id", "screen name", "tweets", "total followers", "followers list", "first degree follower", "first degree friend", "second degree follower", "second degree friend"))
						my_writer.writerow ({"follower id":userid, "screen name": screenname, "tweets": tweets, "total followers": followers, #"followers list": followerslist, 
							"first degree follower": fd_follower, "first degree friend": fd_friend, "second degree follower": sd_follower, "second degree friend": sd_friend})		
					print "successfully scraping"
				not_finished=False
			except tweepy.RateLimitError:
				time.sleep(1*60)
				print "sleeping"

### function which will scrape the ids of all followers for each
### FD follower				
				
def sd_follower_scraper(target):
	for i in tweepy.Cursor(api.followers, target).items():
		sd_followers.append(i.id)
		print "successfully scraping"

### for loop which will scrape the user ids of all SD followers, with
### accounting for rate limits		
		
for i in fd_targets:
	not_finished = True
	while not_finished:
		try:
			sd_follower_scraper(i)
			not_finished=False
			print "successfully scraping in loop"
		except tweepy.RateLimitError:
			time.sleep(1*60)
			print "sleeping"

### scraping the user info for SD followers			

sd_followers_info_scraper(sd_followers)

### similarly to the process for FD followers, using the csv to identify the
### most active SD follower

f = open('lltwitter_1.csv', 'rb')
my_reader = csv.DictReader(f, fieldnames=("follower id", "screen name", "tweets", "total followers", "followers list", "first degree follower", "first degree friend", "second degree follower", "second degree friend"))
sd_followers_list = []

for i in my_reader:
	if i["second degree follower"]=="True":
		sd_followers_list.append(i)
sd_followers_list = sd_followers_list[1:len(sd_followers_list)]

sd_followers_most_active = max(sd_followers_list, key=lambda x:int(x['tweets']))
sd_followers_most_active



### creating empty lists in which to store the ids of FD friends and
### the friends of those FD friends (SD friends), and adding the
### ids of expert/layman friends to the list of FD friends


sd_friends = []

fd_friends_targets = []

for i in fd_friends_expert_list:
	fd_friends_targets.append(i["follower id"])

for i in fd_friends_layman_list:
	fd_friends_targets.append(i["follower id"])

### function which will scrape user info for SD friends.  Works the
### same as analogous functions above for FD friends/followers
	
def sd_friends_info_scraper(idlist):
	for i in idlist:
		not_finished = True
		while not_finished:
			try:
				user = api.get_user(int(i))
				if user.protected == False:
					userid = user.id
					tweets = user.statuses_count
					followers = user.followers_count
					followerslist = user.followers_ids()
					screenname = user.screen_name
					fd_follower = False
					fd_friend=False
					sd_follower=False
					sd_friend=True
					with open('lltwitter_1.csv', 'ab') as f:
						my_writer = csv.DictWriter(f, fieldnames=("follower id", "screen name", "tweets", "total followers", "followers list", "first degree follower", "first degree friend", "second degree follower", "second degree friend"))
						my_writer.writerow ({"follower id":userid, "screen name": screenname, "tweets": tweets, "total followers": followers, #"followers list": followerslist, 
							"first degree follower": fd_follower, "first degree friend": fd_friend, "second degree follower": sd_follower, "second degree friend": sd_friend})		
					print "successfully scraping"
				not_finished=False
			except tweepy.RateLimitError:
				time.sleep(1*60)
				print "sleeping"

### function which will scrape the ids of all friends for each
### FD friend
				
def sd_friend_scraper(target):
	for i in tweepy.Cursor(api.friends, target).items():
		sd_friends.append(i.id)
		print "successfully scraping"

### for loop which will scrape the user ids of all SD friends, with
### accounting for rate limits	
		
for i in fd_friends_targets:
	not_finished = True
	while not_finished:
		try:
			sd_friend_scraper(i)
			print "successfully scraping"
			not_finished=False
		except tweepy.RateLimitError:
			time.sleep(1*60)
			print "sleeping"

### scraping the user info for SD friends				

sd_friends_info_scraper(sd_friends)

### similarly to the process for FD friends, using the csv to identify the
### most active SD friends

f = open('lltwitter_1.csv', 'rb')
my_reader = csv.DictReader(f, fieldnames=("follower id", "screen name", "tweets", "total followers", "followers list", "first degree follower", "first degree friend", "second degree follower", "second degree friend"))
sd_friends_list = []

for i in my_reader:
	if i["second degree friend"]=="True":
		sd_friends_list.append(i)
sd_friends_list = sd_friends_list[1:len(sd_friends_list)]

sd_friends_most_active = max(sd_friends_list, key=lambda x:int(x['tweets']))
sd_friends_most_active