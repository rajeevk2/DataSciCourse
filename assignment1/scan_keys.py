import sys
import json
import urllib

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

def get_state(tweet):
    # extract place information, coordinates, etc.
    place = tweet['place']
    coordinates = tweet['coordinates']
    if place['country_code']=='US':
        #print json.dumps(place,indent=4)
##        if place['full_name']!=[]:
##            fullName = place['full_name'].split(',')
##            state_ac = fullName[1]
##            key,value = states.items()
##            print 'key:     ', key
##            print 'value:   ', value
##            if state_ac in unicode(states.keys(),'utf-8'):
##                print '===>'
        if coordinates.keys()!=[]:
            latlon = coordinates['coordinates']         
            url = 'http://maps.googleapis.com/maps/api/geocode/json?latlng={0},{1}'
            request = url.format(latlon[1],latlon[0])
            response = urllib.urlopen(request)
            gapi_loc = json.load(response)
            addresses = []
            for lines in gapi_loc['results']:
                addresses.append(lines['formatted_address'])
            state_here = addresses[len(addresses)-3].split(',')
            state_ac = state_here[1]
            state_here = addresses[len(addresses)-2].split(',')
            state = state_here[0]
            if state in states.values():
                print '--->\t'
        else:
            return []
    else:
        pass
    return [state,state_ac]


tweet_file = open(sys.argv[1])

f = open(tweet_file.name)
for line in f:
    tweet=json.loads(line)
    try:
        if tweet['lang']=='en':
            [state,state_ac] = get_state(tweet)
            print '\t\t{ssa}\t{ss}'.format(ssa=state_ac,ss=state)
    except:
        pass
