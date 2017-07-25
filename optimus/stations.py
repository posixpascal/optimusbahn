from optimus.db import insert_station
import csv

class Stations(object):
    def __init__(self):
        print("OK")

    @classmethod
    def load(cls):
        stations = []
        with open('data/stations.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter = ";", quotechar='"')
            skip = True
            for station in reader:
                if skip:
                    skip = False
                    continue
                stations.append(Station(station))
                # Insert station in db
                insert_station(station)

        return stations

class Station(object):
    def __init__(self, data):
        evanr, ds100, name, travel_type, lat, lng, _, __ = data
        self.evanr = evanr
        self.ds100 = ds100
        self.name = name
        self.travel_type = travel_type
        self.lat = lat
        self.lng = lng
