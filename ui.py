
from Translator import Translator

def status(settings):
    controls = ''
    for control in settings.controls:
        controls += '[' + control.fromKey + ', ' + control.toKey + ']'

    print(f"""Running: {settings.running}
debug: {settings.debugging}
controls: {controls}
""")

def running(settings):
    settings.running = not settings.running
    print(f"running changed to: {settings.running}")

def debug(settings):
    settings.debugging = True
    input("press enter to stop debugging\n")
    settings.debugging = False

def controlsSelection(q):
    out = ''
    while out != "mouse" and out != "exit" and len(out) != 1:
        out = input(q)

    return out

def controls(settings):
    settings.controls = []

    i = 0
    while True:
        settings.controls.append(Translator())

        settings.controls[i].fromKey = controlsSelection(f"type the key you want to set as input key {i + 1}, or type exit to exit\n> ")
        if (settings.controls[i].fromKey.lower() == 'exit'):
            settings.controls.pop()
            break

        settings.controls[i].toKey = controlsSelection(f"type the key you want to set as output key {i + 1}\n> ")
 
        i += 1

def ui(settings):
    print("Key Translator v1\n")
    status(settings)

    while True:
        inp = input("> ").lower()

        if inp == "help":
            print("type the value you want to change to change them\n")
            status(settings)
        elif inp == "exit":
            exit()
        elif inp == "status":
            status(settings)
        elif inp == "running":
            running(settings)
        elif inp == "debug":
            debug(settings)
        elif inp == "controls":
            controls(settings)
