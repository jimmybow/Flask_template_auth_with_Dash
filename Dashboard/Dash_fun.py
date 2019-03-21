# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 22:34:51 2019

@author: jimmybow
"""

from datetime import datetime, timedelta
from extensions import cache
from urllib.parse import parse_qs
from dash.dependencies import Input, State, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import uuid
import os
import pickle
import string, random

@cache.memoize(timeout=1800)
def create_secret(key):
    return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(100))

def get_dash_url(url_base):
    return '{}?secret={}'.format(url_base, create_secret(url_base))

def save_object(obj, session_id, name):
    os.makedirs('Dir_Store', exist_ok=True)
    file = 'Dir_Store/{}_{}'.format(session_id, name)
    pickle.dump(obj, open(file, 'wb'))
    
def load_object(session_id, name):
    file = 'Dir_Store/{}_{}'.format(session_id, name)
    obj = pickle.load(open(file, 'rb'))
    os.remove(file)
    return obj

def clean_Dir_Store():
    if os.path.isdir('Dir_Store'):
        file_list = pd.Series('Dir_Store/' + i for i in os.listdir('Dir_Store'))
        mt = file_list.apply(lambda x: datetime.fromtimestamp(os.path.getmtime(x))).astype(str)
        for i in file_list[mt < str(datetime.now() - timedelta(hours = 3))]: os.remove(i)
        
def serve_layout():
    session_id = str(uuid.uuid4())
    clean_Dir_Store()
    return html.Div([
        html.Div(session_id, id='session_id', style={'display': 'none'}),
        dcc.Location(id='url', refresh=False),
        html.Div(id='index')
    ])

def apply_layout(app, layout):
    app.config.supress_callback_exceptions = True
    app.layout = serve_layout

    @app.callback(
            Output('index', 'children'),
            [Input('url', 'search')])
    def display_page(request_args):
        if request_args:
            url_args = parse_qs(request_args[1:])   
            if 'secret' in url_args and url_args['secret'][0] == create_secret(app.url_base_pathname):
                return layout
        return html.Div('Error ! 不可訪問 !')