import tweepy
import time
import csv

with open('lltwitter_1.csv', 'wb') as f:
	my_writer = csv.DictWriter(f, fieldnames=("follower id", "screen name", "tweets", "total followers", "followers list", "first degree follower", "first degree friend", "second degree follower", "second degree friend"))
	my_writer.writeheader()

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

CWLL_Tourney = api.get_user('@910EasternRgnl')

def fd_follower_scraper(target):
	for i in tweepy.Cursor(api.followers, target).items():
		CWLL_Tourney_followers.append(i.id)

CWLL_Tourney_followers = []

fd_follower_scraper('@910EasternRgnl')

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
				

fd_followers_info_scraper(CWLL_Tourney_followers)

f = open('lltwitter_1.csv', 'rb')
my_reader = csv.DictReader(f, fieldnames=("follower id", "screen name", "tweets", "total followers", "followers list", "first degree follower", "first degree friend", "second degree follower", "second degree friend"))
fd_followers_list = []
fd_followers_expert_list = []
fd_followers_layman_list =[]

for i in my_reader:
	fd_followers_list.append(i)
fd_followers_list = fd_followers_list[1:len(fd_followers_list)]

fd_followers_most_active = max(fd_followers_list, key=lambda x:int(x['tweets']))
fd_followers_most_active

fd_followers_most_friends = max(fd_followers_list, key=lambda x:int(x['total followers']))
fd_followers_most_friends

for i in fd_followers_list:
	if int(i["total followers"])<1001 and int(i["tweets"])>100:
		fd_followers_expert_list.append(i)

for i in fd_followers_list:
	if int(i["total followers"])<101:
		fd_followers_layman_list.append(i)

def fd_friends_scraper(target):
	for i in tweepy.Cursor(api.friends, target).items():
		CWLL_Tourney_friends.append(i.id)

CWLL_Tourney_friends = []

fd_friends_scraper('@910EasternRgnl')

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
				
fd_friends_info_scraper(CWLL_Tourney_friends)

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

sd_followers = []

fd_targets = []

for i in fd_followers_expert_list:
	fd_targets.append(i["follower id"])

for i in fd_followers_layman_list:
	fd_targets.append(i["follower id"])
	
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

def sd_follower_scraper(target):
	for i in tweepy.Cursor(api.followers, target).items():
		sd_followers.append(i.id)
		print "successfully scraping"

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

sd_followers_info_scraper(sd_followers)

f = open('lltwitter_1.csv', 'rb')
my_reader = csv.DictReader(f, fieldnames=("follower id", "screen name", "tweets", "total followers", "followers list", "first degree follower", "first degree friend", "second degree follower", "second degree friend"))
sd_followers_list = []

for i in my_reader:
	if i["second degree follower"]=="True":
		sd_followers_list.append(i)
sd_followers_list = sd_followers_list[1:len(sd_followers_list)]

sd_followers_most_active = max(sd_followers_list, key=lambda x:int(x['tweets']))
sd_followers_most_active













sd_friends = []

fd_friends_targets = []

for i in fd_friends_expert_list:
	fd_friends_targets.append(i["follower id"])

for i in fd_friends_layman_list:
	fd_friends_targets.append(i["follower id"])
	
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
				
def sd_friend_scraper(target):
	for i in tweepy.Cursor(api.followers, target).items():
		sd_friends.append(i.id)
		
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

sd_friends_info_scraper(sd_friends)

f = open('lltwitter_1.csv', 'rb')
my_reader = csv.DictReader(f, fieldnames=("follower id", "screen name", "tweets", "total followers", "followers list", "first degree follower", "first degree friend", "second degree follower", "second degree friend"))
sd_friends_list = []

for i in my_reader:
	if i["second degree friend"]=="True":
		sd_friends_list.append(i)
sd_friends_list = sd_friends_list[1:len(sd_friends_list)]

sd_friends_most_active = max(sd_friends_list, key=lambda x:int(x['tweets']))
sd_friends_most_active