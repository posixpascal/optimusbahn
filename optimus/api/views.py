from flask import render_template
from optimus.api import api

@api.route('/')
@api.route('/index')
def index():
    return render_template('dashboard.html')