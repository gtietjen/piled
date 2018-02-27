import time
import white
import RPi.GPIO as GPIO
from twython import TwythonStreamer

from neopixel import *

# Search terms
TERMS = '#guncontrol'

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
#			white.colorWipe()
			execfile("bestled.py")
#			time.sleep(0.5)

# Create streamer
try:
        stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
       GPIO.cleanup()
