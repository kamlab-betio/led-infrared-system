import time
import board
import neopixel
import RPi.GPIO as GPIO

pixel_pin = board.D18   # GPIO-PIN-NO
num_pixels = 9          # The number of NeoPixels

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.02, auto_write=False, pixel_order=ORDER
)

pixels.fill((255,0,0))
pixels.show()
time.sleep(5)
pixels.fill((0,0,0))
pixels.show()
# GPIO.output(, GPIO.LOW) 
# GPIO.cleanup()
