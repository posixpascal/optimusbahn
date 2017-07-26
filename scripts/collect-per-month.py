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
    print("Collecting delays per month...")

    for month in range(12):
        current = moment.now().replace(day=1)

        month = month + 1
        # Genius level date scripting ...
        start = current.replace(month=month, day=1, hours=0, minutes=0, seconds=0).format(MYSQL_DATE_FORMAT)

        try:
            end = current.replace(month=month, day=31, hours=23, minutes=59, seconds=59).format(MYSQL_DATE_FORMAT)
        except:
            try:
                end = current.replace(month=month, day=30, hours=23, minutes=59, seconds=59).format(MYSQL_DATE_FORMAT)
            except:
                try:
                    end = current.replace(month=month, day=29, hours=23, minutes=59, seconds=59).format(MYSQL_DATE_FORMAT)
                except:
                    end = current.replace(month=month, day=28, hours=23, minutes=59, seconds=59).format(MYSQL_DATE_FORMAT)

        # The hour sql query works for months as well.
        delays = fetch_sql_in_range("sql/stats/collect-delay-per-hour.sql", start, end)
        total = 0
        delayed_trains = 0
        for delay in delays:
            delay = parse_delay(delay[0])
            total += delay
            if delay > 0:
                delayed_trains += 1

        result['results'][str(month)] = {
            'total_delay': total,
            'total_trains': len(delays),
            'delayed_trains': delayed_trains
        }

    print("Done collecting")
    output_file = "data/delay-per-year.json"

    with open(output_file, "w+") as f:
        f.write(json.dumps(result))

    print("Done. Written to: {0}".format(output_file))
