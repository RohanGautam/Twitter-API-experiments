import twitter
try:
    con_secret = 'VKwjWAXnuX2wywUZYVsknC0oY'
    con_secret_key = 'UAeNa2QE4Nk8yuDdtvv2ykH6aLF1lat9yx1r824XUgrlx6nPwp'
    token = '2428617499-muXCuNlhiquXythOH9s8mXo4PBp8ZjiZCyX3Ly8'
    token_key = '78YMqJiibi8ooNTmDfyDDwZ7hjfT05EqSV07QgxLzVD4f'
    
    t=twitter.Twitter(auth=twitter.OAuth(token, token_key, con_secret, con_secret_key))
    statupdate=raw_input('Enter text that you want to tweet: ')
    x=t.statuses.update(status=statupdate)
    
    x2=t.statuses.user_timeline(screen_name="@RohanGautam13",count=1, include_rts=False)
    
    if x2[0]['text']==statupdate:print 'Tweeted successfully!🎉'
    else : print 'Status updation failed'
except twitter.api.TwitterHTTPError:
    print 'Status updation failed: Duplicate status entered'