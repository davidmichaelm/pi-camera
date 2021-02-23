from picamera import PiCamera
from time import sleep
# utilize gpio zero framework to interface gpio
# https://gpiozero.readthedocs.io
from gpiozero import LED, Button
# utilize signal framework
from signal import pause
import datetime

camera = PiCamera()

def take_picture():
    camera.start_preview()
    sleep(2)
    camera.capture('/home/pi/Desktop/' + datetime.datetime.now().strftime('%c') + '.jpg')
    camera.stop_preview()

button = Button(5)
button.when_pressed = take_picture

pause()