from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import datetime
import requests
from requests_oauthlib import OAuth1
from lxml import html
import re
import json

# You don't need this import if you're going to have your keys in the same file
from keys import ckey, csecret, atoken, asecret, PBAccessToken

class listener(StreamListener):

	'''
		This is Tweetpy. We just override the class and
		set the streamlistener. Pretty straightforward.

	'''

	def on_data(self, data):

		'''
			If a tweet happens gets the data, strips the text.
			Checks whether it's relevant. If it isn't, do nothing.
			If it is, get the Twitlonger post ID and call the
			scrap_twitlonger function passing it said ID.
			Then call the send_to_pushbullet function to send 
			the notification.

		'''
		try:
		    tweet = data.split(',"text":"')[1].split('","source":')[0]
		    print tweet
		    if tweet.find('será necesario restringir') > 0:
			    twitlonger = tweet.split('tl.gd/')[1]
			    message = scrap_twitlonger(twitlonger)
				send_to_pushbullet(message)
			return True
		except BaseException, e:
			print "Given error was spotted " + str(e)

	def on_error(self, status):
	    print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
USER_ID = '1201975304'
twitterStream.filter(follow=[USER_ID])


def scrap_twitlonger(twitlonger):
	''' 
		Takes a twitlonger post ID, scraps the body of the post
		and then returns a string depending on the contents of 
		the post. If the hour is stated in said post, it's added
		If it's not, then it's implied it's current time.

		Note to self: Implement GMT - whatever our president
		decides to change it to.
	'''
	page = requests.get('http://www.twitlonger.com/show/%s' %twitlonger)
	tree = html.fromstring(page.content)
	texto = tree.xpath('/html/body/div[2]/div[1]/div[3]/div/p[1]/text()')
	hora = re.search('[0-9]+:[0-9]+',texto[0])
	circuitos = texto[0].split(str('detallados a continuación: ').decode('utf-8'))[1].split(str(' #ElNiñoNoEsJuego').decode('utf-8'))[0]
	if hora:
		return "La luz se ira a las " + hora.group(0) + " en " + circuitos
	else:
		hora = re.search('En momentos',texto[0])
		if hora:
			return "La luz se ira a las " + str(datetime.datetime.now().time()) + " en " + circuitos

def send_to_pushbullet(message, PBAccessToken):

	'''
		Takes a PushBullet Access-Token API and returns
		an error if anything goes wrong.
		Takes whatever message is passed through the
		parameter and sends it to every device connected
		to your PushBullet account.

		Note to self: Implement the ability to choose
		what device you want to send it to. 

	'''

	try:
		data = json.dumps({"type": "note",
			"title": "Anuncio de Luz",
			"body": message})
		resp = requests.post(
			'https://api.pushbullet.com/v2/pushes', 
			headers={"Authorization": 'Bearer '+ PBAccessToken,
			"Content-Type": "application/json"}, 
			data=data)
	except BaseException, e:
		print "Given error: " + str(e)

