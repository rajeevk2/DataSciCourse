import sys
import json
import re
from pprint import pprint
import codecs

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

def countMoodScore():
    data_f = codecs.open('output.txt','rU','utf-8') 
    for line in data_f:
        tweet = json.loads(line)
        if tweet["lang"] == "en":
            print tweet["source"]
    return data_f


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()

    scores = scoreDirectory()
    #print scores.items()
    
    data_f = countMoodScore()
    
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
