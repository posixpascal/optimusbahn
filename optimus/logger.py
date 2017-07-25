import logging

logger = logging.getLogger()
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
fileHandler = logging.FileHandler("logs/optimus.log")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)