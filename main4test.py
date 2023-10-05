import requests
import tago
import credentials
import time
import raspFunctions
from picamera import PiCamera
import serial
import os
import RPi.GPIO as GPIO

# Configurar o pino GPIO 21 para entrada
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)
GPIO.setup(20, GPIO.OUT)

def checkInternetRequests(url='http://www.google.com/', timeout=3):
    try:
        # Check if internet connection is available by sending a HEAD request to Google
        r = requests.head(url, timeout=timeout)
        return True
    except requests.ConnectionError as ex:
        print(ex)
        return False

# Variables to start the code and personalize all things
xCut = [0, 256]
yCut = [0, 256]
timeToStart = 0
timeToMeasure = 2

time.sleep(timeToStart)
point = "alpha"
shouldStop = True

while checkInternetRequests() == False:  # Wait for internet connection
    time.sleep(timeToMeasure)

# Tago.io setup
client = tago.Device(credentials.tagoToken)
filename = '/home/pi/v2_prototype/number.txt'
GPIO.output(20, GPIO.LOW)

i = 0
while i <= 0:
    if GPIO.input(21) == False:
        #raspFunctions.updateModelFCN()
        with open(filename, 'r') as file:
            number = int(file.read())

        number += 1

        with open(filename, 'w') as file:
            file.write(str(number))
            battery = 100-((number*100)/1600)

            print('A')
    else:
        with open(filename, 'w') as file:
            file.write(str(0))
            battery = 100-((0*100)/1600)
            print('B')

    data = {
        'variable': 'bateria',
        'value': str(battery),
        'unit': '%'
    }

    client.insert(data)

    raspFunctions.obtainTemperature(client)
    camera = PiCamera()
    raspFunctions.runModelFCN(client, camera, xCut, yCut, point)
    camera.close()
    GPIO.output(20, GPIO.HIGH)
    time.sleep(1)

    i = i + 1

#os.system('sudo shutdown -h now')
GPIO.cleanup()
