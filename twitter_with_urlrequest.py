#from kivy.network.urlrequest import UrlRequest
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import twitter
#import json


#enter your twitter api info below:
con_secret = ''
con_secret_key = ''
token = ''
token_key = ''

t=twitter.Twitter(auth=twitter.OAuth(token, token_key, con_secret, con_secret_key))


class AddLocationForm(BoxLayout):
    search_results=ObjectProperty()
    search_input=ObjectProperty()
    def status_update(self):
        print self.search_input.text
        t.statuses.update(status=self.search_input.text)
        self.search_results.item_strings.append('Tweeted successfully!!')
    def twet(self):
        #using multithreading to prevent lag in the app
        from threading import Thread
        thread = Thread(target=self.status_update)
        thread.start()
        self.search_results.item_strings.append('.........')
        
    
    
    
class UrltryApp(App):
    pass
if __name__=='__main__':
    UrltryApp().run()
