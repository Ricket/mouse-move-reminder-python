import mouse
import time
import win32gui, win32process, psutil
from pathlib import Path
import os

curr_dir = Path(__file__).parent

# Put ffmpeg into path so that pydub picks it up
ffmpeg_bin = curr_dir.joinpath('ffmpeg-2022-02-17-git-2812508086-full_build/bin')
os.environ['PATH'] = str(ffmpeg_bin) + ';' + os.environ['PATH']

from pydub import AudioSegment
from pydub.playback import play

idle_warning_sound_path = curr_dir.joinpath('sfx/NaviHeyListen.mp3')
idle_warning_sound = AudioSegment.from_mp3(str(idle_warning_sound_path))

def do_idle_warning():
    print('warning, idle for too long!')
    play(idle_warning_sound)
    # stop timer

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
        

#mouse.hook(mouseHandler)

#time.sleep(120)

do_idle_warning()
