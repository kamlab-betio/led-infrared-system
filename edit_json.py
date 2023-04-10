import cgir_6
import cgir_12
import cgir_18
import cgir_24

import json
import subprocess
import time



#####################実行コマンド####################

def encode(udlr):
    try:
        if udlr == 6:
            runcmd = subprocess.call('./cgirtool_6.py enc -f signal_6.json signal_6'.split())
            print(runcmd)
        elif udlr == 12:
            runcmd = subprocess.call('./cgirtool_12.py enc -f signal_12.json signal_12'.split())
            print(runcmd)
        elif udlr == 18:
            runcmd = subprocess.call('./cgirtool_18.py enc -f signal_18.json signal_18'.split())
            print(runcmd)
        elif udlr == 24:
            runcmd = subprocess.call('./cgirtool_24.py enc -f signal_24.json signal_24'.split())
            print(runcmd)
        else:
            print('error')
    except:
        print('command_error')

def decode(udlr):
    try:
        if udlr == 6:
            runcmd = subprocess.call('./cgirtool_6.py dec -f signal_6.json signal_6'.split())
            print(runcmd)
        elif udlr == 12:
            runcmd = subprocess.call('./cgirtool_12.py dec -f signal_12.json signal_12'.split())
            print(runcmd)
        elif udlr == 18:
            runcmd = subprocess.call('./cgirtool_18.py dec -f signal_18.json signal_18'.split())
            print(runcmd)
        elif udlr == 24:
            runcmd = subprocess.call('./cgirtool_24.py dec -f signal_24.json signal_24'.split())
            print(runcmd)
        else:
            print('error')
    except:
        print('command_error')

def send_infrared(udlr):
    try:
        if udlr == 6:
            runcmd = subprocess.call('./cgirtool_6.py send signal_6'.split())
            print(runcmd)
        elif udlr == 12:
            runcmd = subprocess.call('./cgirtool_12.py send signal_12'.split())
            print(runcmd)
        elif udlr == 18:
            runcmd = subprocess.call('./cgirtool_18.py send signal_18'.split())
            print(runcmd)
        elif udlr == 24:
            runcmd = subprocess.call('./cgirtool_24.py send signal_24'.split())
            print(runcmd)
        else:
            print('error')
    except Exception as e:
        print(e)
        print('command_error')

def receive_infrared(udlr):
    try:
        if udlr == 6:
            runcmd = subprocess.call('./cgirtool_6.py rec signal_6'.split())
            result = runcmd
            print(runcmd)
        elif udlr == 12:
            runcmd = subprocess.call('./cgirtool_12.py rec signal_12'.split())
            print(runcmd)
        elif udlr == 18:
            runcmd = subprocess.call('./cgirtool_18.py rec signal_18'.split())
            print(runcmd)
        elif udlr == 24:
            runcmd = subprocess.call('./cgirtool_24.py rec signal_24'.split())
            print(runcmd)
        else:
            print('error')
    except:
        print('command_error')

#############################################




###################リセット###################
def reset():

    #jsonファイルの中身を配列を初期化
    for i in range(1,5):
        number = (i * 6)
        with open('/home/pi/pi_test_betio/signal_'+str(number)+'.json','r') as f:
            json_dict = json.load(f)
        json_dict["data"][0] = [0] * 37

        #上書きした配列をjsonに書き直す
        with open('/home/pi/pi_test_betio/signal_'+str(number)+'.json','w') as f:
            json.dump(json_dict,f)
        
        encode(number)
        

    # #signal_12のリセット
    # with open('/home/pi/signal_12.json','r') as f:
    #     json_dict = json.load(f)
    # json_dict["data"] = [0] * 37 

    # #上書きした配列をjsonに書き直す
    # with open('/home/pi/signal_12.json','w') as f:
    #     json.dump(json_dict,f)

    # #signal_18のリセット
    # with open('/home/pi/signal_18.json','r') as f:
    #     json_dict = json.load(f)
    # json_dict["data"] = [0] * 37 

    # #上書きした配列をjsonに書き直す
    # with open('/home/pi/signal_18.json','w') as f:
    #     json.dump(json_dict,f)

    # #signal_24のリセット
    # with open('/home/pi/signal_24.json','r') as f:
    #     json_dict = json.load(f)
    # json_dict["data"] = [0] * 37 

    # #上書きした配列をjsonに書き直す
    # with open('/home/pi/signal_24.json','w') as f:
    #     json.dump(json_dict,f)


