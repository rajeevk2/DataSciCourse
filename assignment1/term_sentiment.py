import sys
import codecs
import json
        
def hw():
    print '======================\nHello, world!\n======================\n'

def lines(fp):
    print "Number of lines in {file} are {lins}".format(file=fp.name,lins=str(len(fp.readlines())))

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
    sentiments={}
    for line in data_f:
        tweet = json.loads(line)
        sentiment = 0
        lineNum +=1
        try:
            if tweet["lang"] == "en":
                #print json.dumps(tweet,indent=4)
                try:
                    newline = tweet["text"]
                    words = [w for w in newline.split()]
                    for word in words:
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
##        print "sentiment of tweet # {LineN} is {value}".format(LineN=lineNum,value=sentiment)
        sentiments[lineNum]=sentiment
        print "sentiment of tweet = {value}".format(value=sentiments[lineNum])
    return sentiments

        
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()

    # creating AFINN-111 dictionary
    scores = scoreDirectory()

    # extracting sentiments from tweets
    sentiments = countMoodScore(scores)
    numTweets = 0
    for sentiment in sentiments:
##        if sentiment!=0:
##            numTweets += 1
##        else:
##            numTweet += 0
        print sentiment
    print '\n Number of tweets extracted: {num}'.format(num=numTweets)
    
    
    print '\n======================'
    lines(sent_file)
    lines(tweet_file)
    print '======================\n'

if __name__ == '__main__':
    main()
