import sys

try: 
  import RPi.GPIO as GPIO
  sys.path.append('/home/pi/web') 
  from time import sleep
  import switchers as switchers
  import logger as logger

  signalPin = 26
  w1 = 22
  w2 = 23
  w3 = 24
  w4 = 25
  callbackPin = 27 
  sleepTime = 0.1

  GPIO.setmode(GPIO.BCM)
  GPIO.setup(signalPin, GPIO.OUT)
  GPIO.setup(w1, GPIO.IN)
  GPIO.setup(w2, GPIO.IN)
  GPIO.setup(w3, GPIO.IN)
  GPIO.setup(w4, GPIO.IN)
  GPIO.setup(callbackPin, GPIO.IN)

  def signalReceived(channel):
    if GPIO.input(w2) == GPIO.LOW:
      print('w2')
      if GPIO.input(w1) == GPIO.LOW:
        sleep(sleepTime)        
        switchers.switchOn(2)
        GPIO.output(signalPin,1)
        print('on')        
      else:
        sleep(sleepTime)
        GPIO.output(signalPin,0)
        switchers.switchOff(2)
        print('off')
 
  print('start')

  GPIO.remove_event_detect(27)
  GPIO.add_event_detect(27, GPIO.RISING, callback=signalReceived)

  GPIO.output(signalPin,0)
  while True:
    sleep(30)
except:
  print("Unexpected error:", sys.exc_info()[0])
  logger.log(sys.exc_info()[0], '/home/pi/common/temperature/logWireless')
