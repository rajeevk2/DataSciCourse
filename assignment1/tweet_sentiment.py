import sys
import json
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

def countMoodScore(scores):
    data_f = codecs.open('output.txt','rU','utf-8') 
	lineNum = 0
    for line in data_f:
        tweet = json.loads(line)
        sentiment = 0
        try:
            if tweet["lang"] == "en":
                try:
                    newline = tweet["text"]
                    words = [w for w in newline.split()]
					lineNum +=1
                    for word in words:
                        for scored_word in scores:
                            if word==scored_word:
                                sentiment += scores[word]
                                print "\t{lineN}sentiment for {term} is {score}".format(lineN=lineNum,term=word,score=scores[word])
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
    
    [data_f] = countMoodScore(scores)
    
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
