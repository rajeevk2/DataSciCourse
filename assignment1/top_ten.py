import sys
import codecs
import json
from collections import Counter 

# file name
tweet_file = open(sys.argv[1])

# open file with tweets
f = codecs.open(tweet_file.name,'rU','utf-8')
h = []

for line in f:
    tweet = json.loads(line)
    try:        
        if tweet['lang']=='en':
            if 'entities' in tweet.keys() and 'hashtags'in tweet['entities']:
                if tweet['entities']['hashtags'] != []:
                    for hashtags in tweet['entities']['hashtags']:
                        h.append(hashtags['text'].encode('utf-8'))
    except:
        pass

top_ten = Counter(h).most_common(10)
for key,value in top_ten:
    print key,'\t\t\t',float(value)
