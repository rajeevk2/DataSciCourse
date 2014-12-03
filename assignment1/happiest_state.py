import sys
import codecs
import json

states = {'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

sent_file = open(sys.argv[1])
tweet_file = open(sys.argv[2])

# compile scores directory
s = open(sent_file.name)
scores ={}
for line in s:
    term, score = line.split("\t")
    scores[term] = int(score)

# open file with tweets
f = codecs.open(tweet_file.name,'rU','utf-8')

h={} # happiness directory
for line in f:
    tweet=json.loads(line)
    sentiment = 0
    try:
        if tweet['lang']=='en':
            newline = tweet['text']
            for w in  newline.split():
                for word in scores:
                    if w == word:
                        sentiment += scores[w]
                        print "\tsentiment for {term} is {score}".format(term=word,score=scores[word])
            place = tweet['place']
            print 'sentiment for {area} is {num}'.format(area=place,num=sentiment)
            print 'Coordinates are ',tweet['coordinates']
            if place in states.keys() or place in states.values():
                h[place] = h.get(place,0) + sentiment
    except:
        pass

p =[] # happiest place list
for key, value in h.items():
    p.append((value,key)) # list consists of place, happiness index
p.sort(reverse=True) # sort list as happiest to saddest

for index,place in p[0:10]:
    print place,'\t',index
                
