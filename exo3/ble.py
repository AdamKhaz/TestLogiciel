import platform
import time
import _bleio
import random

from adafruit_ble import BLERadio
from adafruit_ble.services.nordic import UARTService

if platform.system() == 'Darwin':
    addr = _bleio.Address(string="35AAF6EA-6FF0-EDDF-76BB-5D5F6F818760")
elif platform.system() == 'Windows':
    addr = _bleio.Address(string="ce:bf:e4:0c:07:6a")

ble = BLERadio()
print("Scanning...")
while True:
    ble.connect(addr)
    if ble.connected:
        print("Connected")
        print("Commands: 'S' to stop, 'G' to go, 'C' to calibrate")
        print("'Kp <value>' to set Kp, 'Ki <value>' to set Ki, 'Kd <value>' to set Kd")
        print("'M <value>' to set max speed, 'm <value>' to set min speed")
        print("'B <value>' to set base speed")
    while ble.connected:
        user_input = input("Enter a command: ")
        if len(user_input) >= 1:
            cmd = user_input[0]
            if cmd in ['S', 'G', 'C']:
                buffer = cmd.encode('utf-8')
                print(buffer)
                ble.connections[0][UARTService].write(buffer)
                time.sleep(1)
            elif len(user_input) >= 3:
                print(user_input[0:2])
                if user_input[0:2] in ['Kp', 'Ki', 'Kd']:
                    value = float(user_input[3:])
                    buffer = user_input.encode('utf-8')
                    print(buffer)
                    ble.connections[0][UARTService].write(buffer)
                    time.sleep(1)
                elif user_input[0] in ['M', 'm', 'B']:
                    value = int(user_input[2:])
                    buffer = user_input.encode('utf-8')
                    print(buffer)
                    ble.connections[0][UARTService].write(buffer)
                    time.sleep(1)
                else:
                    print("Invalid command.")
            else:
                print("Invalid input. Please enter a valid command.")
        else:
            print("Invalid input. Please enter a valid command.")