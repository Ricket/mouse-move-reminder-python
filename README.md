mouse-move-reminder-python
===

When RuneScape is running and you haven't moved your mouse for nearly 5 minutes, play an annoying sound.

# Installation

Download ffmpeg: https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z

Extract it into this folder. Update the variable `ffmpeg_bin` at top of main.py to point to the bin subfolder.

Install Python dependencies:

(TODO confirm if simpleaudio is needed)

```
pip install mouse pywin32 psutil simpleaudio pydub
```