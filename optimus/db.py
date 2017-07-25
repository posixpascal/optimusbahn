import MySQLdb

from optimus.logger import logger
from optimus.config import config

conn = MySQLdb.connect(
    host = config["mysql"]["host"],
    user = config["mysql"]["user"],
    passwd = config["mysql"]["passwd"],
    db = config["mysql"]["db"])

def run_sql(filename, *args):
    cur = conn.cursor()
    cur.connection.autocommit(True)
    with open(filename, "r") as sql:
        query = sql.read()
        if len(args) > 0:        
            query = query.format(*args)
        print(query)
        cur.execute(query)
    cur.close()

def fetch_sql(filename, *args):
    cur = conn.cursor()
    cur.connection.autocommit(True)
    with open(filename, "r") as sql:
        query = sql.read()
        if len(args) > 0:        
            query = query.format(*args)
        cur.execute(query)
    cur.close()
    result = []
    for row in cur:
        result.append(row)
    return result

def setup_db():
    run_sql("sql/create-journeys.sql")
    run_sql("sql/create-trains.sql")
    run_sql("sql/create-stations.sql")

def insert_journey(journey, station):
    if journey.is_delayed(): 
        delayed = 1
    else: delayed = 0

    # Check if any ID was found.
    station_ids = fetch_sql("sql/get-station-id.sql", station.name)
    if len(station_ids):
        station_id = station_ids[0][0]
    else: return False

    # Insert journey to database
    run_sql("sql/insert-journey.sql", 
        station_id,
        journey.train,
        journey.platform,
        journey.status,
        delayed
    )

    logger.debug("Inserted journey: {0}".format(journey.train))

def insert_station(station):
    evanr, ds100, name, travel_type, lat, lng, _, __ = station
    run_sql("sql/insert-station.sql", 
        name,
        evanr,
        ds100,
        lat,
        lng
    )
    logger.debug("Inserted station: {0}".format(name))