#############################################





#####################送信####################

#制御から送られてきた配列をjsonファイルに全コピー

#GPIOsend = XX GPIOrec =XX
def cpy_json_6(send_data):
    with open('/home/pi/pi_test_betio/signal_6.json','r') as f:
        json_dict = json.load(f)

        cpy_data = json_dict["data"]
    
        cpy_data = cpy_data[0]

        for i in range(len(cpy_data)):
            cpy_data[i] = send_data[i]
            
    json_dict["data"] = [cpy_data] 

    #上書きした配列をjsonに書き直す
    with open('/home/pi/pi_test_betio/signal_6.json','w') as f:
        json.dump(json_dict,f)
    #赤外線コード生成
    encode(6)

    # time.sleep(0.1)
    send_infrared(6)
    #赤外線コード送信
    # for i in range(5):
    # send_infrared(6)
    # time.sleep(0.05)
    


#GPIOsend = XX GPIOrec =XX
def cpy_json_12(send_data):
    with open('/home/pi/pi_test_betio/signal_12.json','r') as f:
        json_dict = json.load(f)

        cpy_data = json_dict["data"]
    
        cpy_data = cpy_data[0]

        for i in range(len(cpy_data)):
            cpy_data[i] = send_data[i]
            
    json_dict["data"] = [cpy_data] 

    #上書きした配列をjsonに書き直す
    with open('/home/pi/pi_test_betio/signal_12.json','w') as f:
        json.dump(json_dict,f)
    #赤外線コード生成
    encode(12)

    #赤外線コード送信
    send_infrared(12)


#GPIOsend = XX GPIOrec =XX
def cpy_json_18(send_data):
    with open('/home/pi/pi_test_betio/signal_18.json','r') as f:
        json_dict = json.load(f)

        cpy_data = json_dict["data"]
    
        cpy_data = cpy_data[0]

        for i in range(len(cpy_data)):
            cpy_data[i] = send_data[i]
            
    json_dict["data"] = [cpy_data] 

    #上書きした配列をjsonに書き直す
    with open('/home/pi/pi_test_betio/signal_18.json','w') as f:
        json.dump(json_dict,f)
    #赤外線コード生成
    encode(18)
    
    # time.sleep(0.2)
    send_infrared(18)
    #赤外線コード送信
    # for i in range(2):
    #     send_infrared(18)
    #     time.sleep(1)


#GPIOsend = XX GPIOrec =XX
def cpy_json_24(send_data):
    with open('/home/pi/pi_test_betio/signal_24.json','r') as f:
        json_dict = json.load(f)

        cpy_data = json_dict["data"]
    
        cpy_data = cpy_data[0]

        for i in range(len(cpy_data)):
            cpy_data[i] = send_data[i]
            
    json_dict["data"] = [cpy_data] 

    #上書きした配列をjsonに書き直す
    with open('/home/pi/pi_test_betio/signal_24.json','w') as f:
        json.dump(json_dict,f)
    #赤外線コード生成
    encode(24)

    #赤外線コード送信
    send_infrared(24)


###############################################






#####################受信#######################

#json配列の光データを編集して制御に送る

#24から来たデータに対しての自身の光る位置
def getjson_6():
    
    with open('/home/pi/pi_test_betio/signal_6.json','r') as f:

        json_dict = json.load(f)

        befo_data = json_dict["data"]

        befo_data = befo_data[0]

    #赤外線コード受信
    receive_infrared(6)

    #受け取った赤外線コードをjson化
    decode(6)

    with open('/home/pi/pi_test_betio/signal_6.json','r') as f:

        json_dict = json.load(f)

        get_data = json_dict["data"]

        get_data = get_data[0]

    rays = infrared_rays_receive()

    # if  cgir_6.REC_NO_DATA == 10:
    #     print("きた")
    match_count = 0
    for i in range(len(get_data)):
        if get_data[i] == befo_data[i]:
            match_count += 1
            if match_count == 37:
                return None
            
    count = 0
    for i in range(len(get_data)):
        if get_data[i] == 0:
            count+=1
            if (count == 37):
                return get_data
        
    
    if get_data[0] == 30:  #先頭配列が30は初期通信を行う 
        get_data[1] = 6
        return get_data

    #配列に0がある場合、その筐体が震源
    #配列の10番目が0の場合、角から来たデータではない
    elif get_data.count(0) == 1: 
        rays = rays.infrared_rays_receive_6_from24(get_data)
        print("入った１")
        for i in range(len(get_data)):
            if 1<=i<=9:
                get_data[i] = rays[i-1]
                get_data[0] = 0
            else:
                get_data[i]
                get_data[0] = 0

        get_data[0] = 0


        if get_data[10] == 0:
            get_data[10] = 77
        
        #print(get_data)
        return get_data
    
    
    else:
        rays = rays.infrared_rays_receive_6_from24(get_data)
        print("入った２")
        for i in range(len(get_data)):
            if 1<=i<=9:
                get_data[i] = rays[i-1]
            else:
                get_data[i]
        print(get_data)
        return get_data

    

    #return get_data

