import tweepy
import time
import operator
import csv 

#Check the documentation page
#http://docs.tweepy.org/en/v3.2.0/

#Get access to API
auth = tweepy.OAuthHandler('your consumer key', 'your consumer secret') ##Never put these in public code! Do NOT push keys to GitHub. Keep a private file that you can simply import
auth.set_access_token('your access token', 'your access token secret')    
api = tweepy.API(auth)

#See rate limit
api.rate_limit_status()

with open('lltwitter.csv', 'wb') as f:
	my_writer = csv.DictWriter(f, fieldnames=("follower id", "screen name", "tweets", "total followers", "followers list", "first degree follower", "first degree friend", "second degree follower", "second degree friend"))
	my_writer.writeheader()

CWLL_Tourney = api.get_user('@910EasternRgnl')

for follower_id in CWLL_Tourney.followers_ids():
	user = api.get_user(follower_id)
	userid = user.id
	tweets = user.statuses_count
	followers = user.followers_count
	#followerslist = user.followers_ids()
	screenname = user.screen_name
	fd_follower = True
	fd_friend=False
	sd_follower=False
	sd_friend=False
	with open('lltwitter.csv', 'ab') as f:
		my_writer = csv.DictWriter(f, fieldnames=("follower id", "screen name", "tweets", "total followers", "followers list", "first degree follower", "first degree friend", "second degree follower", "second degree friend"))
		my_writer.writerow ({"follower id":userid, "screen name": screenname, "tweets": tweets, "total followers": followers, #"followers list": followerslist, 
		"first degree follower": fd_follower, "first degree friend": fd_friend, "second degree follower": sd_follower, "second degree friend": sd_friend})

for follower_id in CWLL_Tourney.followers_ids():
    not_finished=True
    while not_finished:
        try:
			user = api.get_user(follower_id)
			userid = user.id
			tweets = user.statuses_count
			followers = user.followers_count
			#followerslist = user.followers_ids()
			screenname = user.screen_name
			fd_follower = True
			fd_friend=False
			sd_follower=False
			sd_friend=False
			with open('lltwitter.csv', 'ab') as f:
				my_writer = csv.DictWriter(f, fieldnames=("follower id", "screen name", "tweets", "total followers", "followers list", "first degree follower", "first degree friend", "second degree follower", "second degree friend"))
				my_writer.writerow ({"follower id":userid, "screen name": screenname, "tweets": tweets, "total followers": followers, #"followers list": followerslist, 
				"first degree follower": fd_follower, "first degree friend": fd_friend, "second degree follower": sd_follower, "second degree friend": sd_friend})
			not_finished=False
        except:
            time.sleep(1)		

for friend_id in CWLL_Tourney.friends_ids():
	not_finished=True
	while not_finished:
        try:
			user = api.get_user(friends_id)
			userid = user.id
			tweets = user.statuses_count
			followers = user.followers_count
			#followerslist = user.followers_ids()
			screenname = user.screen_name
			fd_follower=False
			fd_friend = True
			sd_follower=False
			sd_friend=False
			with open('lltwitter.csv', 'ab') as f:
				my_writer = csv.DictWriter(f, fieldnames=("follower id", "screen name", "tweets", "total followers", "followers list", "first degree follower", "first degree friend", "second degree follower", "second degree friend"))
				my_writer.writerow ({"follower id":userid, "screen name": screenname, "tweets": tweets, "total followers": followers, #"followers list": followerslist, 
				"first degree follower": fd_follower, "first degree friend": fd_friend, "second degree follower": sd_follower, "second degree friend": sd_friend})
			not_finished=False
        except:
            time.sleep(1)
				
for i in :
	if i.followers_count <1001:
		for follower_id in i.followers_ids():
			user = api.get_user(follower_id)
			userid = user.id
			tweets = user.statuses_count
			followers = user.followers_count
			#followerslist = user.followers_ids()
			screenname = user.screen_name
			fd_follower = False
			fd_friend=False
			sd_follower=True
			sd_friend=False
			with open('lltwitter.csv', 'ab') as f:
				my_writer = csv.DictWriter(f, fieldnames=("follower id", "screen name", "tweets", "total followers", "followers list", "first degree follower", "first degree friend", "second degree follower", "second degree friend"))
				my_writer.writerow ({"follower id":userid, "screen name": screenname, "tweets": tweets, "total followers": followers, #"followers list": followerslist, 
				"first degree follower": fd_follower, "first degree friend": fd_friend, "second degree follower": sd_follower, "second degree friend": sd_friend})

for i in :
	if i.friends_count <1001:
		for follower_id in i.followers_ids():
			user = api.get_user(follower_id)
			userid = user.id
			tweets = user.statuses_count
			followers = user.followers_count
			#followerslist = user.followers_ids()
			screenname = user.screen_name
			fd_follower = False
			fd_friend=False
			sd_follower=False
			sd_friend=True
			with open('lltwitter.csv', 'ab') as f:
				my_writer = csv.DictWriter(f, fieldnames=("follower id", "screen name", "tweets", "total followers", "followers list", "first degree follower", "first degree friend", "second degree follower", "second degree friend"))
				my_writer.writerow ({"follower id":userid, "screen name": screenname, "tweets": tweets, "total followers": followers, #"followers list": followerslist, 
				"first degree follower": fd_follower, "first degree friend": fd_friend, "second degree follower": sd_follower, "second degree friend": sd_friend})	
		
		
		
		
		
		
		
f = open('lltwitter.csv', 'rb')
my_reader = csv.DictReader(f, fieldnames=("follower id", "screen name", "tweets", "total followers", "followers list", "first degree follower", "first degree friend", "second degree follower", "second degree friend"))
	