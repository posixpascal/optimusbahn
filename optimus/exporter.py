import time
import os

def exporter_start():
    while True:
        os.system("python3 scripts/collect-hourly-delay.py")
        os.system("python3 scripts/collect-per-month.py")
        os.system("python3 scripts/collect-trains.py")
        time.sleep(60)