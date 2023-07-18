# gui-dlp

This is a GUI front-end application for yt-dlp. You must already 
have yt-dlp (and its dependencies, such as ffmepg) installed and in 
the system PATH Environment. (Settings > System > About > Advanced 
System Settings > Advanced tab > Environment Variables > Double-
click "Path" under System Variables > make a new path to the folder 
where you placed yt-dlp (and do the same for ffmpeg, if you haven't 
already after downloading yt-dlp)).

This presently does not have all of the features available in the 
terminal, so I wouldn't recommend using it if you need more 
technically specific options.

You can run it as a python script just fine, or if you want to 
convert this into a Windows executable, I would recommend the tool 
auto-py-to-exe (https://pypi.org/project/auto-py-to-exe/), or just
use one of my releases.

It runs in both Windows and Linux (macOS as of yet untested).
For Linux users, you may have to install "Tk" (Tkinter module for Python)
before running the python3 script. A couple of features do not work
exactly as intended in Linux (terminal window not showing with download
progress), but core functionality still operates smoothly.

--------------------------------------------------------------------

This is by no means "clean" code, and I am by no means an expert, 
so don't expect this to be highly optimized.
To quote some guy, "I have no idea what I'm doing." 
