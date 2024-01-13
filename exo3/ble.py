import platform
import time
import _bleio
import random
import time

from adafruit_ble import BLERadio
from adafruit_ble.services.nordic import UARTService

if platform.system() == 'Darwin':
    addr = _bleio.Address(string="35AAF6EA-6FF0-EDDF-76BB-5D5F6F818760")
elif platform.system() == 'Windows':
    addr = _bleio.Address(string="ce:bf:e4:0c:07:6a")

class BLEservice():
    def __init__(self):
        self.ble = BLERadio()
        self.addr = None
        self.connected = False
        self.connections = []
        self.connection = None
        self.uart = None
        self.uart_service = None
    
    def _connect(self, addr):
        self.addr = addr
        self.ble.start_scan()
        while not self.connected:
            for adv in self.ble.start_scan():
                if adv.address == self.addr:
                    self.connection = self.ble.connect(self.addr)
                    self.connections.append(self.connection)
                    self.uart_service = self.connection[UARTService]
                    self.uart = self.uart_service.start_service()
                    self.connected = True
                    self.ble.stop_scan()
                    break
        print("Connected")
        print("Commands: 'S' to stop, 'G' to go, 'C' to calibrate")
        print("'Kp <value>' to set Kp, 'Ki <value>' to set Ki, 'Kd <value>' to set Kd")
        print("'M <value>' to set max speed, 'm <value>' to set min speed")
        print("'B <value>' to set base speed")
    
    def send(self, cmd):
        if self.connected:
            buffer = cmd.encode('utf-8')
            self.uart.write(buffer)
            time.sleep(1)
        else:
            print("Not connected.")

    def listen(self):
        if self.connected:
            while self.connected:
                if self.uart.in_waiting:
                    print(self.uart.read(self.uart.in_waiting).decode('utf-8'))
        else:
            print("Not connected.")
    
    def disconnect(self):
        if self.connected:
            self.connection.disconnect()
            self.connected = False
            self.connection = None
            self.uart = None
            self.uart_service = None
            print("Disconnected")
        else:
            print("Not connected.")
    
    def sniffing(self):
        #scanning surrounding devices
        print("Scanning...")
        startTime = time.time()
        for adv in self.ble.start_scan():
            print(adv.address)
            print(f"name : {adv.complete_name}")
            print(adv.rssi)
            print()
            currentTime = time.time()
            if currentTime - startTime > 5:
                break
        self.ble.stop_scan()
        
        

"""
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
"""

if __name__ == "__main__":
    BleSession = BLEservice()
    BleSession.sniffing()