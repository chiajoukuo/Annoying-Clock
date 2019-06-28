import time 
import sys 
import pygame
import argparse

# soundFile = 'sound.wav' 
# not_executed = 1 
# def soundStart(): 
# if sys.platform[:5] == 'linux': 
# import os 
# os.popen2('aplay -q'   soundFile) 
# else: 
# import winsound 
# winsound.PlaySound(soundFile, winsound.SND_FILENAME) 
# while(not_executed): 

# soundStart() 
# not_executed = 0 

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--hour', type=int)
	parser.add_argument('--minute', type=int)
	opts = parser.parse_args()

	SETHOUR = opts.hour
	SETMINUTE = opts.minute

	while True:
		dt = list(time.localtime()) 
		hour = dt[3] 
		minute = dt[4] 
		if hour == SETHOUR and minute == SETMINUTE: # 下午5點33分的時候開始提示 
			pygame.mixer.init()
			pygame.mixer.music.load("testMusic.mp3")
			pygame.mixer.music.set_volume(1.0)
			pygame.mixer.music.play()

			while pygame.mixer.music.get_busy() == True:
				pass