#18から来たデータに対しての自身の光る位置
def getjson_12():
    
    with open('/home/pi/pi_test_betio/signal_12.json','r') as f:

        json_dict = json.load(f)

        befo_data = json_dict["data"]

        befo_data = befo_data[0]

    #赤外線コード受信
    receive_infrared(12)

    #受け取った赤外線コードをjson化
    decode(12)

    with open('/home/pi/pi_test_betio/signal_12.json','r') as f:

        json_dict = json.load(f)

        get_data = json_dict["data"]

        get_data = get_data[0]
    
    rays = infrared_rays_receive()
    
    match_count = 0
    for i in range(len(get_data)):
        if get_data[i] == befo_data[i]:
            match_count += 1
            if match_count == 37:
                return 

    count = 0
    for i in range(len(get_data)):
        if get_data[i] == 0:
            count+=1
            if (count == 37):
                return get_data

    if get_data[0] == 30:  #先頭配列が30は初期通信を行う
        get_data[1] = 12
        return get_data

    elif get_data.count(0) == 1:  #配列に0がある場合、その筐体が震源
        rays = rays.infrared_rays_receive_12_from18(get_data)
        for i in range(len(get_data)):
            if 1<=i<=9:
                get_data[i] = rays[i-1]
                get_data[0] = 0
            else:
                get_data[i]
                get_data[0] = 0

        # get_data[0] = 0

        if get_data[10] == 0:
            get_data[10] = 77
        
        print("elifに入ったぞいいいいいいいい")
        return get_data
    
    else:
        rays = rays.infrared_rays_receive_12_from18(get_data)
        for i in range(len(get_data)):
            if 1<=i<=9:
                get_data[i] = rays[i-1]
            else:
                get_data[i]
        print("elseに入ってるよ")
        return get_data


    #return get_data


#12から来たデータに対しての自身の光る位置
def getjson_18():
    
    with open('/home/pi/pi_test_betio/signal_18.json','r') as f:

        json_dict = json.load(f)

        befo_data = json_dict["data"]

        befo_data = befo_data[0]

    #赤外線コード受信
    receive_infrared(18)

    #受け取った赤外線コードをjson化
    decode(18)

    with open('/home/pi/pi_test_betio/signal_18.json','r') as f:

        json_dict = json.load(f)

        get_data = json_dict["data"]

        get_data = get_data[0]
    
    rays = infrared_rays_receive()

    match_count = 0
    for i in range(len(get_data)):
        if get_data[i] == befo_data[i]:
            match_count += 1
            if match_count == 37:
                return None
            
    count = 0
    for i in range(len(get_data)):
        if get_data[i] == 0:
            count+=1
            if (count == 37):
                return get_data

    if get_data[0] == 30:  #先頭配列が30は初期通信を行う
        get_data[1] = 18
        return get_data

    elif get_data.count(0) == 1:  #配列に0がある場合、その筐体が震源
        rays = rays.infrared_rays_receive_18_from12(get_data)
        for i in range(len(get_data)):
            if 1<=i<=9:
                get_data[i] = rays[i-1]
                get_data[0] = 0
            else:
                get_data[i]
                get_data[0] = 0

        # get_data[0] = 0

        if get_data[10] == 0:
            get_data[10] = 77
        
        print(get_data)
        return get_data
    
    else:
        rays = rays.infrared_rays_receive_18_from12(get_data)
        for i in range(len(get_data)):
            if 1<=i<=9:
                get_data[i] = rays[i-1]
            else:
                get_data[i]
        print(get_data)
        return get_data


    #return get_data


