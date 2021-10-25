from pynput import keyboard
from pygame import mixer
from random import random
import json

class Audio:
	def __init__(self, file, chance):
		self.file = file
		self.audio = mixer.Sound(file=file)
		
		self.chance = chance/100

	def play(self):
		self.audio.play()

class Trigger:
	def __init__(self, audios, stopKey = 'home', triggerKeys = ['down']):
		self.stopKey = stopKey
		self.triggerKeys = triggerKeys
		self.audios = audios
	
	def on_press(self, key):
		# Get the key
		try:
			k = key.char
		except AttributeError:
			k = key.name
		# Stop if stopKey is pressed
		if k == self.stopKey:
			print("stopKey ('{}') was pressed and the program will stop.".format(k))
			return False
		# What to do if one of triggerKeys is pressed
		if k in self.triggerKeys:
			print("DEBUG: '{}' was pressed.".format(k))
			self.select_audio()

	def select_audio(self):
		nRandom = random()
		c = 0
		for i in self.audios:
			if c < nRandom < (c + i.chance):
				print("DEBUG: audio {} will be played!".format(i.file))
				i.play()
				pass
			c += i.chance

def main():
	mixer.init()
	# Read file
	with open("settings.json", "r") as read_file:
		# Parse it
		data = json.load(read_file)
	
	# List to be filled with Audio objects
	audios = []
	# Iterate on data from file
	for i in data["audios"]:
		LoadedAudio = Audio(i["path"], i["chance"])
		audios.append(LoadedAudio)

	Triggerer = Trigger(audios=audios, stopKey=data["stopKey"], triggerKeys=data["triggerKeys"])

	# Collect events until released
	with keyboard.Listener(
			on_press=Triggerer.on_press) as listener:
		listener.join()

if __name__ == "__main__":
	main()