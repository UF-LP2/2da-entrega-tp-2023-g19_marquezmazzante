import subprocess
from datetime import datetime
import time
import os

def clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
def RelojComputacional():

    for h in range (0, 24):
        for m in range(0,60):
            print("hora:", h, "min:", m)
            time.sleep(0.5)
            clear()

if __name__ == "__main__":
    RelojComputacional()