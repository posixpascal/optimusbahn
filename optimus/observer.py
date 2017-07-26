import logging
import threading
from optimus.logger import logFormatter
from optimus.bahn import get_departure_board
from optimus.db import insert_journey
class StationObserver(object):
    def __init__(self, stations):
        self.thread_id = 0
        self.logger = None
        self.stations = stations

    def start(self):
        self.setup_logger()
        for station in self.stations:
            self.fetch_trains(station)
        

    def fetch_trains(self, station):
        departure_board = get_departure_board(station)
        for journey in departure_board:
            insert_journey(journey, station)
            self.logger.debug("Add journey to database {0}".format(journey.train))
            # insert train maybe?
        print("Inserted {0} journeys".format(len(departure_board)))

    def setup_logger(self):
        file_handler = logging.FileHandler("logs/stationobserver-{0}.log".format(self.thread_id))
        file_handler.setFormatter(logFormatter)
        self.logger = logging.getLogger("SO_{0}".format(self.thread_id))
        self.logger.setLevel(logging.DEBUG)
        
        self.logger.addHandler(file_handler)