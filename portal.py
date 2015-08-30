# Watchdog Main Program
import io
import time
import picamera
import subprocess
import threading
from daemon import *

def generate_fname():
    return time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())) + '.h264'

lifeSpan = 1

daemonProcess = threading.Thread(target=lambda:daemon(lifeSpan))
daemonProcess.setDaemon(True)
daemonProcess.start()

camera = picamera.PiCamera()
camera.resolution = (1280, 720)
camera.framerate = 24

print('Watchdog started at ' + time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())))

vlcProcess = subprocess.Popen(['cvlc', '-vvv', 'stream:///dev/stdin', '--sout', '#standard{access=http,mux=ts,dst=:8090}', ":demux=h264"],stdin=subprocess.PIPE)
stream = vlcProcess.stdin

camera.start_recording(stream, format='h264', resize=(640, 360))

while(True):
    camera.start_recording(generate_fname(), splitter_port=2)
    camera.wait_recording(60)
    camera.stop_recording(splitter_port=2)
