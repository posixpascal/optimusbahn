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

@api.route('/data/delays')
def delays_today():
    with open('data/delays-today.json', 'r') as f:
        return f.read()

@api.route('/data/delays/yesterday')
def delays_yesterday():
    with open('data/delays-yesterday.json', 'r') as f:
        return f.read()

@api.route('/data/year')
def delays_year():
    with open('data/delay-per-year.json', 'r') as f:
        return f.read()

@api.route('/data/trains')
def trains_today():
    with open('data/trains-today.json', 'r') as f:
        return f.read()