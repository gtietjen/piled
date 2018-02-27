import time
import atexit
from datetime import datetime, timedelta
from neopixel import Adafruit_NeoPixel, Color


# LED strip configuration:
LED_COUNT = 20      # Number of LED pixels.
LED_PIN = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT = False   # True to invert the signal (when using NPN transistor level shift)
INTERVAL = 0.15
# INTERVAL2 = 0.1

def whiteLight(strip, wait_ms=50):
    """Turn off all LEDs."""
    for i in range(strip.numPixels()):
        # strip.setPixelColor(0, Color(200, 255, 255))
        # strip.setPixelColor(1, Color(200, 255, 255))
        # strip.setPixelColor(2, Color(200, 255, 255))
        # strip.setPixelColor(3, Color(200, 255, 255))
        strip.setPixelColor(0, Color(0, 255, 0))
        strip.setPixelColor(1, Color(0, 255, 0))
        strip.setPixelColor(2, Color(0, 255, 0))
        strip.setPixelColor(3, Color(0, 255, 0))
    strip.show()
    time.sleep(wait_ms/1000.0)

def whiteLight2(strip, wait_ms=50):
    """Turn off all LEDs."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(4, Color(200, 255, 255))
        strip.setPixelColor(5, Color(200, 255, 255))
        strip.setPixelColor(6, Color(200, 255, 255))
        strip.setPixelColor(7, Color(200, 255, 255))
    strip.show()
    time.sleep(wait_ms/1000.0)

def whiteLight3(strip, wait_ms=50):
    """Turn off all LEDs."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(8, Color(200, 255, 255))
        strip.setPixelColor(9, Color(200, 255, 255))
        strip.setPixelColor(10, Color(200, 255, 255))
        strip.setPixelColor(11, Color(200, 255, 255))
    strip.show()
    time.sleep(wait_ms/1000.0)

def whiteLight4(strip, wait_ms=50):
    """Turn off all LEDs."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(12, Color(200, 255, 255))
        strip.setPixelColor(13, Color(200, 255, 255))
        strip.setPixelColor(14, Color(200, 255, 255))
        strip.setPixelColor(15, Color(200, 255, 255))
    strip.show()
    time.sleep(wait_ms/1000.0)

def whiteLight5(strip, wait_ms=50):
    """Turn off all LEDs."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(16, Color(200, 255, 255))
        strip.setPixelColor(17, Color(200, 255, 255))
        strip.setPixelColor(18, Color(200, 255, 255))
        strip.setPixelColor(19, Color(200, 255, 255))
    strip.show()
    time.sleep(wait_ms/1000.0)

def turnOff1(strip, wait_ms=50):
    """Turn off all LEDs."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(0, Color(0, 0, 0))
        strip.setPixelColor(1, Color(0, 0, 0))
        strip.setPixelColor(2, Color(0, 0, 0))
        strip.setPixelColor(3, Color(0, 0, 0))
    strip.show()

def turnOff2(strip, wait_ms=50):
    """Turn off all LEDs."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(4, Color(0, 0, 0))
        strip.setPixelColor(5, Color(0, 0, 0))
        strip.setPixelColor(6, Color(0, 0, 0))
        strip.setPixelColor(7, Color(0, 0, 0))
    strip.show()

def turnOff3(strip, wait_ms=50):
    """Turn off all LEDs."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(8, Color(0, 0, 0))
        strip.setPixelColor(9, Color(0, 0, 0))
        strip.setPixelColor(10, Color(0, 0, 0))
        strip.setPixelColor(11, Color(0, 0, 0))
    strip.show()

def turnOff4(strip, wait_ms=50):
    """Turn off all LEDs."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(12, Color(0, 0, 0))
        strip.setPixelColor(13, Color(0, 0, 0))
        strip.setPixelColor(14, Color(0, 0, 0))
        strip.setPixelColor(15, Color(0, 0, 0))
    strip.show()

