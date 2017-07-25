class Journey(object):
    def __init__(self):
        self.time = ""
        self.train = ""
        self.destinations = ""
        self.platform = 0
        self.status = ""

    def is_delayed(self):
        return self.status and self.status != "+0"