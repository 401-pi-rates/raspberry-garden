import RPi.GPIO as GPIO
import requests

def button_callback_true(channel):
	#URL = "http://ec2-52-38-69-34.us-west-2.compute.amazonaws.com:80/api/v1/test"
	URL = "http://172.16.4.124:8000/api/v1/test"
	print("Button was pushed!")
	print(URL)
	DATA = {'has_moisture': True}
	r = requests.post(url = URL, data = DATA)
	print(r.text, DATA)

def button_callback_false(channel):
        #URL = "http://ec2-52-38-69-34.us-west-2.compute.amazonaws.com:80/api/v1/test"
        URL = "http://172.16.4.124:8000/api/v1/test"
        print("Button was pushed!")
        DATA = {'has_moisture': False}
        r = requests.post(url = URL, data = DATA)
        print(r.text, DATA)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(21,GPIO.RISING,callback=button_callback_true,bouncetime=1000)
GPIO.add_event_detect(20,GPIO.RISING,callback=button_callback_false,bouncetime=1000)

message = input("Press enter to quit\n\n")

GPIO.cleanup()
