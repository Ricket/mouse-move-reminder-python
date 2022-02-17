import mouse
import time

def mouseHandler(event):
    if isinstance(event, mouse.MoveEvent):
        print(event)

mouse.hook(mouseHandler)

time.sleep(120)
