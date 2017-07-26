import MySQLdb

from optimus.logger import logger
from optimus.config import config

conn = MySQLdb.connect(
    host = config["mysql"]["host"],
    user = config["mysql"]["user"],
    passwd = config["mysql"]["passwd"],
    db = config["mysql"]["db"])

# Execute SQL file without caring about the result (atm)
def run_sql(filename, *args):
    cur = conn.cursor()
    cur.connection.autocommit(True)
    with open(filename, "r") as sql:
        query = sql.read()
        if len(args) > 0:        
            query = query.format(*args)
        cur.execute(query)
    cur.close()

# Fetch all by query
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

# Fetch in range
def fetch_sql_in_range(filename, start, end):
    cur = conn.cursor()
    cur.connection.autocommit(True)
    with open(filename, "r") as sql:
        query = sql.read()
        query = query.format(start, end)
        cur.execute(query)
    cur.close()
    result = []
    for row in cur:
        result.append(row)
    return result

# Add a page variable to the query before running it
def fetch_paged_sql(filename, page, size = 25):
    cur = conn.cursor()
    cur.connection.autocommit(True)
    with open(filename, "r") as sql:
        query = sql.read()
        query = query.format(page * size)
        cur.execute(query)
    cur.close()
    result = []
    for row in cur:
        result.append(row)
    return result

# Initialize optimus dbs
def setup_db():
    run_sql("sql/create-trains.sql")
    run_sql("sql/create-stations.sql")
    run_sql("sql/create-journeys.sql")
    run_sql("sql/create-destinations.sql")

# Helper to insert train journey
def insert_journey(journey, station):
    train_id = None

    if journey.is_delayed(): 
        delayed = 1
    else: delayed = 0

    # Check if any ID was found.
    station_ids = fetch_sql("sql/get-station-id.sql", station.name)
    if len(station_ids):
        station_id = station_ids[0][0]
    else: return False

    # Fetch train id or create it
    train_ids = fetch_sql("sql/get-train-id-by-name.sql", journey.train.name)
    if len(train_ids):
        train_id = train_ids[0][0]
    else:
        run_sql("sql/insert-train.sql",
                journey.train.name,
                journey.train.arrival,
                journey.train.departure
        )
        train_ids = fetch_sql("sql/get-train-id-by-name.sql", journey.train.name)
        if len(train_ids):
            train_id = train_ids[0][0]


    # Insert journey to database
    run_sql("sql/insert-journey.sql", 
        station_id,
        train_id,
        journey.platform,
        journey.status,
        delayed
    )

    for destination in journey.train.destinations:
        insert_destination(train_id, destination)

    logger.debug("Inserted journey: {0}".format(journey.train))

def insert_destination(train_id, destination):
    run_sql("sql/insert-destination.sql",
            train_id,
            destination.name,
            destination.departure,
            destination.arrival,
            destination.platform,
            destination.status
    )


# Helper to insert a station
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
