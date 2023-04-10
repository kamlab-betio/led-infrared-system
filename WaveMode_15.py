#from typing_extensions import runtime
import sys
import edit_json
import threading
import Button
import Led
import ColorSample
import time
from concurrent.futures.thread import ThreadPoolExecutor


recv_data18 = [0] * 37
recv_data24 = [0] * 37
recv_data12 = [0] * 37
recv_data6 = [0] * 37

wave_direction = [0, 0, 0, 0]
count = 0
# now_data[方位データ, 光データ, 角判定データ, タイムテーブル, 最大震度]
now_data = [0] * 37
now_data[0] = 30
now_data[10] = 77
# now_data[36] = 100

button_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

magnitude = 0


##########################
#インスタンス化
button =  Button.Button()
wave_led = Led.Led()
##########################

################################################################################
# 初期化関数
def control_reset():
    #初期化をするタイミングを見てる
    
    edit_json.reset()
    print("edit_json.reset() fin")

    global wave_direction
    wave_direction = [0, 0, 0, 0]
    global button_data
    button_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    global recv_data18 
    recv_data18 = [0] * 37
    global recv_data24
    recv_data24 = [0] * 37
    global recv_data12
    recv_data12 = [0] * 37
    global recv_data6
    recv_data6 = [0] * 37


    global count
    count = 0
    # now_data[方位データ, 光データ, 角判定データ, タイムテーブル, 最大震度]
    global now_data
    now_data = [0] * 37
    now_data[0] = 30
    now_data[10] = 77
    # now_data[36] = 100

    global magnitude
    magnitude = 0

    print("reset fin")

################################################################################

################################################################################
#[筐体内の最大震度を求める関数]
def max_magnitude_here_func(now_data):
    max_magnitude_here = 0
    for i in range(1,10):
        if max_magnitude_here < now_data[i]:
            max_magnitude_here = now_data[i]

    print(f"この筐体の最大震度 ＝ {max_magnitude_here}")
    return max_magnitude_here

################################################################################


################################################################################
#[配列の大小比較関数]
def comparison(now_data,new_data):
    for n in range(37):
        if now_data[n] < new_data[n]:
            now_data[n] = new_data[n]

    return now_data

################################################################################

################################################################################
#[波紋データ作成関数]
def light_data_creator(button_data):
    push_index = 0

    light_data = [0] * 10
    # button_data[0] = 100

    for n in range(1,10):
        if button_data[n] > 0:
            push_index =  n

    if push_index == 1:
        light_data = [0,0,1,2,1,1,2,2,2,2]
    elif push_index == 2:
        light_data = [0, 1, 0, 1, 1, 1, 1, 2, 2, 2]
    elif push_index == 3:
        light_data = [0, 2, 1, 0, 2, 1, 1, 2, 2, 2]
    elif push_index == 4:
        light_data = [0, 1, 1, 2, 0, 1, 2, 1, 1, 2]
    elif push_index == 5:
        light_data = [0, 1, 1, 1, 1, 0, 1, 1, 1, 1]
    elif push_index == 6:
        light_data = [0, 2, 1, 1, 2, 1, 0, 2, 1, 1]
    elif push_index == 7:
        light_data = [0, 2, 2, 2, 1, 1, 2, 0, 1, 2]
    elif push_index == 8:
        light_data = [0, 2, 2, 2, 1, 1, 1, 1, 0, 1]
    elif push_index == 9:
        light_data = [0, 2, 2, 2, 2, 1, 1, 2, 1, 0]


    return light_data

################################################################################

################################################################################
#[波紋の震度を求める関数]
def magnitude_creator(max_button_data):
    global magnitude
    if max_button_data == 1:
        magnitude = 5
    elif max_button_data == 2:
        magnitude = 10
    elif max_button_data == 3:
        magnitude = 15
    elif max_button_data == 4:
        magnitude = 20
    elif max_button_data == 5:
        magnitude = 25

    return magnitude
################################################################################

################################################################################
# 光情報が追加されたdataにタイムテーブルを追加(上書き)
def complete_data_creator(time_table, data, light_data):

    print(data)
    print(f"time_table = {time_table}")
    print(f"light_data = {light_data}")

    for n in range(0,10):
        data[n] = light_data[n]

    for n in range(10,36):
        data[n] = time_table[n]

    # data[36] = 100
    return data

################################################################################

################################################################################
#[タイムテーブル作成関数]
def time_table_creator(now_unix_time):
    now_unix_time = now_unix_time + 1
    set_time_table = [0] * 11
    for n in range(25):
        set_time_table.append(now_unix_time)
        #LEDの点灯する間隔を設定
        now_unix_time = now_unix_time + 2
        if now_unix_time == 100:
            now_unix_time = 0
        elif now_unix_time > 100:
            now_unix_time = 1

        if now_unix_time == 0:
            now_unix_time = now_unix_time + 1

    # print(set_time_table)
    return set_time_table
