import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights

con_secret = 'VKwjWAXnuX2wywUZYVsknC0oY'
con_secret_key = 'UAeNa2QE4Nk8yuDdtvv2ykH6aLF1lat9yx1r824XUgrlx6nPwp'
token = '2428617499-muXCuNlhiquXythOH9s8mXo4PBp8ZjiZCyX3Ly8'
token_key = '78YMqJiibi8ooNTmDfyDDwZ7hjfT05EqSV07QgxLzVD4f'
t=twitter.Twitter(auth=twitter.OAuth(token, token_key, con_secret, con_secret_key))
x=t.statuses.user_timeline(screen_name="@TheRealRyanHiga",count=20, include_rts=False)

import pprint
pprint.pprint(x[0])

#we need tweets that are: 1)in english and 2) together in one gigantic line
text=''

#for i in x:
#    if i['lang']=='en':
#        text+=i['text'].encode('utf-8')
#print text

#for i in x:
#    print i['text']
