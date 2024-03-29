import boto3
import json
import picamera
import time
import threading
import sys
import pygame
import argparse
import smbus2
sys.modules['smbus'] = smbus2
from RPLCD.i2c import CharLCD
import RPi.GPIO as GPIO
import curses
from curses import wrapper
from requests import get
import json

client=boto3.client('rekognition')

class Scanner:
    def __init__(self, URL=0):
        self.Frame = []
        self.status = False
        self.isstop = False

        self.capture = picamera.PiCamera()
        time.sleep(1)
        self.start()

    def start(self):
        print("ipcom started!!")

    def stop(self):
        self.isstop = True
        print("ipcom stopped!!")

    def __exit__(self, exc_type, exc_value, traceback):
        self.stop()

    def get_photo(self, filename):
        self.capture.capture(filename)

def playmusic(mp3file):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3file)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() == True:
        pass

def detect(photo):
    print("Detect...")
    with open(photo, 'rb') as image:
        response = client.detect_faces(Image={'Bytes': image.read()},Attributes=['ALL'])
    
    print('Detected faces for ' + photo)    
    if len(response['FaceDetails']) == 0:
        awake = False
    for faceDetail in response['FaceDetails']:
        awake = faceDetail['EyesOpen']['Value']
        print(photo)
        print("awake? " + str(awake))
    return awake

def checkawake(s, t):
    newphoto = 'photos/photo_face' + str(t) + '.jpg'
    s.start()
    s.get_photo(newphoto)
    s.stop()
    print('took photo: ' + newphoto)
    isawake = detect(newphoto)
    return isawake

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--hour', type=int)
    parser.add_argument('--minute', type=int)
    opts = parser.parse_args()

    SETHOUR = opts.hour
    SETMINUTE = opts.minute

    if (SETHOUR == None) or (SETMINUTE == None):
        firebase_url = "https://annoying-clock.firebaseio.com/.json"
        Data = get(firebase_url).json()['alarm']
        SETHOUR = Data['alarm1']['hour']
        SETMINUTE = Data['alarm1']['minute']
    
    print("Alarm Time: ", SETHOUR, SETMINUTE)

    # t = threading.Thread(target = clock)
    # t.start()
    print("Start!!!!!!!!")
    s = Scanner()
    do = True
    while do:
        dt = list(time.localtime()) 
        hour = dt[3] 
        minute = dt[4]
        # time.sleep(1)
        if hour == SETHOUR and minute == SETMINUTE:
            # playmusic
            print("Time to get up!!!!!!!!")
            print("start to play music")
            pygame.mixer.init()
            pygame.mixer.music.load("../testMusic2.mp3")
            pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.play()
            
            # set motor
            # GPIO.cleanup()
            GPIO.setmode(GPIO.BCM)

            GPIO.setup(17, GPIO.OUT)
            GPIO.setup(18, GPIO.OUT)
            GPIO.setup(22, GPIO.OUT)
            GPIO.setup(23, GPIO.OUT)

            # motor
            print("Motor start")
            GPIO.output(17, False)
            GPIO.output(18, True)
            GPIO.output(22, False)
            GPIO.output(23, True)
            time.sleep(5)
            print("Motor stop")
            # curses.endwin()
            GPIO.output(17, False)
            GPIO.output(18, False)
            GPIO.output(22, False)
            GPIO.output(23, False)
            GPIO.cleanup()

            # face detect
            print("Face awake detecting...")
            awaketimes = [False]

            for i in range(10):
                awaketimes.append(checkawake(s, i))
                if awaketimes.count(True) > len(awaketimes)/2:
                    pygame.mixer.music.stop()
                    print("You are finally awake!!!")
                    do = False
                    break
            print(awaketimes)
            SETMINUTE += 5
            if (SETMINUTE >= 60):
                SETHOUR += 1
                SETMINUTE -= 60
                if (SETHOUR >= 24):
                    SETHOUR -= 24

        
