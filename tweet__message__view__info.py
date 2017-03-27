import twitter
#enter your twitter api information below
con_secret = ''
con_secret_key = ''
token = ''
token_key = ''
t=twitter.Twitter(auth=twitter.OAuth(token, token_key, con_secret, con_secret_key))
print 'choose:\n\t1) Messaging a user, or\n\t2) Getting information about a user,or\n\t3) Viewing the "n" most recent tweets of a user,or\n\t4)Tweet something!'
choice=raw_input()

if choice=='1': #messaging a user
    try:
        sn=raw_input('Enter the twitter handle of person you want to message: ')
        mes=raw_input('Enter the message you want to send: ')
        t.direct_messages.new(user=sn,text=mes)
        print 'Message sent!'
    except:
        print 'ERROR: you cannot sent messages to users who are not following you'        
        print 'OR=>invalid input'
        
        
elif choice=='2':#Getting info on a particular user
    sn=raw_input('Enter the twitter handle of the person you want information about:')
    x2=t.statuses.user_timeline(screen_name=sn,count=1, include_rts=False)
    print '\t\tINFORMATION ABOUT USER',sn
    print 'Name:\n\t',x2[0]['user']['name']
    print 'Bio:\n\t',x2[0]['user']['description']
    print 'No: of followers\n\t',x2[0]['user']['followers_count']
    print 'url:\n\t',x2[0]['user']['url']
    print 'Verified:\n\t',x2[0]['user']['verified']
    print 'Location:\n\t',x2[0]['user']['location']
    
    
elif choice=='3':#to view the 'n' most recent tweets of a person
    sn=raw_input('Enter the twitter handle of the person you want information about:')
    n=input('Enter Value of n: ')
    x=t.statuses.user_timeline(screen_name=sn,count=n, include_rts=False)
    print '\t\tFirst',n,'tweets of user',sn,':'
    for i in x:
        print '\t'+i['text'],'\n'
        
        
elif choice=='4':#to tweet stuff!
    try:
        statupdate=raw_input('Enter text that you want to tweet: ')
        x=t.statuses.update(status=statupdate)
        
        x2=t.statuses.user_timeline(screen_name="@RohanGautam13",count=1, include_rts=False)
        
        if x2[0]['text']==statupdate:print 'Tweeted successfully!🎉'
        else : print 'Status updation failed'
    except twitter.api.TwitterHTTPError:
        print 'Status updation failed: Duplicate status entered'
    
else:
    print 'Invalid choice!:('
