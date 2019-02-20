# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 22:34:51 2019

@author: jimmybow
"""

import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime, timedelta
import pandas as pd
import uuid
import os
import pickle

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