#6から来たデータに対しての自身の光る位置
def getjson_24():
    
    with open('/home/pi/pi_test_betio/signal_24.json','r') as f:

        json_dict = json.load(f)

        befo_data = json_dict["data"]

        befo_data = befo_data[0]

    #赤外線コード受信
    receive_infrared(24)

    #受け取った赤外線コードをjson化
    decode(24)

    with open('/home/pi/pi_test_betio/signal_24.json','r') as f:

        json_dict = json.load(f)

        get_data = json_dict["data"]

        get_data = get_data[0]
    
    rays = infrared_rays_receive()

    match_count = 0
    for i in range(len(get_data)):
        if get_data[i] == befo_data[i]:
            match_count += 1
            if match_count == 37:
                return None

    count = 0
    for i in range(len(get_data)):
        if get_data[i] == 0:
            count+=1
            if (count == 37):
                return get_data

    if get_data[0] == 30:  #先頭配列が30は初期通信を行う
        get_data[1] = 24
        return get_data

    elif get_data.count(0) == 1:  #配列に0がある場合、その筐体が震源
        rays = rays.infrared_rays_receive_24_from6(get_data)
        for i in range(len(get_data)):
            if 1<=i<=9:
                get_data[i] = rays[i-1]
                get_data[0] = 0
            else:
                get_data[i]
                get_data[0] = 0

        # get_data[0] = 0

        if get_data[10] == 0:
            get_data[10] = 77
        
        print(get_data)
        print("配列に０が入ってたよおおおおおお！！！")
        return get_data
    
    else:
        rays = rays.infrared_rays_receive_24_from6(get_data)
        for i in range(len(get_data)):
            if 1<=i<=9:
                get_data[i] = rays[i-1]
            else:
                get_data[i]
        print(get_data)
        return get_data


    #return get_data


    
##############################################



