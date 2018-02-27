import time

from neopixel import *


# LED strip configuration:
LED_COUNT      = 1     
LED_PIN        = 12
LED_FREQ_HZ    = 800000  
LED_DMA        = 5      
LED_BRIGHTNESS = 255    
LED_INVERT     = False   

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

# Main program logic follows:
if __name__ == '__main__':

    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    strip.begin()

    print 'Press Ctrl-C to quit.'
    while True:
        # Color wipe animations.
        colorWipe(strip, Color(255,203,5))  # Maize wipe
        colorWipe(strip, Color(0,39,76))  # Blue wipe
