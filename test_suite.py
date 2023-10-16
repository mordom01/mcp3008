import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

#using physical pin 11 to blink an LED
GPIO.setmode(GPIO.BOARD)
chan_list = [11]
GPIO.setup(chan_list, GPIO.OUT)
#Following commands control the state of the output
#pin = 11


# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
# get reading from adc 
# mcp.read_adc(adc_channel)

while True: 
    for i in range(5):
        GPIO.output(11, GPIO.HIGH)
        time.sleep(0.25)
        GPIO.output(11, GPIO.LOW)
        time.sleep(0.25)
    for i in range(50):
        print(mcp.read_adc(0))
        if(mcp.read_adc(0) > 500): #light sensor
            print("light")
        else:
            print("dark")
        time.sleep(0.1)
    for i in range(4):
        GPIO.output(11, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(11, GPIO.LOW)
        time.sleep(0.1)
    for i in range(50):
        print(mcp.read_adc(1))
        if(mcp.read_adc(1) > 500): #sound sensor
            #print("clap")
            GPIO.output(11, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(11, GPIO.LOW)
            #time.sleep(0.1)
        else:
            print("dark")
            time.sleep(0.1)