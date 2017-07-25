import threading

from optimus.api import api
from optimus.config import config
from optimus.db import setup_db
from optimus.observer import StationObserver
from optimus.stations import Stations
from optimus.utils import thread_group


class Optimus(object):
    """Optimus

    This class handles most of the underlaying logic for 
    optimizing bahn.de 
    """

    def __init__(self):
        self.stations = Stations.load()
        self.observers = []
        self.api = None

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
        self.api = threading.Thread(target=api.run, args = ())
        self.api.start()


if __name__ == "__main__":
    setup_db()
    Optimus().start()
