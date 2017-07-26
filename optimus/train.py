import requests
from bs4 import BeautifulSoup
from optimus.destination import Destination

class Train(object):
    def __init__(self):
        self.id = None
        self.name = None
        self.arrival = None
        self.departure = None
        self.destinations = []

    @classmethod
    def from_url(cls, url):
        train = Train()

        url = "https://rabdc.bahn.de/{0}".format(url)
        request = requests.get(url)

        soup = BeautifulSoup(request.text, "html.parser")
        tables = soup.select("table.result.stboard.train")

        for table in tables:
            tablerows = table.select('tr')
            for tablerow in tablerows:
                if tablerow.get('class') == 'current': continue
                destination = Destination.from_html(tablerow)
                if destination:
                    train.destinations.append(destination)

            train.departure = train.destinations[0].departure
            train.arrival = train.destinations[len(train.destinations) - 1].arrival

        return train