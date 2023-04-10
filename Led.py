import time
import board
import neopixel
import ColorSample

pixel_pin=board.D18
num_pixels=9

ORDER=neopixel.GRB

pixels = neopixel.NeoPixel(
        pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER)

class Led:
    def __init__(self):
        pixels.fill((ColorSample.black()))
    
    def color_rec(self):
        pixels[4]=ColorSample.orange()
        pixels.show()
        # time.sleep(2)
        # pixels[4]=ColorSample.black()
        # pixels.show()
        

    def color_all(self):
        #white
        #pixels.fill((255,0,0)) #色指定
        pixels.fill(ColorSample.white()) #色指定（自作パッケージ参照）
        pixels.show() #発光
        time.sleep(5) #時間指定（５秒間）

    def color_clear(self):
        print("color_clear start")
        #black
        #pixels.fill((0,0,0)) #色指定
        pixels.fill((ColorSample.black())) #色指定（自作パッケージ参照）
        pixels.show() #発光

    def color_set(self):
        test=[0,0,1,0,0,0,0,0,2]
        #i=0
        for i in range(1,10): #実際はrange(9)
            if(test[i]>=1): #1以上だったら
                if button_log[i-1]!=1:
                    pixels[i-1]=ColorSample.white() #white
                else:
                    pixels[i-1]=ColorSample.black() #black
                #pass
        pixels.show() #発光
        #time.sleep(5) #時間指定（５秒間）
        
        
    def get_time(self):
        now_unix_time = time.time()
        now_unix_time =  int(now_unix_time)
        now_unix_time_2 = int(now_unix_time / 100)
        # print(now_unix_time_2)
        now_unix_time_2 = now_unix_time_2 * 100
        # print(now_unix_time_2)
        now_unix_time = int(now_unix_time - now_unix_time_2)
        # print(now_unix_time)
        return now_unix_time

    def color_wave(self,time):
        print("color_wave start")
        print(time)

        test = [30]*10
        data=time
        while True:
            # print("while now")
            print(test)
            for LED_index in range(1,10):
                LED_data = int(data[LED_index])
                print(f"LED_data = {LED_data}")
                if LED_data == 0:
                    test[LED_index] = 0
                LED_order_time = data[LED_data + 10]

                now_time = self.get_time()
                # print(now_time)

                if now_time > LED_order_time:
                    increment = LED_order_time - now_time
                    increment = increment + 3
                    now_time = now_time - increment

                print(f"now_time = {now_time}")
                print(f"LED_order_time = {LED_order_time}")

                if now_time == LED_order_time:
                        test[LED_index] = LED_data

                        # time[LED_index] = now_time 
                        # print("ifに入った")                       
                        # time.sleep(5)
                        print(test)

                        if LED_data==1 or LED_data == 9 or LED_data==17 or LED_data==25: #1,9,17,25,33
                            pixels[LED_index-1]=ColorSample.red() #red
                                #pixels.show()
                        elif LED_data==2 or LED_data==10 or LED_data==18 : #2,10,18,26,34
                            pixels[LED_index-1]=ColorSample.orange() #orange
                                #pixels.show()
                        elif LED_data==3 or LED_data==11 or LED_data==19: #3,11,19,27,35
                            pixels[LED_index-1]=ColorSample.yellow() #yellow
                                #pixels.show()
                        elif LED_data==4 or LED_data==12 or LED_data==20: #4,12,20,28,36
                            pixels[LED_index-1]=ColorSample.lightgreen() #lightgreen
                                #pixels.show()
                        elif LED_data==5 or LED_data==13 or LED_data==21 : #5,13,21,29
                            pixels[LED_index-1]=ColorSample.green() #green
                                #pixels.show()
                        elif LED_data==6 or LED_data==14 or LED_data==22 : #6,14,22,30
                            pixels[LED_index-1]=ColorSample.lightblue() #lightblue
                                #pixels.show()
                        elif LED_data==7 or LED_data==15 or LED_data==23 : #7,15,23,31
                            pixels[LED_index-1]=ColorSample.blue() #blue
                                #pixels.show()
                        elif LED_data==8 or LED_data==16 or LED_data==24: #8,16,24,32
                            pixels[LED_index-1]=ColorSample.purple() # purple
                                #pixels.show()
            pixels.show() #発光


            if test.count(30) == 1:
                # time.sleep(2)
                print(test)
                print("Led break")
                break
            
        while True:
            now_time = self.get_time()
            print(f"del_now_time = {now_time}")
            fin_time = data[data[36] + 10] + 3
            if fin_time >= 100:
                fin_time = fin_time - 100
            if fin_time == 0:
                fin_time = 1
            if fin_time == now_time :
                # time.sleep(2)
                pixels.fill((ColorSample.black()))
                pixels.show()
                print("Led del")
                break
        # time.sleep(2)
        # pixels.fill((ColorSample.black()))
        # pixels.show()
        
        
        """
    def color_wave(self):
        #test=[0,1,2,3,4,5,6,7,8]
        #test=[0,9,10,11,12,13,14,15,16]
        test=[0,0,5,3,14,23,35,5,0]
        #j=0
        for i in range(8): #実際はrange(9)
            j=0 #初期化
            #if(ans[i+1]>=1):
            for n in range(36): #0~36番目
                if(test[i+1]==n+1):
                    if j==0: #1,9,17,25,33
                        pixels[i]=ColorSample.red() #red
                    elif j==1: #2,10,18,26,34
                        pixels[i]=ColorSample.orange() #orange
                    elif j==2: #3,11,19,27,35
                        pixels[i]=ColorSample.yellow() #yellow
                    elif j==3: #4,12,20,28,36
                        pixels[i]=ColorSample.lightgreen() #lightgreen
                    elif j==4: #5,13,21,29
                        pixels[i]=ColorSample.green() #green
                    elif j==5: #6,14,22,30
                        pixels[i]=ColorSample.lightblue() #lightblue
                    elif j==6: #7,15,23,31
                        pixels[i]=ColorSample.blue() #blue
                    else: #8,16,24,32
                        pixels[i]=ColorSample.purple() # purple
                #print("j=",j)
                j=j+1
                if(j==8): #8のとき初期化
                    j=0
        pixels.show() #発光
        time.sleep(5) #時間指定（５秒間）実装時に消す
        """    
    
    
    """ 
    def wheel(pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3)
            g = int(255 - pos * 3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos * 3)
            g = 0
            b = int(pos * 3)
        else:
            pos -= 170
            r = 0
            g = int(pos * 3)
            b = int(255 - pos * 3)
        return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

 
 
    
    def rainbow_cycle(wait):
        for j in range(255):
            for i in range(num_pixels):
                pixel_index = (i * 256 // num_pixels) + j
                pixels[i] = ModeTest.wheel(pixel_index & 255)
            pixels.show()
            time.sleep(0.01)
    """


    #color_all() #実行
    #color_one() #実行
