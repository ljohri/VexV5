#VEX Cortex Python-Project
import vex
import sys

#region config
led_red = vex.DigitalOutput(12)
led_green = vex.DigitalOutput(11)
switch = vex.DigitalInput(3)
#endregion config

# Define a function for the first thread
def thread1():
    while True: # Flash the LED
        led_red.on()
        sys.sleep(3)
        led_red.off()
        sys.sleep(3)
       
# Define a function for the second thread
def thread2():
    while True: # LED is on with switch
        led_green.is_on(switch.is_on())
     
# Start both threads
sys.run_in_thread(thread1)
sys.run_in_thread(thread2)
# There could be additional code here running in the main thread