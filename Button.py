#2021/12/16 by Senzaki(19RD102)
import spidev
import random
import board
import neopixel
import ColorSample

pixel_pin=board.D18
num_pixels=9
ORDER=neopixel.GRB

pixels = neopixel.NeoPixel(
        pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER)

class Button:

    # コンストラクタ
    def __init__(self):
        # spiの設定
        self.spi1 = spidev.SpiDev()   #シリアル通信用メソッドの宣言
        self.spi1.open(0,0)   #bus0, cs0
        self.spi1.max_speed_hz = 200000  #動作スピード(2MHz)

        self.spi2 = spidev.SpiDev()
        self.spi2.open(0,1)   #bus0, cs1
        self.spi2.max_speed_hz = 200000  #動作スピード(2MHz)

        self.Vref = 5.177 #基準電圧
        
        print("Button Ready")
    
    # デストラクタ
    def __del__(self):
        self.spi1.close()
        self.spi2.close()
        print("spi closed")
    
    # ボタン番号を指定して入力の強弱を返すメソッド
    def get_button_single_shot(self, channel):
        if (channel < 1 or channel > 9):
            raise IndexError("A/D channel is out of range") #範囲外のボタンを指定した場合
        value = self.power_judge(self.__get_volt(channel))
        return value
    
    # ボタン番号を指定して入力の最大値を返すメソッド
    def get_button_single_hold(self, channel):
        if (channel < 1 or channel > 9):
            raise IndexError("A/D channel is out of range") #範囲外のボタンを指定した場合

        maxvalue = 0

        value = self.power_judge(self.__get_volt(channel))
        if value == 0:
            return 0
        else:
            maxvalue = value
            while True:
                volt = self.__get_volt(channel)
                value = self.power_judge(volt)
                if volt <= 0.8:
                    return maxvalue
                elif value > maxvalue:
                    maxvalue = value
                else:
                    pass
            
#########################################################################
    # 全てのボタンのうち、入力があったボタンの入力の最大値を返すメソッド
    def get_button_list_wave(self):
        # アクセスするボタンの順番を指定

       

        pixels[4]=ColorSample.blue() #blue
        pixels.show()

        lis = list(range(1, 10))
        random.shuffle(lis) # ランダム
        
        b = [0,0,0,0,0,0,0,0,0,0] #返すリスト
        maxvalue = 0
        for i in lis:
            value = self.power_judge(self.__get_volt(i))

            if value == 0:
                continue
            else:
                maxvalue = value
                while True:
                    volt = self.__get_volt(i)
                    value = self.power_judge(volt)
                    if volt <= 0.8:
                        b[i] = maxvalue
                        return b
                    elif value > maxvalue:
                        maxvalue = value
                    else:
                        pass

        pixels.fill((ColorSample.black()))
        pixels.show()

        return b
#################################################################################
    # 全てのボタンを監視し、入力があったボタンを返すメソッド
    def get_button_list_solo(self):
        # アクセスするボタンの順番を指定
        lis = list(range(1, 10))
        #random.shuffle(lis) # ランダム

        b = [0,0,0,0,0,0,0,0,0,0] #返すリスト
        for i in lis:
            value = self.power_judge(self.__get_volt(i))
            if value > 0:
                b[i] = 1
                break            
        return b
    
    # ボタン番号を指定してアナログ電圧を返すメソッド(外部呼び出し用)
    def get_button_volt(self, channel):
        if (channel < 1 or channel > 9):
            raise IndexError("A/D channel is out of range") #範囲外のボタンを指定した場合
        
        return self.__get_volt(channel) #データの取得

    # ボタンを指定してアナログ電圧を取得するメソッド(内部処理用)
    def __get_volt(self, channel):
        channel = channel - 1
        # A/Dコンバータと通信
        if channel == 8:
            adc = self.spi2.xfer2([0x06, 0x00, 0x00])
        elif channel > 3:
            adc = self.spi1.xfer2([0x07, channel - 4 << 6, 0x00])
        else:
            adc = self.spi1.xfer2([0x06, channel << 6, 0x00])
    
        # 取得したデータの整形
        data = ((adc[1] & 0x0f) << 8) | adc[2]
        p_data = self.Vref * data / 4096
        p_data = round(p_data, 5)

        return p_data
    
    # 電圧を強弱に変換するメソッド
    def power_judge(self, data):
        
        #取得したデータの判定
        if data >= 3.6:
            return 5
        elif data >= 3.3:
            return 4
        elif data >= 2.8:
            return 3
        elif data >= 2.4:
            return 2
        elif data >= 2.0:
            return 1
        else:
            return 0
    