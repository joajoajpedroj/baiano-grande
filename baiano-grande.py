from pynput import keyboard
from pygame import mixer

mixer.init()
mixer.music.load("audio.mp3")

def on_press(key):
    if key == keyboard.Key.home:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in ['1', '2', 'left', 'right']:  # keys of interest
        mixer.music.play()
        # self.keys.append(k)  # store it in global-like variable
        print('Key pressed: ' + k)
        #return False  # stop listener; remove this if want more keys

# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()