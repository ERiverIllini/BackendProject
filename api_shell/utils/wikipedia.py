import urllib2
import json




# def wikipedia():  # api.php?action=query&titles=Main%20Page&prop=revisions&rvprop=content&format=json
data = {}
query = 'LeBron James'
# print query
wikiQuery = ''
for i in xrange(len(query)):
    if query[i] == " " or query[i] == "_":
        wikiQuery += "%20"
    else:
        wikiQuery += query[i]

print wikiQuery
print "https://en.wikipedia.org/w/api.php?query&titles="+wikiQuery+"&prop=revisions&rvprop=content&format=json"
wikiResponse = urllib2.urlopen("https://en.wikipedia.org/w/api.php?action=query&titles="+wikiQuery+"&prop=revisions&rvprop=content&format=json").read()

wikiJson = json.loads(wikiResponse)
wikiText = wikiJson["query"]["pages"]["240940"]["revisions"][0]
print wikiText
#
# wikiText = wikiJson["batchcomplete"]["query"]["pages"]["the text I think?"]
# data["wikipedia"] = wikiText
