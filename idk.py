from sys import argv
import os
import signal
import subprocess
import time
import neopixel
 
#Basic configurations
SLEEP_TIME = 1 #Time to sleep between server pings in seconds
 
#LED strip configuration
LED_COUNT = 12
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 5
LED_BRIGHTNESS = 255
LED_INVERT = False
 
#Primary functions
def getPing(hostname):
    '''
    Input: Takes in a hostname to ping
    Output: Returns the response time of the server
    '''
    ping = subprocess.Popen(
        ["/bin/ping", "-c", "1", hostname],
        stdout=subprocess.PIPE
        )
 
    response = ping.communicate()
    try:
        #get the response time from the ping output
        responseTime = int(float(str(response).split('time=')[1].split(' ms')[0]))
    except:
        #server time out
        print("Server time out")
        responseTime = 1000
 
    #return the response time of the server
    return responseTime
 
def getColor(responseTime):
    '''
    Input: Takes in an integer responseTime
    Output: Returns an RGB tuple for the corresponding color to ping rate
    '''
 
    if responseTime <= 50:
        return neopixel.Color(0,255,0) #GREEN
    elif responseTime > 50 and responseTime <= 100:
        return neopixel.Color(125,255,0) #LIGHT GREEN
    elif responseTime > 100 and responseTime <= 150:
        return neopixel.Color(255,255,0) #YELLOW
    else:
        return neopixel.Color(255,0,0) #RED
 
def colorChange(strip, color, wait_ms=50):
    '''Wipe color in a pixel at a time'''
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)
 
#MAIN
 
hostname = 'http://iad.valve.net/'
 
#check for valid usage
if(len(argv) == 2):
    #set our hostname
    hostname = argv[1]
else:
    print('Usage: neoPing {hostname}')
    exit()
 
strip = neopixel.Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
 
strip.begin()
 
while True:
    ping = getPing(hostname)
    color = getColor(ping)
 
    #print our final color and ping
    print("Ping to " + hostname + ": " + str(ping))
    colorChange(strip, color)
    time.sleep(SLEEP_TIME)
