# -*- coding: utf-8 -*-
import json
import urllib2
import tweepy
# urllib2
"""
The urllib2 module defines functions and classes which help in opening URLs (mostly HTTP) 
in a complex world — basic and digest authentication, redirections, cookies and more.
"""


artistResponse = urllib2.urlopen("https://api.spotify.com/v1/search?q=justin%20bieber&type=artist").read()


artistJson = json.loads(artistResponse)
print artistJson
uid = artistJson['artists']['items'][0]['id']
print uid
print artistJson['artists']['items'][0]['name']
topTracks = urllib2.urlopen("https://api.spotify.com/v1/artists/" + uid + "/top-tracks?country=US").read()

topTracksJson = json.loads(topTracks)
print topTracksJson['tracks'][0]['album']['name']
