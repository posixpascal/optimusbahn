import json
import shutil
import sys

import moment
import os

optimus_folder = os.path.realpath(os.path.abspath("./"))
sys.path.insert(0, optimus_folder)

MYSQL_DATE_FORMAT = "YYYY-MM-DD HH:mm:ss"

from optimus.db import fetch_sql_in_range
from optimus.utils import parse_delay

result = {
    'started': moment.now().format("DD.MM.YYYY HH:mm:ss"),
    'results': {}
}

if __name__ == "__main__":
    print("Collecting train delays today...")
    current = moment.now()

    start = current.replace(hours=0, minutes=0, seconds=0).format(MYSQL_DATE_FORMAT)
    end = current.replace(hours=23, minutes=59, seconds=59).format(MYSQL_DATE_FORMAT)

    delays = fetch_sql_in_range("sql/stats/collect-delay-per-hour.sql", start, end)
    total = 0
    delayed_trains = 0
    for delay in delays:
        delay = parse_delay(delay[0])
        if delay > 0:
            delayed_trains += 1

    result['results'] = {
        'total_trains': len(delays),
        'delayed_trains': delayed_trains
    }

    print("Done collecting")
    output_file = "data/trains-today.json"

    try:
        shutil.move(output_file, "data/trains-yesterday.json")
    except FileNotFoundError:
        pass

    with open(output_file, "w+") as f:
        f.write(json.dumps(result))

    print("Done. Written to: {0}".format(output_file))
