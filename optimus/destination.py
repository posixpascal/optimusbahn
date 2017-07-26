class Destination(object):
    def __init__(self):
        self.arrival = None
        self.departure = None
        self.platform = None
        self.name = None
        self.status = None

    @classmethod
    def from_html(cls, html):
        destination = Destination()
        if html.find("td", {'class': "station"}):
            destination.name = html.find("td", {'class': "station"}).text.strip()
            destination.arrival = html.find("td", {'class': "arrival"}).text.replace("&nbsp;", "").strip()
            destination.departure = html.find("td", {'class': "departure"}).text.replace("&nbsp;", "").strip()
            destination.platform = html.find("td", {'class': "platform"}).text.replace("&nbsp;", "").strip()
            return destination
        else: # metadata
            return False