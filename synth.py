from ptprotoplus import adc, psonic
from gpiozero import Button
from time import sleep

adc = adc.ADCProbe()
button = Button(21)

while True:
    if button.is_pressed:
        print(adc.read_value(0))
        note = adc.read_value(0)
        psonic.play(60)
        sleep(0.5)