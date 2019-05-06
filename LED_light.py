Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 

from gpiozero import LED, Button
from gpiozero import Buzzer
from time import sleep

led = LED(4)
light_button = Button(21)
buzzer_button = Button(13)
buzzer = Buzzer(17)


while True:
    if light_button.is_pressed:
        led.on()
    elif buzzer_button.is_pressed:
        for i in range(5):
            led.on()
            sleep(.5)
            led.off()
            sleep(.5)
            buzzer.on()
            sleep(.5)
            buzzer.off()
        
    else:
        led.off()
        buzzer.off()
