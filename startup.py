'''
3V3 3V3 3.3V power
GND GND Ground
CLK P11/P_SCLK SPI clock input
DIN P10/P_MOSI SPI data input
CS P8/P_CE0 Chip select, Low active
DC P25 Data/Command select
RST P27 Reset
BL P24 Back light
KEY1 P21 Button 1GPIO
KEY2 P20 Button 2GPIO
KEY3 P16 Button 3GPIO
Joystick Up P6 Joystick up
Joystick Down P19 Joystick down
Joystick Left P5 Joystick left
Joystick Right P26 Joystick right
Joystick Press P13 Joystick press
'''

from sys import platform

if platform == 'win32':
    print('you on windows')
    from EmulatorGUI import GPIO
    GPIO.setmode(GPIO.BCM)
else:
    print('fsa')
    import RPi.GPIO as GPIO # pylint: disable=import-error
    GPIO.setmode(GPIO.BOARD)

input_schema = {
    'key1': 21,
    'key2': 20,
    'key3': 16,
    'up': 6,
    'down': 19,
    'left': 5,
    'right': 26,
    'press': 13
}

# Joystick press
#GPIO.setup(13, GPIO.IN)
for key, value in input_schema.items():
    GPIO.setup(value, GPIO.IN)

while True:
    for key, value in input_schema.items():
        if GPIO.input(value):
            print(key)
    #if GPIO.input(13):
    #    print('u r pressing joystick down')