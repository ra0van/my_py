from rauth.service import OAuth1Service, OAuth1Session
import json
from pprint import pprint
import urllib2

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

def main():
	session = GetSession()

	print 'ENter search key:'
	q = raw_input()
	SearchBooks(session,q)

def GetAcessToken ():
	global CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET

	print 'Authenticating............'
	goodreads = OAuth1Service(
	    consumer_key=CONSUMER_KEY,
	    consumer_secret=CONSUMER_SECRET,
	    name='goodreads',
	    request_token_url='http://www.goodreads.com/oauth/request_token',
	    authorize_url='http://www.goodreads.com/oauth/authorize',
	    access_token_url='http://www.goodreads.com/oauth/access_token',
	    base_url='http://www.goodreads.com/'
	    )

	# head_auth=True is important here; this doesn't work with oauth2 for some reason
	request_token, request_token_secret = goodreads.get_request_token(header_auth=True)

	authorize_url = goodreads.get_authorize_url(request_token)
	print 'Visit this URL in your browser: ' + authorize_url
	accepted = 'n'
	while accepted.lower() == 'n':
	    # you need to access the authorize_link via a browser,
	    # and proceed to manually authorize the consumer
	    accepted = raw_input('Have you authorized me? (y/n) ')

	print 'Fetching access tokens.............'
	session = goodreads.get_auth_session(request_token, request_token_secret)

	# these values are what you need to save for subsequent access.
	ACCESS_TOKEN = session.access_token
	ACCESS_TOKEN_SECRET = session.access_token_secret


def GetKeys():
	global  CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET

	with open('keys.json') as data_file:
		data = json.load(data_file)

	data_file.close()
	# pprint (data)

	if data['ACCESS_TOKEN'].strip()  and data['ACCESS_TOKEN_SECRET'].strip() :
		print 'Found access tokens'
		ACCESS_TOKEN = data['ACCESS_TOKEN'].strip()
		ACCESS_TOKEN_SECRET = data['ACCESS_TOKEN_SECRET'].strip()

	else:
		print "Couldn't find any access tokens."
		CONSUMER_KEY =  data['CONSUMER_KEY'].strip() 
		CONSUMER_SECRET =  data['CONSUMER_SECRET'].strip()
		GetAcessToken()
		#save access tokens back to file
		data['ACCESS_TOKEN'] = ACCESS_TOKEN
		data['ACCESS_TOKEN_SECRET'] = ACCESS_TOKEN_SECRET

		#pprint(data)

		with open('keys.json','w') as data_file:
			json.dump(data,data_file)
		data_file.close()


def GetSession():
	if ACCESS_TOKEN and ACCESS_TOKEN_SECRET:
		return GetNewSession()
	else:
		GetKeys()
		return GetNewSession()	

def GetNewSession():
	new_session  = OAuth1Session(
		consumer_key = CONSUMER_KEY,
		consumer_secret = CONSUMER_SECRET,
		access_token = ACCESS_TOKEN,
		access_token_secret = ACCESS_TOKEN_SECRET
	)
	return new_session

def SearchBooks(session,searchKey):
	URL =  'https://www.goodreads.com/search/index.xml'
	data = {q : searchKey}
	response = session.get(URL,data)

	# if(response.status_code!=200):
	# 	print response
	# else:
	# 	print response
	print response

if __name__ == '__main__':
	main()