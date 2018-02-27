import time
import white
import RPi.GPIO as GPIO
from twython import TwythonStreamer

from neopixel import *

# Search terms
# TERMS = '#yes'

# TERMS = twitter.showStatus(id="866007536595546112")
#TERMS = twitter.statuses.show(id="866007536595546112")

#SearchTerm = 'abracadabra' # If spaces are included, they are 'OR', ie finds tweets with any one of the words, not the whole string.
Tweeter = '866007536595546112' # This is Donald Trump, finds tweets from him or mentioning him
#Place = '"47.405,-177.296,1mi"' # Sent from within 1 mile of Lat, Long

# print status['text']

# GPIO pin number of LED
#LED = 22

# Twitter application authentication
APP_KEY = 'n84wARYnIoYQaUH0Rql1P2XIu'
APP_SECRET = 'KLOeFtnT7DA5RCtHJx9OZLvDgFoRNZW3rNTjFGMWxiwmdqe8YM'
OAUTH_TOKEN = '866007536595546112-1tp9i7lt97uVdHX2PHi0P2jqMI0anPb'
OAUTH_TOKEN_SECRET = 'Lqh88jwGMoe5JIWgKtE5HAFIJC30X91URoRCIdouoFZCQ'

# Setup callbacks from Twython Streamer
class BlinkyStreamer(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:
                        print data['text'].encode('utf-8')
#                       white.colorWipe()
                        execfile("bestled.py")
#                       time.sleep(0.5)

# Create streamer
try:
        stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        # stream.statuses.filter(track=TERMS)
        stream.statuses.filter(follow=Tweeter)
except KeyboardInterrupt:
       GPIO.cleanup()
