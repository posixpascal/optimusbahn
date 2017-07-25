from flask import render_template
from optimus.api import api
from optimus.db import fetch_sql
from optimus.config import config as cfg

@api.route('/')
def index():
    return render_template('dashboard.html')


@api.route('/trains/')
def trains():
    trains = fetch_sql('sql/list-trains.sql')
    return render_template('trains.html', trains = trains)


@api.route('/stations/')
def stations():
    return render_template('stations.html')


@api.route('/config/')
def config():
    return render_template('config.html', cfg = cfg)