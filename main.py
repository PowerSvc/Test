import os
import subprocess
import sys
import time

while (True):
    process = subprocess.Popen([sys.executable, "main.py"])
    print('запускаю заново цыкл')
    process.wait()

