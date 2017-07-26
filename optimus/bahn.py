import requests
import moment
import traceback

from optimus.journey import Journey
from optimus.train import Train
from optimus.utils import truncate

from datetime import datetime
from bs4 import BeautifulSoup

BAHN_TIME_FORMAT = "HH:mm:ss"
BAHN_DATE_FORMAT = "D.MM.YYYY"

def rabdc_request(station):
    dt = moment.now().locale("Europe/Berlin")
    
    uri = "https://rabdc.bahn.de/bin/bhftafel.exe/dn?country=DEU&protocol=https:&rt=1&input={0}&boardType=dep&time={1}&productsFilter=11111&&&date={2}&&selectDate=&maxJourneys=&start=yes".format(
        station.name,
        dt.format(BAHN_TIME_FORMAT),
        dt.format(BAHN_DATE_FORMAT)
    )
    
    request = requests.get(uri)

    soup = BeautifulSoup(request.text, "html.parser")
    departure_boards = soup.select("table.result.stboard.dep")

    for departure_board in departure_boards:
        return parse_depature_board(departure_board)
    
    return []

def get_departure_board(station):
    journeys = rabdc_request(station)
    return journeys

def parse_depature_board(soup):
    journeys = []
    entries = soup.select("tr[id^='journeyRow_']")
    for entry in entries:
        journey = Journey()

        try:
            train = Train.from_url(entry.findAll("td", {'class': "train"})[1].find('a')['href'])
            train.name = truncate(entry.findAll("td", {'class': "train"})[1].text)

            journey.time = entry.find("td", {'class': "time"}).text.strip()
            journey.train = train

            if entry.find("td", {'class': "platform"}):
                journey.platform = entry.find("td", {'class': "platform"}).text.strip()
            journey.status = entry.find("td", {'class': 'ris'}).text.strip()
            journeys.append(journey)
        except Exception as e:
            print(traceback.format_exc())

    return journeys