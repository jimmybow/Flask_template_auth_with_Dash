# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 02:04:00 2018

@author: jimmybow
"""

from flask import Flask, render_template
from extensions import cache
from Dashboard.Dash_fun import get_dash_url
from Dashboard import Dash_App, Dash_App2

app = Flask(__name__)

cache.init_app(app)
app = Dash_App.Add_Dash(app)
app = Dash_App2.Add_Dash(app)

@app.route('/')
def url_with_app1():
    return render_template('template_with_app1.html', Dash_App_url = get_dash_url(Dash_App.url_base))

@app.route('/app2')
def url_with_app2():
    return render_template('template_with_app2.html', Dash_App2_url = get_dash_url(Dash_App2.url_base))

if __name__ == '__main__':
    app.run(debug=True)
