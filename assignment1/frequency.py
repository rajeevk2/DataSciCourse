import sys
import codecs
import json
##from collections import Counter

sent_file = open(sys.argv[1])

f = codecs.open(sent_file.name,'rU','utf-8')

h = {} # histogram dictonary
for line in f:
    tweet=json.loads(line) # parse a JSON object(?)
    try:
        if tweet['lang']=='en':     # go further iff tweet is in English
            newline = tweet['text'] # extract tweet text
            for w in newline.split():   # extract words in the tweet text
                w = w.lower()           # convert every word to lower caps
                h[w] = h.get(w,0)+1     # compute frequency of occurence
    except:
        pass
    
total_ = sum(h.values())
unique_= len(h)
print "total number of words: ", total_
print "number of unique words: ", unique_

t=[] # frequency list
for key,value in h.items():
    t.append((value,key))# create list of pair={word, frequency} for each word
t.sort(reverse=True) # sort list in descending order of frequency

for freq,word in t[0:10]:
    print word,'\t',freq
