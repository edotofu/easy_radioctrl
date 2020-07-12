# coding: UTF-8
import RPi.GPIO as GPIO
import requests
import time


# 駆動用モータ（左）
GPIO_LEFT  = 23
# 駆動用モータ（右）
GPIO_RIGHT = 24


GPIO.setmode(GPIO.BCM) 
# GPIO23を利用
GPIO.setup(GPIO_LEFT,GPIO.OUT)
# GPIO24を利用
GPIO.setup(GPIO_RIGHT,GPIO.OUT)

if __name__ == '__main__':
    try:

        while True:

            get_response = ""
            get_response = requests.get("http://localhost:5000/getcommand")
            get_response_text = get_response.text
            # print(get_response_text)

            if get_response_text == "Strate":
                GPIO.output(GPIO_RIGHT,True)   
                GPIO.output(GPIO_LEFT,True) 
                time.sleep(0.5)
                GPIO.output(GPIO_RIGHT,False)   
                GPIO.output(GPIO_LEFT,False) 
            if get_response_text == "Left":
                GPIO.output(GPIO_RIGHT,False)   
                GPIO.output(GPIO_LEFT,True) 
                time.sleep(0.2)
                GPIO.output(GPIO_RIGHT,False)   
                GPIO.output(GPIO_LEFT,False) 
            if get_response_text == "Right":
                GPIO.output(GPIO_RIGHT,True)   
                GPIO.output(GPIO_LEFT,False) 
                time.sleep(0.2)
                GPIO.output(GPIO_RIGHT,False)   
                GPIO.output(GPIO_LEFT,False) 
            if get_response_text == "Stop":
                GPIO.output(GPIO_RIGHT,False)   
                GPIO.output(GPIO_LEFT,False) 


            # 前進
            #GPIO.output(GPIO_LEFT,True)
            #GPIO.output(GPIO_RIGHT,True)
            #time.sleep(1)

            # Lチカ停止
            #GPIO.output(GPIO_LEFT,True)
            #GPIO.output(GPIO_RIGHT,False)
            #time.sleep(2.0)

        # TODO:Excption処理

        # GPIOクリア
        GPIO.cleanup()


    except Exception as e:
        print("例外args:", e.args)
        print("Measurement stopped by User")
        # 駆動用モータ停止
        GPIO.output(GPIO_RIGHT,False)
        GPIO.output(GPIO_LEFT,False)   
        # GPIOクリア               
        GPIO.cleanup()

