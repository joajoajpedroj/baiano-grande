from pynput import keyboard
from pygame import mixer

mixer.init()
mixer.music.load("audio.mp3")

class Audio:
	def __init__(self, file):
		self.file = file
		
class Trigger:
	def __init__(self, stopKey = keyboard.Key.home, triggerKeys = ['down'], files = []):
		self.stopKey = stopKey
		self.triggerKeys = triggerKeys
		self.files = files
	
	def on_press(self, key):
		# Stop if stopKey is pressed
		if key == self.stopKey:
			return False
		# Get the key
		try:
			k = key.char
		except AttributeError:
			k = key.name
		# What to do if one of triggerKeys is pressed
		if k in self.triggerKeys:
			print("DEBUG: '{}' was pressed and will trigger the audio".format(k))
			

def main():
	Triggerer = Trigger()

	# Collect events until released
	with keyboard.Listener(
			on_press=Triggerer.on_press) as listener:
		listener.join()

if __name__ == "__main__":
	main()