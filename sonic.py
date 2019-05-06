Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
from ptprotoplus import sensors, psonic
from time import sleep
from gpiozero import Button

sensor = sensors.DistanceSensor()
button = Button(26)
pitch_button = Button(21)
distance = sensor.get_distance()

while True:
    if button.is_pressed:
        note = 40 + distance
        psonic.play(note)
    elif pitch_button.is_pressed:
        p_note = 60 + distance
        psonic.play(p_note)
    
