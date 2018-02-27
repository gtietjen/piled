import time
import atexit
from datetime import datetime, timedelta
from neopixel import Adafruit_NeoPixel, Color


# LED strip configuration:
LED_COUNT = 16      # Number of LED pixels.
LED_PIN = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT = False   # True to invert the signal (when using NPN transistor level shift)
INTERVAL = 5

def whiteLight(strip, wait_ms=50):
    """Turn off all LEDs."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(200, 255, 255))
    strip.show()
    time.sleep(wait_ms/1000.0)


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
    try:
        while datetime.now() < start_time + timedelta(seconds=INTERVAL):
            whiteLight(strip)

    except KeyboardInterrupt:
        turnOffAll(strip)
