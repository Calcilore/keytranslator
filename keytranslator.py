from pynput.keyboard import Key
from pynput.keyboard import Listener   as KBListener
from pynput.keyboard import Controller as KBController
from pynput.mouse    import Button
from pynput.mouse    import Controller as MSController

from ui import ui
from Translator import Translator

mouse         = MSController()
keyboard      = KBController()

class SettingsClass:
    running     = False
    debugging   = False
    controls    = []

settings = SettingsClass()

def debug(*txt):
    if (settings.debugging):
        print(*txt,end="")

def checkKey(key):
    try:
        keyC = key.char

        for i in range(len(settings.controls)):
            if settings.controls[i].fromKey == keyC:
                return i
    except:
        return -1

    return -1

def press(t):
    if (t.isPressed):
        return

    debug('press\n')

    if (t.toKey == "mouse"):
        mouse.press(Button.left)
    else:
        keyboard.press(t.toKey)

    t.isPressed = True

def release(t):
    if (not t.isPressed):
        return

    debug('release\n')

    if (t.toKey == "mouse"):
        mouse.release(Button.left)
    else:
        keyboard.release(t.toKey)

    t.isPressed = False

def on_press(key):
    if not settings.running:
        return

    i = checkKey(key)
    if (i != -1):
        press(settings.controls[i])

def on_release(key):
    if not settings.running:
        return

    i = checkKey(key)
    if (i != -1):
        release(settings.controls[i])


def main():
    # Start keyboad listener
    listener = KBListener(on_press=on_press, on_release=on_release)
    listener.start()

    settings.controls.append(Translator())
    settings.controls[0].fromKey = 'f'
    settings.controls[0].toKey = ' '
    settings.controls.append(Translator())
    settings.controls[1].fromKey = 'j'
    settings.controls[1].toKey = 'mouse'

    ui(settings)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
