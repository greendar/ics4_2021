from machine import Pin
import utime


greenLED = Pin(16, Pin.OUT)
redLED = Pin(17, Pin.OUT)
trigger = Pin(18, Pin.OUT)
echo = Pin(19, Pin.IN)

def ultra():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   if distance < 15:
       redLED.low()
       greenLED.high()
   else:
       greenLED.low()
       redLED.low()
   print("The distance from object is ",distance,"cm")

while True:
   ultra()
   utime.sleep(1)
