#python3!
#CCTV Bean Sentry Surveillance system
#Nov 21, 2020
#192.168.0.37
#TODO: server instead of VLC

import picamera
import time
import socket

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 24
camera.rotation = 90

server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(0)

#accept a single connection and create a makefile object
connection = server_socket.accept()[0].makefile('wb')

try:
    camera.start_recording(connection, format='h264')
    camera.wait_recording(60)
    camera.stop_recording()
finally:
    connection.close()
    server_socket.close()

"""
#preview that is semi-transparent to view program output
camera.start_preview(alpha=200)
#need to sleep at least for 2s before taking an image to sense light levels
camera.start_recording('/home/pi/Desktop/video.h264')
sleep(10)
#camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_recording()
camera.stop_preview()
"""