# WatchPuppy

Using WatchPuppy, you can easily turn your Raspberry Pi into a surveillance camera.

##Function
With WatchPuppy you can:
-Record H.264 video clips
-Clean up unneeded clips
-Real-time video streaming

##Hardware Requirements

-Raspberry Pi TypeB/B+/2 Type B
-Raspberry Pi CSI Camera Module (You **CANNOT** use a USB camera, as PiCamera Module, which is used by Watchdog, supports Raspberry Pi CSI Camera Module only.)

##Dependencies

-[PiCamera](https://pypi.python.org/pypi/picamera/) Module 
-VLC

##Usage
First, you should install VideoLan on your Raspberry Pi.
    sudo apt-get install vlc

Next, you should install PiCamera module. You can install via `apt`:
    sudo apt-get install picamera
You can install PiCamera via PIP as well.

Then you are ready to start the main program of WatchPuppy:
    python portal.py

##Configuration
###Change recording resolution
(TODO)
###Change streaming resolution
(TODO)
###Change clip length
(TODO)
###Change clip lifespan
(TODO)