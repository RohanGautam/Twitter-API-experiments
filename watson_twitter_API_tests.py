import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights
#enter your twitter api info below:
con_secret = ''
con_secret_key = ''
token = ''
token_key = ''
t=twitter.Twitter(auth=twitter.OAuth(token, token_key, con_secret, con_secret_key))
x=t.statuses.user_timeline(screen_name="@TheRealRyanHiga",count=20, include_rts=False)

import pprint
pprint.pprint(x[0])

#we need tweets that are: 1)in english and 2) together in one gigantic line


for i in x:
    if i['lang']=='en':
        text+=i['text'].encode('utf-8')
print text

#to be continued....
