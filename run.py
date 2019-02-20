# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 02:04:00 2018

@author: jimmybow
"""

from flask import Flask, render_template, request
from datetime import datetime
import string, random
from flask_caching import Cache
import Dash_App, Dash_App2

app = Flask(__name__)

cache = Cache(app, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory',
    'CACHE_THRESHOLD': 50  # should be equal to maximum number of active users
})

@cache.memoize(timeout=1800)
def create_secret(key):
    return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(100))

app, Dash_App_url_base = Dash_App.Add_Dash(app, create_secret)
app, Dash_App2_url_base = Dash_App2.Add_Dash(app, create_secret)

@app.route('/')
def url_with_app1():
    Dash_App_url = '{}?secret={}'.format(Dash_App_url_base, create_secret(Dash_App_url_base))
    return render_template('url_with_app1.html', Dash_App_url=Dash_App_url)

@app.route('/app2')
def url_with_app2():
    Dash_App2_url = '{}?secret={}'.format(Dash_App2_url_base, create_secret(Dash_App2_url_base))
    return render_template('url_with_app2.html', Dash_App2_url=Dash_App2_url)

if __name__ == '__main__':
    app.run(debug=True)
