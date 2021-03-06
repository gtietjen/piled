import time
import atexit
from datetime import datetime, timedelta
from neopixel import Adafruit_NeoPixel, Color

#edit




# LED strip configuration:
LED_COUNT = 20      # Number of LED pixels.
LED_PIN = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT = False   # True to invert the signal (when using NPN transistor level shift)
INTERVAL = 0.15
# INTERVAL2 = 0.1


def lightsOn(strip, four_on=False, wait_ms=50):
    
    if four_on:
        for i, four in zip(range(strip.numPixels()), four_on):
            print(i, four, 'on')
            strip.setPixelColor(four, Color(200, 255, 255))
            strip.setPixelColor(four, Color(200, 255, 255))
            strip.setPixelColor(four, Color(200, 255, 255))
            strip.setPixelColor(four, Color(200, 255, 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def lightsOff(strip, four_off=False, all_off=False, wait_ms=50):

    if four_off:
        for i, off in zip(range(strip.numPixels()), four_off):
            print(i, off, 'off')
            strip.setPixelColor(off, Color(0, 0, 0))
            strip.setPixelColor(off, Color(0, 0, 0))
            strip.setPixelColor(off, Color(0, 0, 0))
            strip.setPixelColor(off, Color(0, 0, 0))
        strip.show()
        time.sleep(wait_ms/1000.0)

    if all_off:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()


def turnOffAll(strip, wait_ms=50):
    """Turn off all LEDs."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()

# Main program logic follows:
if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    atexit.register(turnOffAll, strip)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    start_time = datetime.now()
    light2 = datetime.now() + timedelta(seconds=0.1)
    light3 = datetime.now() + timedelta(seconds=0.2)
    light4 = datetime.now() + timedelta(seconds=0.3)
    light5 = datetime.now() + timedelta(seconds=0.4)
    light6 = datetime.now() + timedelta(seconds=0.5)
    light7 = datetime.now() + timedelta(seconds=0.6)
    light8 = datetime.now() + timedelta(seconds=0.7)
    light9 = datetime.now() + timedelta(seconds=0.8)
    light10 = datetime.now() + timedelta(seconds=0.9)
    light11 = datetime.now() + timedelta(seconds=1.0)
    light12 = datetime.now() + timedelta(seconds=1.1)
    light13 = datetime.now() + timedelta(seconds=1.2)
    light14 = datetime.now() + timedelta(seconds=1.3)
    light15 = datetime.now() + timedelta(seconds=1.4)
    light16 = datetime.now() + timedelta(seconds=1.5)
    light17 = datetime.now() + timedelta(seconds=1.6)
    light18 = datetime.now() + timedelta(seconds=1.7)
    light19 = datetime.now() + timedelta(seconds=1.8)
    light20 = datetime.now() + timedelta(seconds=1.9)
    light21 = datetime.now() + timedelta(seconds=2.0)
    light22 = datetime.now() + timedelta(seconds=2.1)
    light23 = datetime.now() + timedelta(seconds=2.2)
    light24 = datetime.now() + timedelta(seconds=2.3)
    light25 = datetime.now() + timedelta(seconds=2.4)
    light26 = datetime.now() + timedelta(seconds=2.5)
    light27 = datetime.now() + timedelta(seconds=2.6)
    light28 = datetime.now() + timedelta(seconds=2.7)
    light29 = datetime.now() + timedelta(seconds=2.8)
    light30 = datetime.now() + timedelta(seconds=2.9)
    light31 = datetime.now() + timedelta(seconds=3.0)
    light32 = datetime.now() + timedelta(seconds=3.1)
    light33 = datetime.now() + timedelta(seconds=3.2)
    light34 = datetime.now() + timedelta(seconds=3.3)
    light35 = datetime.now() + timedelta(seconds=3.4)
    light36 = datetime.now() + timedelta(seconds=3.5)
    light37 = datetime.now() + timedelta(seconds=3.6)
    light38 = datetime.now() + timedelta(seconds=3.7)
    light39 = datetime.now() + timedelta(seconds=3.8)
    light40 = datetime.now() + timedelta(seconds=3.9)
    light41 = datetime.now() + timedelta(seconds=4.0)
    light42 = datetime.now() + timedelta(seconds=4.1)
    light43 = datetime.now() + timedelta(seconds=4.2)
    light44 = datetime.now() + timedelta(seconds=4.3)
    light45 = datetime.now() + timedelta(seconds=4.4)
    light46 = datetime.now() + timedelta(seconds=4.5)
    # light11 = datetime.now() + timedelta(seconds=1.50)
    end = start_time + timedelta(seconds=5)


    onWhiteLightsOneThree = lightsOn(strip, four_on=[0,1,2,3], wait_ms=50)
    onWhiteLightsFourSeven = lightsOn(strip, four_on=[4,5,6,7], wait_ms=50)
    onWhiteLightsEightEleven = lightsOn(strip, four_on=[8,9,10,11], wait_ms=50)
    onWhiteLightsTwelveFifteen = lightsOn(strip, four_on=[12,13,14,15], wait_ms=50)
    onWhtieLightsSixteenNineteen = lightsOn(strip, four_on=[16,17,18,19], wait_ms=50)

    onList = [onWhiteLightsOneThree, onWhiteLightsFourSeven, onWhiteLightsEightEleven,onWhiteLightsTwelveFifteen, onWhtieLightsSixteenNineteen]
    

    offWhiteLightsOneThree = lightsOff(strip, four_off=[0,1,2,3], wait_ms=50)
    offWhiteLightsFourSeven = lightsOff(strip, four_off=[4,5,6,7], wait_ms=50)
    offWhiteLightsEightEleven = lightsOff(strip, four_off=[8,9,10,11], wait_ms=50)
    offWhiteLightsTwelveFifteen = lightsOff(strip, four_off=[12,13,14,15], wait_ms=50)
    offWhiteLightsSixteenNineteen = lightsOff(strip, four_off=[16,17,18,19], wait_ms=50)

    offList = [offWhiteLightsOneThree, offWhiteLightsFourSeven, offWhiteLightsEightEleven, offWhiteLightsTwelveFifteen, offWhiteLightsSixteenNineteen]
    # onList is 'odd' offlist is 'even'
    result = [None]*(len(onList)+len(offList))
    result[::2] = onList
    result[1::2] = offList

# count = 0

# while (count< 10):
#     for i, on in zip(range(len(result)), result):
#         count+=1
#         if (i % 2 != 0):
#             on
#         else:
#             on
#     break

arg1 = [i for i in range(0, 255, 4)]
arg2 = [i for i in range(0, 255, 4)]
arg3 = [i for i in range(0, 255, 4)]

lst = [1,2,3,4,5]

lights = [l for i in range( int(round(len(arg1) / len(lst))) ) for l in lst]
del lights[-1]

count = 0
while (count < 60):
    for i, li, ar1, ar2,ar3, in zip(range(strip.numPixels()), lights, arg1, arg2, arg3):
        print(i, li, 'on')
        strip.setPixelColor(li, Color(ar1, ar2, ar3))
        strip.show()
        time.sleep(1)
        strip.setPixelColor(li, Color(ar1, ar2, ar3))
        strip.show()
        time.sleep(1)
        strip.setPixelColor(li, Color(ar1, ar2, ar3))
        strip.show()
        time.sleep(1)
        strip.setPixelColor(li, Color(ar1, ar2, ar3))
        strip.show()
        time.sleep(1)
        strip.setPixelColor(li, Color(ar1, ar2, ar3))
        strip.show()
        time.sleep(1)
        count+=1
    break
