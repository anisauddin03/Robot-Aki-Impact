from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
sleep(5)
camera.stop_preview()

# link to the github of opencv camera and raspberry pi
# https://github.com/2lambda123/Face-Recognition-using-RaspberryPi/blob/3c60fdea32caafbe129400f6a202609ec3ab24c1/facial_recognition_mrinal/Face-Recognition-using-Raspberry-Pi-master/README.md?plain=1
# commands in terminal to go into virtual enviroment of cv
# $ source ~/.profile
# $ workon cv

