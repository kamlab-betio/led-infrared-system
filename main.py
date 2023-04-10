#!/bin/python3
## -*- coding: utf-8 -*-
import RPi.GPIO as GPIO 
import pigpio as pi
# import neopixel
# import ColorSample
import time
#import Led
# import board
import Only_Led
import WaveMode_15

# pixel_pin=board.D18
# num_pixels=9
# ORDER=neopixel.GRB

# pixels = neopixel.NeoPixel(
#         pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER)

only_led = Only_Led.Only()

#ポート番号の定義
Sw_pin = 22                         #変数"Sw_pin"に22を代入
Sw1_pin = 26
Led1_pin = 23                        #変数"Led1_pin"に23を代入
Led2_pin = 24                        #変数"Led2_pin"に24を代入

#電源
PIN = 3        #変数”PIN”に3を代入
Led_pin = 25        #変数”Led_pin"に25を代入

#GPIOの設定
GPIO.setmode(GPIO.BCM)#GPIOのモードを"GPIO.BCM"に設定

#GPIO22を入力モードに設定してプルダウン抵抗を有効にする
GPIO.setup(Sw_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Led1_pin, GPIO.OUT)       #GPIO23を出力モードに設定
GPIO.setup(Led2_pin, GPIO.OUT)       #GPIO24を出力モードに設定

#電源
# プルアップ抵抗を有効にする
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Led_pin, GPIO.OUT)         #GPIO25を出力モードに設定
GPIO.output(Led_pin, GPIO.HIGH)    #GPIO25の出力をHIGH(3.3V)にする


flag = True

#単体・複数の切り替え
def my_callback(Sw_pin):
    global flag
    flag = not flag


GPIO.add_event_detect(Sw_pin, GPIO.RISING, callback=my_callback, bouncetime=500)


while True:
    
    if flag:
        # LEDが冒頭から光ってしまうことを防止する
        #only_led.color_off()

        GPIO.output(Led2_pin, GPIO.LOW)
        GPIO.output(Led1_pin, GPIO.HIGH)
        # sb.process()
        only_led.light()

        time.sleep(0.05)

    else:
        GPIO.output(Led1_pin, GPIO.LOW)
        GPIO.output(Led2_pin, GPIO.HIGH)
        
        # 各変数をリセット
        WaveMode_15.control_reset()
        #波紋モードの実
        #インスタンス名前.関数名
        print("wave_mode start")
        WaveMode_15.control()
        print("wave_mode fin")
        # flag = True

        # pixels.fill((255,0,0))
        # pixels.show()
        # time.sleep(2)
        # pixels.fill((0,0,0))
        # pixels.show()
        
        time.sleep(0.05)
