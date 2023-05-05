#authors: Nathan Hughes, Devansh Sharma, and Sebastian Vera
import RPi.GPIO as GPIO
import time
import datetime
import requests

headers = {"Content-Type": "application/json"}

piID = "pi0"
#GPIO pin that sensor is connected to
sensorID0 = "26"
sensorID1 = "16"

GPIO.setwarnings(False)
# Set up GPIO mode and pin, BCM stands for Broadcom SOC channel
GPIO.setmode(GPIO.BCM)
#utilizing raspi built in resistor on gpio pin 26
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT)
buzzer = GPIO.PWM(17, 1000)
# Loop to read state of reed switch
try:
  previous_stateS1 = None
  previous_stateS2 = None

  while True:
    current_stateS1 = GPIO.input(26)
    current_stateS2 = GPIO.input(16)
    if current_stateS1 != previous_stateS1:
    #check whitespace
      time_stamp = str(datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
      if current_stateS1 == False:
        print('door 1 is closed '+str(datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")))
        #TODO
        status = '{"status": "Closed", "timestamp": "' + time_stamp + '"}'
        print(status)
        requests.put('http://34.94.122.160:8080/api/v1/sensors/Pi0/Sen0', data=status, headers=headers)
        time.sleep(.5)
      else:
        print('door 1 is open '+str(datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")))
        #TODO
        status = '{"status": "Open", "timestamp": "' + time_stamp + '"}'
        print(status)
        requests.put('http://34.94.122.160:8080/api/v1/sensors/Pi0/Sen0', data=status, headers=headers)
        buzzer.start(10)
        time.sleep(.5)
        buzzer.stop()
      previous_stateS1 = current_stateS1

    if current_stateS2 != previous_stateS2:
    #check whitespace
      time_stamp = str(datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
      if current_stateS2 == False:
        print('door 2 is closed '+str(datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")))
        #TODO
        status = '{"status": "Closed", "timestamp": "' + time_stamp + '"}'
        print(status)
        requests.put('http://34.94.122.160:8080/api/v1/sensors/Pi0/Sen1', data=status, headers=headers)
        time.sleep(.5)
      else:
        print('door 2 is open '+str(datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")))
        #TODO
        status = '{"status": "Open", "timestamp": "' + time_stamp + '"}'
        print(status)
        requests.put('http://34.94.122.160:8080/api/v1/sensors/Pi0/Sen1', data=status, headers=headers)
        buzzer.start(10)
        time.sleep(.5)
        buzzer.stop()
      previous_stateS2 = current_stateS2

except KeyboardInterrupt:
    print("\nclean and exit program ")
    GPIO.cleanup()