from neopixel import *

LED_COUNT   = 12
LED_PIN     = 18
LED_FREQ_HZ = 800000
LED_DMA     = 5
LED_INVERT  = False

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
strip.begin()
strip.setPixelColor(0, Color(255,255,255))
strip.setPixelColor(1, Color(255,255,255))
strip.setPixelColor(2, Color(255,255,255))
strip.setPixelColor(3, Color(255,255,255))
strip.setPixelColor(4, Color(255,255,255))
strip.setPixelColor(5, Color(255,255,255))
strip.setPixelColor(6, Color(255,255,255))
strip.setPixelColor(7, Color(255,255,255))
strip.setPixelColor(8, Color(255,255,255))
strip.setPixelColor(9, Color(255,255,255))
strip.setPixelColor(10, Color(255,255,255))
strip.show()
