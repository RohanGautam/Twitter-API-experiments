import twitter
try:
    #enter your twitter api info below:
    con_secret = ''
    con_secret_key = ''
    token = ''
    token_key = ''
    
    t=twitter.Twitter(auth=twitter.OAuth(token, token_key, con_secret, con_secret_key))
    statupdate=raw_input('Enter text that you want to tweet: ')
    x=t.statuses.update(status=statupdate)
    
    x2=t.statuses.user_timeline(screen_name="@RohanGautam13",count=1, include_rts=False)
    
    if x2[0]['text']==statupdate:print 'Tweeted successfully!🎉'
    else : print 'Status updation failed'
except twitter.api.TwitterHTTPError:
    print 'Status updation failed: Duplicate status entered'
