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

def countMoodScore(scores,fp):
    data_f = codecs.open(fp.name,'rU','utf-8') 
    lineNum = 0
    for line in data_f:
        tweet = json.loads(line)
        sentiment = 0
        lineNum +=1
        try:
            if tweet["lang"] == "en":
                print json.dumps(tweet,indent=4)
                try:
                    newline = tweet["text"]
                    for word in newline.split():
                        for scored_word in scores:
                            try:
                                if word==scored_word:
                                    sentiment += scores[word]
                                    print "\tsentiment for {term} is {score}".format(term=word,score=scores[word])
                            except:
                                pass
                except:
                    pass
        except:
            pass
        print "sentiment of tweet # {LineN} is {value}".format(LineN=lineNum,value=sentiment)
    return [data_f]


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()

    scores = scoreDirectory()
    
    [data_f] = countMoodScore(scores,sent_file)
    
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