################################################################################

################################################################################
# [現在のunix時間を計測する関数]
def get_time():
    now_unix_time = time.time()
    now_unix_time =  int(now_unix_time)
    now_unix_time_2 = int(now_unix_time / 100)
    # print(now_unix_time_2)
    now_unix_time_2 = now_unix_time_2 * 100
    # print(now_unix_time_2)
    now_unix_time = int(now_unix_time - now_unix_time_2)
    # print(now_unix_time)

    # print("now_unix_time")
    # print(now_unix_time)

    now_unix_time = now_unix_time + 20

    if now_unix_time >= 100:
        now_unix_time = now_unix_time - 100
    
    return now_unix_time

################################################################################

################################################################################
#[波紋データ作成関数]
def wave_data_creator(button_data):

    data = [0] * 37

    light_data = light_data_creator(button_data)
    now_unix_time = get_time()
    time_table = time_table_creator(now_unix_time)
    complete_data = complete_data_creator(time_table, data, light_data)

    magnitude = magnitude_creator(max(button_data))
    print(f"magnitude = {magnitude}")
    complete_data[36] = magnitude

    complete_data[10] = 77

    return complete_data

################################################################################

################################################################################
#受信関数_18
def recv_18():
    global recv_data18
    global wave_direction
    global count
    global now_data

    recv_data18 = edit_json.getjson_18()

    if recv_data18 is not None:
        wave_direction[0] = 1
        print(f"recv_data18={recv_18}")
        # count = 1

        if recv_data18[0] == 0:
            count = count + 2
            now_data = recv_data18
            print(f"受信しました! 先頭0= {wave_direction}")
        elif recv_data18[0] != 0:
            # wave_direction[1] = 1
            count = count+1
            now_data = comparison(now_data, recv_data18)
            print(f"受信しました! 先頭１= {wave_direction}")
    print(f"18count = {count}")
################################################################################

################################################################################
#受信関数_24
def recv_24():
    global recv_data24
    global wave_direction
    global count
    global now_data

    recv_data24 = edit_json.getjson_24()

    if recv_data24 is not None:
        wave_direction[1] = 1
        print(f"recv_data24={recv_24}")
        if recv_data24[0] == 0:
            count = count + 2
            now_data = recv_data24
            print(f"受信しました! = {wave_direction}")

        elif recv_data24[0] != 0:
            count = count+1
            now_data = comparison(now_data, recv_data24)
            print(f"受信しました! = {wave_direction}")
    print(f"24count = {count}")
################################################################################

################################################################################
#受信関数_12
def recv_12():
    global recv_data12
    global wave_direction
    global count
    global now_data

    recv_data12 = edit_json.getjson_12()
    if recv_data12 is not None:
        wave_direction[2] = 1
        print(f"recv_data12={recv_12}")
        if recv_data12[0] == 0:
            count = count + 2
            now_data = recv_data12
            print(f"受信しました! 先頭０= {wave_direction}")
        elif recv_data12[0] != 0:
            count = count + 1
            now_data = comparison(now_data, recv_data12)
            print(f"受信しました! 先頭１= {wave_direction}")
    print(f"12count = {count}")
################################################################################

################################################################################
#受信関数_6
def recv_6():
    global recv_data6
    global wave_direction
    global count
    global now_data

    recv_data6 = edit_json.getjson_6()

    if recv_data6 is not None:
        wave_direction[3] = 1
        print(f"recv_data6={recv_6}")
        if recv_data6[0] == 0:
            count = count + 2
            now_data = recv_data6
            print(f"受信しました! = {wave_direction}")
        elif recv_data6[0] != 0:
            count = count + 1
            now_data = comparison(now_data, recv_data6)
            print(f"受信しました! = {wave_direction}")
    print(f"6count = {count}")
################################################################################

################################################################################
#button受信関数
def button_recv():
    # button =  Button.Button()
    global button
    global button_data
    button_recv_count = 600

    for i in range(button_recv_count):
        button_data = button.get_button_list_wave()
        if button_data.count(0) != 10:
            break

    print(f"取得したボタンデータ = {button_data}")
################################################################################

################################################################################
#[制御_受信関数]
def recv_data_and_button_data():

    global recv_data18
    global recv_data24
    global recv_data12
    global recv_data6

    global wave_direction
    global button_data
    global count

    while True:

        thread18 = threading.Thread(target=recv_18)
        thread24 = threading.Thread(target=recv_24)
        thread12 = threading.Thread(target=recv_12)
        thread6 = threading.Thread(target=recv_6)

        thread_button = threading.Thread(target=button_recv)

        thread18.start()
        thread24.start()
        thread12.start()
        thread6.start()
        thread_button.start()


        thread18.join()
        thread24.join()
        thread12.join()
        thread6.join()
        # thread_button.join()
        

        if count == 2 or button_data.count(0) != 10:

            print(f"wave_direction = {wave_direction}")
            print(f"button_data = {button_data}")
            break

        elif  count > 2:
            # print("count error")
            print(wave_direction)
            control_reset()
            sys.exit("error : wave_direction count error")
            # time.sleep(10) 
        # else:
        #     continue
        

