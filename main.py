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

class Scanner:
    def __init__(self, URL=0):
        self.Frame = []
        self.status = False
        self.isstop = False

        self.capture = picamera.PiCamera()
        time.sleep(2)
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

def clock():
    # clock
    lcd = CharLCD('PCF8574', address=0x27, port=1, backlight_enabled=True)
    lcd.clear()

    while True:
        lcd.cursor_pos = (0, 0)
        lcd.write_string("Date: {}".format(time.strftime("%Y/%m/%d")))
        lcd.cursor_pos = (1, 0)
        lcd.write_string("Time: {}".format(time.strftime("%H:%M:%S")))
        time.sleep(1)

def playmusic(mp3file):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3file)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() == True:
        pass

def detect(photo):
    client=boto3.client('rekognition')

    with open(photo, 'rb') as image:
        response = client.detect_faces(Image={'Bytes': image.read()},Attributes=['ALL'])

    print('Detected faces for ' + photo)    
    for faceDetail in response['FaceDetails']:
        awake = faceDetail['EyesOpen']['Value']
        print(photo + "awake? " + str(awake))
    return awake

def checkawake(s, t):
    newphoto = 'photos/photo_face' + str(t) + '.png'
    s.get_photo(newphoto)
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

    # set motor
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)

    stdscr = curses.initscr()
    stdscr.clear()

    # t = threading.Thread(target = clock)
    # t.start()
    
    print(SETHOUR, SETMINUTE)
    do = True
    while do:
        dt = list(time.localtime()) 
        hour = dt[3] 
        minute = dt[4] 
        if hour == SETHOUR and minute == SETMINUTE:
            # playmusic
            print("start to play music")
            pygame.mixer.init()
            pygame.mixer.music.load("../testMusic.mp3")
            pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.play()
            
            # motor
            print("motor start")
            GPIO.output(17, False)
            GPIO.output(18, True)
            GPIO.output(22, False)
            GPIO.output(23, True)
            time.sleep(5)
            print("motor stop")
            curses.endwin()
            GPIO.output(17, False)
            GPIO.output(18, False)
            GPIO.output(22, False)
            GPIO.output(23, False)

            # face detect
            print("face detecting")
            awaketimes = [False, False]
            s = Scanner()
            for i in range(10):
                awaketimes.append(checkawake(s, i))
                if awaketimes.count(True) > len(awaketimes)/2:
                    pygame.mixer.music.stop()
                    print("You are finally awake")
                    do = False
                    break
            print(awaketimes)

        