class infrared_rays_receive:
    # def __init__(self):
    #     print("start")


    def infrared_rays_receive_18_from12(self,light_data):

        if light_data[1] != 0 and light_data[4] != 0 and light_data[7] != 0:
            data_1 = light_data[1]
            data_4 = light_data[4]
            data_7 = light_data[7]

            if data_1 == data_4 != data_7:
                new_light_data = [
                    data_7 + 2, data_7 + 1, data_7,
                    data_7 + 2, data_7 + 1, data_7,
                    data_7 + 2, data_7 + 1, data_7
                ]

            elif data_4 == data_7 != data_1:
                new_light_data = [
                    data_1 + 2, data_1 + 1, data_1,
                    data_1 + 2, data_1 + 1, data_1,
                    data_1 + 2, data_1 + 1, data_1
                ]

            elif data_1 == data_4 == data_7:
                new_light_data = [
                    data_7 + 3, data_7 + 2, data_7 + 1,
                    data_7 + 3, data_7 + 2, data_7 + 1,
                    data_7 + 3, data_7 + 2, data_7 + 1
                ]

            else:
                new_light_data = [
                    data_1, data_1, data_1,
                    data_4, data_4, data_4,
                    data_7, data_7, data_7
                ]
            # print(new_light_data)

        else:
            if light_data.index(0) == 1:
                new_light_data = [
                    3, 2, 1,
                    3, 2, 1,
                    3, 2, 2
                ]
            elif light_data.index(0) == 4:
                new_light_data = [
                    3, 2, 1,
                    3, 2, 1,
                    3, 2, 1
                ]
            elif light_data.index(0) == 7:
                new_light_data = [
                    3, 2, 2,
                    3, 2, 1,
                    3, 2, 1
                ]

        # print(12)
        # print(new_light_data)
        return new_light_data


    def infrared_rays_receive_24_from6(self,light_data):
        if light_data[1] != 0 and light_data[2] != 0 and light_data[3] != 0:
            data_1 = light_data[1]
            data_2 = light_data[2]
            data_3 = light_data[3]

            if data_1 == data_2 != data_3:
                new_light_data = [
                    data_3 + 2, data_3 + 2, data_3 + 2,
                    data_3 + 1, data_3 + 1, data_3 + 1,
                    data_3, data_3, data_3
                ]
                
                

            elif data_2 == data_3 != data_1:
                new_light_data = [
                    data_1 + 2, data_1 + 2, data_1 + 2,
                    data_1 + 1, data_1 + 1, data_1 + 1,
                    data_1, data_1, data_1
                ]
                

            elif data_1 == data_2 == data_3:
                new_light_data = [
                    data_3 + 3, data_3 + 3, data_3 + 3,
                    data_3 + 2, data_3 + 2, data_3 + 2,
                    data_3 + 1, data_3 + 1, data_3 + 1
                ]
                

            else:
                new_light_data = [
                    data_1, data_2, data_3,
                    data_1, data_2, data_3,
                    data_1, data_2, data_3
                ]
                

        else:
            if light_data.index(0) == 1:
                new_light_data = [
                    3, 3, 3,
                    2, 2, 2,
                    1, 1, 2
                ]
                print(new_light_data)
            elif light_data.index(0) == 2:
                new_light_data = [
                    3, 3, 3,
                    2, 2, 2,
                    1, 1, 1
                ]
                print(new_light_data)
            elif light_data.index(0) == 3:
                new_light_data = [
                    3, 3, 3,
                    2, 2, 2,
                    2, 1, 1
                ]
                print(new_light_data)

        # print(6)
        # print(new_light_data)
        return new_light_data


    def infrared_rays_receive_12_from18(self,light_data):
        if light_data[3] != 0 and light_data[6] != 0 and light_data[9] != 0:
            # data_3 = light_data[3]
            # data_6 = light_data[6]
            # data_9 = light_data[9]
            if light_data[3] == light_data[6] != light_data[9]:
                new_light_data = [
                    light_data[9], light_data[9] + 1, light_data[9] + 2,
                    light_data[9], light_data[9] + 1, light_data[9] + 2,
                    light_data[9], light_data[9] + 1, light_data[9] + 2
                ]

            elif light_data[6] == light_data[9] != light_data[3]:
                new_light_data = [
                    light_data[3], light_data[3] + 1, light_data[3] + 2,
                    light_data[3], light_data[3] + 1, light_data[3] + 2,
                    light_data[3], light_data[3] + 1, light_data[3] + 2
                ]

            elif light_data[3] == light_data[6] == light_data[9]:
                new_light_data = [
                    light_data[3] + 1, light_data[3] + 2, light_data[3] + 3,
                    light_data[3] + 1, light_data[3] + 2, light_data[3] + 3,
                    light_data[3] + 1, light_data[3] + 2, light_data[3] + 3
                ]

            else:
                new_light_data = [
                    light_data[3], light_data[6], light_data[9],
                    light_data[3], light_data[6], light_data[9],
                    light_data[3], light_data[6], light_data[9]
                ]
            # print(new_light_data)


        else:
            if light_data.index(0) == 3:
                new_light_data = [
                    1, 2, 3,
                    1, 2, 3,
                    2, 2, 3
                ]
            elif light_data.index(0) == 6:
                new_light_data = [
                    1, 2, 3,
                    1, 2, 3,
                    1, 2, 3
                ]
            elif light_data.index(0) == 9:
                new_light_data = [
                    2, 2, 3,
                    1, 2, 3,
                    1, 2, 3
                ]
        # print(18)
        # print(new_light_data)
        return new_light_data


    def infrared_rays_receive_6_from24(self,light_data):
        if light_data[7] != 0 and light_data[8] != 0 and light_data[9] != 0:
            data_7 = light_data[7]
            data_8 = light_data[8]
            data_9 = light_data[9]

            if data_7 == data_8 != data_9:
                new_light_data = [
                    data_9, data_9, data_9,
                    data_9 + 1, data_9 + 1, data_9 + 1,
                    data_9 + 2, data_9 + 2, data_9 + 2
                ]

            elif data_8 == data_9 != data_7:
                new_light_data = [
                    data_7, data_7, data_7,
                    data_7 + 1, data_7 + 1, data_7 + 1,
                    data_7 + 2, data_7 + 2, data_7 + 2
                ]

            elif data_7 == data_8 == data_9:
                new_light_data = [
                    data_9 + 1, data_9 + 1, data_9 + 1,
                    data_9 + 2, data_9 + 2, data_9 + 2,
                    data_9 + 3, data_9 + 3, data_9 + 3
                ]
            else:
                new_light_data = [
                    data_7, data_8, data_9,
                    data_7, data_8, data_9,
                    data_7, data_8, data_9
                ]

        else:
            if light_data.index(0) == 7:
                new_light_data = [
                    1, 1, 2,
                    2, 2, 2,
                    3, 3, 3
                ]
            elif light_data.index(0) == 8:
                new_light_data = [
                    1, 1, 1,
                    2, 2, 2,
                    3, 3, 3
                ]
            elif light_data.index(0) == 9:
                new_light_data = [
                    2, 1, 1,
                    2, 2, 2,
                    3, 3, 3
                ]

        # print(24)
        # print(new_light_data)
        return new_light_data


