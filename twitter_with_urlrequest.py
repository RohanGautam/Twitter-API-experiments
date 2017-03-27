#from kivy.network.urlrequest import UrlRequest
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import twitter
#import json



con_secret = 'VKwjWAXnuX2wywUZYVsknC0oY'
con_secret_key = 'UAeNa2QE4Nk8yuDdtvv2ykH6aLF1lat9yx1r824XUgrlx6nPwp'
token = '2428617499-muXCuNlhiquXythOH9s8mXo4PBp8ZjiZCyX3Ly8'
token_key = '78YMqJiibi8ooNTmDfyDDwZ7hjfT05EqSV07QgxLzVD4f'
#search_url='https://api.twitter.com/1.1/statuses/mentions_timeline.json'
t=twitter.Twitter(auth=twitter.OAuth(token, token_key, con_secret, con_secret_key))


class AddLocationForm(BoxLayout):
    search_results=ObjectProperty()
    search_input=ObjectProperty()
    def status_update(self):
        print self.search_input.text
        t.statuses.update(status=self.search_input.text)
        self.search_results.item_strings.append('Tweeted successfully!!')
    def twet(self):
        #from multiprocessing import Process
        from threading import Thread
        thread = Thread(target=self.status_update)
        thread.start()
        self.search_results.item_strings.append('.........')
        
    
    
    
class UrltryApp(App):
    pass
if __name__=='__main__':
    UrltryApp().run()
