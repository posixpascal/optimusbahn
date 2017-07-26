import sys
import os
import moment
import shutil
import json

optimus_folder = os.path.realpath(os.path.abspath("./"))
sys.path.insert(0, optimus_folder)

MYSQL_DATE_FORMAT = "YYYY-MM-DD HH:mm:ss"

from optimus.db import fetch_sql, run_sql, fetch_sql_in_range
from optimus.utils import parse_delay

result = {
    'started': moment.now().format("DD.MM.YYYY HH:mm:ss"),
    'results': {}
}

if __name__ == "__main__":
    print("Collecting delays per hour...")
    current = moment.now()

    for hour in range(24):
        start = current.replace(hours=hour, minutes=0, seconds=0).format(MYSQL_DATE_FORMAT)
        end = current.replace(hours=hour, minutes=59, seconds=59).format(MYSQL_DATE_FORMAT)


        delays = fetch_sql_in_range("sql/stats/collect-delay-per-hour.sql", start, end)
        print("Found {0} delay entries for hour@{1}".format(len(delays), hour))
        total = 0
        delayed_trains = 0
        for delay in delays:
            delay = parse_delay(delay[0])
            total += delay
            if delay > 0:
                delayed_trains += 1

        print("Total of {0} minutes delay for hour@{1}".format(total, hour))
        result['results'][str(hour)] = {
            'total_delay': total,
            'total_trains': len(delays),
            'delayed_trains': delayed_trains
        }

    print("Done collecting")
    output_file = "data/delays-today.json"

    try:
        shutil.move(output_file, "data/delays-yesterday.json")
    except FileNotFoundError:
        pass

    with open(output_file, "w+") as f:
        f.write(json.dumps(result))

    print("Done. Written to: {0}".format(output_file))