################################################################################

################################################################################
#[送信関数]
def send_data(now_data,wave_direction):
    print("送信開始")

        # 18方向へ送信
    if wave_direction[0] == 0:
        if wave_direction[2] == 1 and wave_direction.count(1) == 1:
            now_data[10] = 0
        now_data[0] = 18
        print(f"18送信now_data={now_data}")
        edit_json.cpy_json_18(now_data)
        now_data[10] = 77

        time.sleep(1.0)
           
        # 24方向へ送信
    if wave_direction[1] == 0:
        if wave_direction[3] == 1 and wave_direction.count(1) == 1:
            now_data[10] = 0
        now_data[0] = 24
        print(f"24送信now_data={now_data}")
        edit_json.cpy_json_24(now_data)
        now_data[10] = 77

        time.sleep(1.0)

        # 12方向へ送信
    if wave_direction[2] == 0:
        if wave_direction[0] == 1 and wave_direction.count(1) == 1:
            now_data[10] = 0
        now_data[0] = 12
        print(f"12送信now_data={now_data}")
        edit_json.cpy_json_12(now_data)
        now_data[10] = 77

        time.sleep(1.0)

        # 6方向へ送信
    if wave_direction[3] == 0:
        if wave_direction[1] == 1 and wave_direction.count(1) == 1:
            now_data[10] = 0
        now_data[0] = 6
        print(f"6送信now_data={now_data}")
        edit_json.cpy_json_6(now_data)
        now_data[10] = 77
        # time.sleep(0.5)
        
################################################################################
################################################################################
def sub_procces(data_1,data_2):
    # now_data = []
    global now_data
    # now_data = wave_data_creator(data_1)
    # now_data = wave_data_creator(data_2)
    now_data = comparison(now_data,data_1)
    now_data = comparison(now_data,data_2)
    print(f"now_data = {now_data}")

################################################################################
# ################################################################################


def control():
    ##########################
    #インスタンス化
    # button =  Button.Button()
    # wave_led = Led.Led()
    ##########################

    global wave_direction
    global now_data
    global button_data

    global wave_led
    # button_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    
    # if flag[0] == True:
    #     break
    # 赤外線データとボタンデータをスレッドで取得
    # 関数内ではwhileでループしてある。

    while True:
        # 赤外線受信とボタンデータの受け取りを関数内でスレッド化して実行する
        recv_data_and_button_data()

        # 赤外線を受信(波紋データを受信)していた場合の処理
        if wave_direction.count(0) != 4 and button_data.count(0) == 10:
            
            # この筐体内の最大震度を求める
            max_magnitude_here = max_magnitude_here_func(now_data)
            print(f"この筐体の最大震度 = {max_magnitude_here}")
                
            # この筐体内の最大震度と、波紋データの最大震度が等しい場合、この筐体で波紋データの最大震度を迎えるということになるので、
            # 隣の筐体へは送信をしてはいけない
            if max_magnitude_here != now_data[36]:
                send_data(now_data,wave_direction)

            elif max_magnitude_here == now_data[36]:
                for n in range(1,10):
                    if now_data[n] == max_magnitude_here:
                        now_data[0] = 0
                    
            time.sleep(1)

            # 受信したことを知らせるために一つだけLEDを点灯させる
            wave_led.color_rec()

            # 波紋状にLEDを光らせるように命令
            wave_led.color_wave(now_data)
            print("color_wave fin")
            wave_led.color_clear()
            print("color_clear fin")
            # 初期化関数
            control_reset()

            print("control fin")
            
        elif button_data.count(0) != 10 and wave_direction.count(0) == 4:
            # button_dataから波紋データ(now_data)を作成
            now_data = wave_data_creator(button_data)
            print(f"now_data = {now_data}")
                
            # この筐体内の最大震度を求める
            max_magnitude_here = max_magnitude_here_func(now_data)
            print(f"この筐体の最大震度 = {max_magnitude_here}")
                
            send_data(now_data,wave_direction)
            time.sleep(1)
            wave_led.color_wave(now_data)
            print("color_wave fin")
            # time.sleep(3)
            wave_led.color_clear()
            print("color_clear fin")
            # 初期化関数
            control_reset()
            print("control fin")    


# ################################################################################



if __name__ == '__main__':
    # get_button_list = Button.Button.get_button_list
    # button =  Button.Button()

    control()
    # data_1 = [18,3,3,3,4,4,4,5,5,5,77,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5]
    # data_2 = [24,3,3,3,4,4,4,5,5,5,77,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5]
    # print(f"data_1 = {data_1}")
    # print(f"data_2 = {data_2}")
    # # print(len(data_1))
    # sub_procces(data_1,data_2)
