from pynput import keyboard
from pygame import mixer
import json

class Audio:
	def __init__(self, file):
		self.file = file
		self.audio = mixer.Sound(file=file)

class Trigger:
	def __init__(self, audios, stopKey = keyboard.Key.home, triggerKeys = ['down']):
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
		if key == self.stopKey:
			print("stopKey ('{}') was pressed and the program will stop.".format(k))
			return False
		# What to do if one of triggerKeys is pressed
		if k in self.triggerKeys:
			print("DEBUG: '{}' was pressed and will trigger the audio.".format(k))
			self.audios[0].audio.play()
			

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
		LoadedAudio = Audio(i["path"])
		audios.append(LoadedAudio)

	Triggerer = Trigger(audios=audios)

	# Collect events until released
	with keyboard.Listener(
			on_press=Triggerer.on_press) as listener:
		listener.join()

if __name__ == "__main__":
	main()