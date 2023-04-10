import time
import board
import neopixel
import ColorSample
import Button


pixel_pin = board.D18   # GPIO-PIN-NO
num_pixels = 9          # The number of NeoPixels

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER
)

class Only:

    def __init__(self):
        self.button = Button.Button()
        
    def color_all(self):
        pixels.fill(ColorSample.red())
        pixels.show()
    
    def color_off(self):
        pixels.fill(ColorSample.black())
        pixels.show()
    
    def color_one(self):
        pixels[0] = ColorSample.red()
        pixels[1] = ColorSample.lightblue()
        pixels[2] = ColorSample.green()
        pixels[3] = ColorSample.lightgreen()
        pixels[4] = ColorSample.purple()
        pixels[5] = ColorSample.orange()
        pixels[6] = ColorSample.yellow()
        pixels[7] = ColorSample.pink()
        pixels[8] = ColorSample.blue()
        pixels.show()
    
    def light(self):
        #print("only_light now")
        data = self.button.get_button_list_solo()
        print(data)
        for i in range(9):
            if(data[i+1]>=1):
                    if i==0:
                        pixels[i] = ColorSample.red()
                        # pixels.show()
                    elif i==1:
                        pixels[i] = ColorSample.lightblue()
                    elif i==2:
                        pixels[i] = ColorSample.green()
                    elif i==3:
                        pixels[i] = ColorSample.lightgreen()
                    elif i==4:
                        pixels[i] = ColorSample.purple()
                    elif i==5:
                        pixels[i] = ColorSample.orange()
                    elif i==6:
                        pixels[i] = ColorSample.yellow()
                    elif i==7:
                        pixels[i] = ColorSample.pink()
                    elif i==8:
                        pixels[i] = ColorSample.blue()
            else:
                pixels[i] = ColorSample.black()     
        pixels.show()