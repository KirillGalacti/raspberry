import smbus
from time import sleep

i2c = smbus.SMBus(1)
SLAVE_ADD_1 = 0x08 # Arduino I2C address
SLAVE_ADD_2 = 0x09 # Arduino I2C address
SLAVE_ADD_3 = 0x0a # Arduino I2C address

def beep(times, delay):
  for x in range(times):
    BUZZER.on()
    sleep(delay)
    BUZZER.off()
    sleep(delay)

def writeI2C(data):
  i2c.write_byte(SLAVE_ADD_1, data)
  i2c.write_byte(SLAVE_ADD_2, data)
  i2c.write_byte(SLAVE_ADD_3, data)

def readI2C():
  inData_1 = i2c.read_byte(SLAVE_ADD_1)
  return inData_1
  inData_2 = i2c.read_byte(SLAVE_ADD_2)
  return inData_2
  inData_3 = i2c.read_byte(SLAVE_ADD_3)
  return inData_3

prevI2CData = 0
beep(2, 0.07)

try:
  while True:
    if SW1.is_pressed:
      writeI2C(1)
      SW1.wait_for_release()

    elif SW2.is_pressed:
      writeI2C(2)
      SW2.wait_for_release()

    elif SW3.is_pressed:
      writeI2C(3)
      SW3.wait_for_release()

      sleep(0.1)