from machine import Pin
from neopixel import NeoPixel
import time, random

np = NeoPixel(Pin(5), 20, bpp=3)

step = 32

def light_on():
    while True:
        for i in range(20):
            for j in range(20):
                np[j] = tuple(( max(0, val - step) for val in np[j]))
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            np[i] = (r, g, b)
            np.write()
            time.sleep(0.05)
