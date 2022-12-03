from tkinter import *
import RPi.GPIO as GPIO
import time

B1 = 26
B2 = 19
B3 = 13
B4 = 6

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(B1, GPIO.IN)
GPIO.setup(B2, GPIO.IN)
GPIO.setup(B3, GPIO.IN)
GPIO.setup(B4, GPIO.IN)


 