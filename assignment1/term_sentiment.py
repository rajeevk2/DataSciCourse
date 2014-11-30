import sys
        
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

def exploreNLTK():
    from nltk import wordnet as wn
##    for synset in list(wn.all_synsets('n'))
##        print synset
        
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()

    # creating AFINN-111 dictionary
    scores = scoreDirectory()

    # explore NLTK
    exploreNLTK()
    
    print '\n======================'
    lines(sent_file)
    lines(tweet_file)
    print '======================\n'

if __name__ == '__main__':
    main()
