import RPi.GPIO as GPIO
from time import sleep

import webbrowser
import time


count=0

PIR_input1=29
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR_input1,GPIO.IN)


PIR_input2=36
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR_input2,GPIO.IN)

import datetime

while True:
    if(GPIO.input(PIR_input1)):
        print("user detected")
        count=count+2
               
    if(GPIO.input(PIR_input2)):
        print("user exited")
        count=count-1
    
    print("No. of people in the COMPLEX="+str(count))
    time= datetime.datetime.now()
    value="No. of people in the COMPLEX at "+str(time.strftime("%H:%M:%S"))+"="+str(count)
    
    html_content=f"<html><head> </head> <body> {value} <br></body> </html>"

    with open("covid.html","a") as html_file:
        html_file.write(html_content)
        print("done")

    sleep(10)
    
