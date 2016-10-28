from flask import Flask, request
from app import app
import tweepy
import json
import urllib2



data = {}
# static url
@app.route('/')
def index():
    return "Hello, World!"

# url parameters
@app.route('/endpoint/<input>')
def endpoint(input):
    return input

# api with endpoint
@app.route('/nameEndpoint', methods=['GET'])
def nameEndpoint():
    if 'name' in request.args:
    	return 'My name is ' + request.args['name']


@app.route("/twitter")
def twitter():
    API_KEY = "dRQ3KrShiWp3Ev2RO7tmRuCWl"
    API_SECRET = "PmSBTqS3JfP2IV6NquNvAsTuTiZ8i5wexv3TXlfRcT5vB0DzQ5"
    ACCESS_TOKEN = "2931812683-lsfCYCiz783yi59KQBVwVwEg0vPoXMKIkCrGRyT"
    ACCESS_TOKEN_SECRET = "U9Tlbf6SnnuCX0CiD9Qx5Fb7rSdgBF5WcDysvbb5nKND6"

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    query = 'Donald Trump'
    max_tweets = 2
    searched_tweets = api.search(q=query, count=max_tweets)

    data['twitter']=json.dumps(searched_tweets)
    return json.dumps(searched_tweets)



@app.route("/spotify")
def spotify():
    artistResponse = urllib2.urlopen("https://api.spotify.com/v1/search?q=tania%20bowra&type=artist").read()


    artistJson = json.loads(artistResponse)
    print artistResponse['artists']['items'][0]


    uid = artistJson['artists']['items'][0]['id']
    topTracks = urllib2.urlopen("https://api.spotify.com/v1/artists/" + uid + "/top-tracks?country=SE").read()

    topTracksJson = json.loads(topTracks)

    data["spotify"] = topTracksJson['tracks']                                #dummy code not really, needs to be fixed
    return topTracksJson['tracks']


@app.route("/wikipedia")             #https://en.wikipedia.org/w/api.php ENDPOINT
def wikipedia():                     #api.php?action=query&titles=Main%20Page&prop=revisions&rvprop=content&format=json
    query = 'thing that austin gives me'

    wikiQuery = ''
    for i in xrange(len(query)):
        if query[i]!=" " or query[i]!="_":
            wikiQuery+=query[i]
        else:
            wikiQuery+="%20"

    wikiResponse = urllib2.urlopen(wikiQuery).read()

    wikiJson = json.loads(wikiResponse)

    wikiText = wikiJson["batchcomplete"]["query"]["pages"]["the text I think?"]
    data["wikipedia"] = wikiText
    
