import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7,gpio.OUT)
    gpio.setup(11,gpio.OUT)
    gpio.setup(13,gpio.OUT)
    gpio.setup(15,gpio.OUT)

init()

def forward():

    gpio.output(7,0)
    gpio.output(11,1)
    gpio.output(13,0)
    gpio.output(15,1)

