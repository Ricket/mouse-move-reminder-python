import mouse
import time
import win32gui, win32process, psutil

def active_window_process_name():
    try:
        pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
        return(psutil.Process(pid[-1]).name())
    except:
        pass

def is_runescape_active():
    active_process = active_window_process_name()
    return active_process == 'rs2client.exe'

def mouseHandler(event):
    if isinstance(event, mouse.MoveEvent):
        if not is_runescape_active():
            return
        print('TODO reset timer')
        

mouse.hook(mouseHandler)

time.sleep(120)
