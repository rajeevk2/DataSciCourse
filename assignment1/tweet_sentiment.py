import sys
import json
import codecs

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

# compile score dictonary
def scoreDirectory():
    afinnfile = open("AFINN-111.txt")
    scores ={}
    for line in afinnfile:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores
scoreN = {'abandon':	-2,
          'abandoned':  -2}

def countMoodScore(scores,fp):
    data_f = codecs.open(fp.name,'rU','utf-8') 
    lineNum = 0
    for line in data_f:
        tweet = json.loads(line)
        sentiment = 0 # reset sentiment for each line
        lineNum +=1
        try:
            if tweet["lang"] == "en": # English language only
                newline = tweet["text"]
                if newline != []: # perform for populated text fields
                    for word in newline.split():
                        sentiment += scores.get(word.encode('utf8'),0)
                        print "\tsentiment for {term} is\t{score}".format(term=word.encode('utf8'),score=scores.get(word.encode('utf8'),0))
        except:
            pass
        print "sentiment of tweet # {LineN} is {value}".format(LineN=lineNum,value=sentiment)


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()

    scores = scoreDirectory()

    print scoreN.items()
    
    countMoodScore(scores,tweet_file)
    
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
