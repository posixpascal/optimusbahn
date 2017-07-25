from flask import Flask

api = Flask(__name__)

from optimus.api import views