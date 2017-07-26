from flask import render_template
from optimus.api import api
from optimus.db import fetch_sql, fetch_paged_sql
from optimus.config import config as cfg

@api.route('/')
def index():
    return render_template('dashboard.html')


@api.route('/trains/')
def trains():
    trains = fetch_sql('sql/list-trains.sql')
    return render_template('trains.html', trains = trains)


@api.route('/stations/')
@api.route('/stations/<int:page>')
def stations(page = 1):
    page = page - 1
    stations = fetch_paged_sql('sql/list-stations.sql', page)
    return render_template('stations.html', stations = stations, page = page + 1)


@api.route('/config/')
def config():
    return render_template('config.html', cfg = cfg)