import sys
import json
import re
from pprint import pprint
import codecs
from collections import Counter

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def scoreDirectory():
    afinnfile = open("AFINN-111.txt")
    scores ={}
    for line in afinnfile:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores

def countMoodScore(scores):
    data_f = codecs.open('output.txt','rU','utf-8') 
    for line in data_f:
        tweet = json.loads(line)
        sentiment = 0
        try:
            if tweet["lang"] == "en":
                try:
                    newline = tweet["text"]
                    words = [w for w in newline.split()]
                    for word in words:
                        for scored_word in scores:
                            if word==scored_word:
                                sentiment += scores[word]
                                print "\tsentiment for {term} is {score}".format(term=word,score=scores[word])
                except:
                    pass
        except:
            pass
        print "sentiment is %d" %sentiment
    return [data_f]


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()

    scores = scoreDirectory()
    #print scores.items()
    
    [data_f] = countMoodScore(scores)
    
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