def turnOff5(strip, wait_ms=50):
    """Turn off all LEDs."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(16, Color(0, 0, 0))
        strip.setPixelColor(17, Color(0, 0, 0))
        strip.setPixelColor(18, Color(0, 0, 0))
        strip.setPixelColor(19, Color(0, 0, 0))
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

    try:
        while datetime.now() < start_time + timedelta(seconds=INTERVAL):
            whiteLight(strip)
            turnOff2(strip)

        while datetime.now() < light2 + timedelta(seconds=INTERVAL):
            whiteLight2(strip)
            turnOff1(strip)

        while datetime.now() < light3 + timedelta(seconds=INTERVAL):
            whiteLight3(strip)
            turnOff1(strip)
            turnOff2(strip)

        while datetime.now() < light4 + timedelta(seconds=INTERVAL):
            whiteLight4(strip)
            turnOff1(strip)
            turnOff2(strip)
            turnOff3(strip)

        while datetime.now() < light5 + timedelta(seconds=INTERVAL):
            whiteLight5(strip)
            turnOff1(strip)
            turnOff2(strip)
            turnOff3(strip)
            turnOff4(strip)

        while datetime.now() < light6 + timedelta(seconds=INTERVAL):
            whiteLight(strip)
            turnOff2(strip)
            turnOff3(strip)
            turnOff4(strip)
            turnOff5(strip)

        while datetime.now() < light7 + timedelta(seconds=INTERVAL):
            whiteLight(strip)
            turnOff2(strip)

        while datetime.now() < light8 + timedelta(seconds=INTERVAL):
            whiteLight2(strip)
            turnOff1(strip)

        while datetime.now() < light9 + timedelta(seconds=INTERVAL):
            whiteLight3(strip)
            turnOff1(strip)
            turnOff2(strip)

        while datetime.now() < light10 + timedelta(seconds=INTERVAL):
            whiteLight4(strip)
            turnOff1(strip)
            turnOff2(strip)
            turnOff3(strip)

        while datetime.now() < light11 + timedelta(seconds=INTERVAL):
            whiteLight5(strip)
            turnOff1(strip)
            turnOff2(strip)
            turnOff3(strip)
            turnOff4(strip)

        while datetime.now() < light12 + timedelta(seconds=INTERVAL):
            whiteLight(strip)
            turnOff2(strip)
            turnOff3(strip)
            turnOff4(strip)
            turnOff5(strip)

        while datetime.now() < light13 + timedelta(seconds=INTERVAL):
            whiteLight(strip)
            turnOff2(strip)

        while datetime.now() < light14 + timedelta(seconds=INTERVAL):
            whiteLight2(strip)
            turnOff1(strip)

        while datetime.now() < light15 + timedelta(seconds=INTERVAL):
            whiteLight3(strip)
            turnOff1(strip)
            turnOff2(strip)

        while datetime.now() < light16 + timedelta(seconds=INTERVAL):
            whiteLight4(strip)
            turnOff1(strip)
            turnOff2(strip)
            turnOff3(strip)

        while datetime.now() < light17 + timedelta(seconds=INTERVAL):
            whiteLight5(strip)
            turnOff1(strip)
            turnOff2(strip)
            turnOff3(strip)
            turnOff4(strip)

        while datetime.now() < light18 + timedelta(seconds=INTERVAL):
            whiteLight(strip)
            turnOff2(strip)
            turnOff3(strip)
            turnOff4(strip)
            turnOff5(strip)

        while datetime.now() < light19 + timedelta(seconds=INTERVAL):
            whiteLight(strip)
            turnOff2(strip)

        while datetime.now() < light21 + timedelta(seconds=INTERVAL):
            whiteLight2(strip)
            turnOff1(strip)

        while datetime.now() < light22 + timedelta(seconds=INTERVAL):
            whiteLight3(strip)
            turnOff1(strip)
            turnOff2(strip)

        while datetime.now() < light23 + timedelta(seconds=INTERVAL):
            whiteLight4(strip)
            turnOff1(strip)
            turnOff2(strip)
            turnOff3(strip)

        while datetime.now() < light24 + timedelta(seconds=INTERVAL):
            whiteLight5(strip)
            turnOff1(strip)
            turnOff2(strip)
            turnOff3(strip)
            turnOff4(strip)

        while datetime.now() < light25 + timedelta(seconds=INTERVAL):
            whiteLight(strip)
            turnOff2(strip)
            turnOff3(strip)
            turnOff4(strip)
            turnOff5(strip)

        while datetime.now() < end + timedelta(seconds=INTERVAL):
            turnOffAll(strip)

    except KeyboardInterrupt:
        turnOffAll(strip)
