import threading 

from optimus.stations import Stations
from optimus.observer import StationObserver
from optimus.config import config
from optimus.utils import thread_group
from optimus.db import setup_db

class Optimus(object):
    """Optimus

    This class handles most of the underlaying logic for 
    optimizing bahn.de 
    """

    def __init__(self):
        self.stations = Stations.load()
        self.observers = []  

    def start(self):
        self.observers = []
        for stations in thread_group(self.stations, config['app']['threads']):
            self.observers.append(
                StationObserver(stations)
            )
        
        i = 1
        for observer in self.observers:
            thread = threading.Thread(target=observer.start, args = ())
            observer.thread = thread
            observer.thread_id = i
            thread.start()
            i += 1
        
        print("Total of {0} Observers started".format(len(self.observers)))



if __name__ == "__main__":
    setup_db()
    Optimus().start()