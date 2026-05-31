import argparse
import json
import re
import sys
from pathlib import Path
import numpy as np
import serial
from connect4_engine.hardware.arduino import ArduinoCommunicator
from connect4_engine.hardware.mock import ArduinoPumpNoOp
from connect4_engine.hardware.robot import RobotCommunicator
from connect4_engine.utils.config import resolve_port
from time import sleep, perf_counter

if __name__ == "__main__":
    ard_port = resolve_port("arduino")
    ard = ArduinoCommunicator(ser=serial.Serial(ard_port, 115200))
    sol_to_turn_on = 0
    sol_is_on = False
    time_on = 0
    while(True):
        cmd = input(f"select solenoid to open or press <enter> to toggle. ")
        if(cmd == 'q'):
            break
        elif cmd == '':
            pass
        elif cmd.startswith('o'):
            time_on = int(cmd[1:])
            ard.turn_on_solenoid(sol_to_turn_on)           
            sleep(time_on / 1000)
            ard.turn_off_solenoids()
            continue

        elif cmd in '1234567':
            sol_to_turn_on = int(cmd[0]) - 1
        
        if sol_is_on:
            ard.turn_off_solenoids()
            end = perf_counter()
            elapsed_ms = (end - start) * 1000
            print(f"Time passed: {elapsed_ms:.2f} ms")
            sol_is_on = False
        else:
            ard.turn_on_solenoid(sol_to_turn_on)           
            start = perf_counter()
            sol_is_on = True
