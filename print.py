import urllib
import json

response = urllib.urlopen("https://stream.twitter.com/1.1/statuses/sample.json")
pyresponse = json.load(response)

print pyresponse.keys()
