# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 22:34:51 2019

@author: jimmybow
"""

from datetime import datetime, timedelta
from flask_login import current_user
import dash_html_components as html
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
        
def apply_layout_with_auth(app, layout):
    def serve_layout():
        if current_user and current_user.is_authenticated:
            session_id = str(uuid.uuid4())
            clean_Dir_Store()
            return html.Div([
                html.Div(session_id, id='session_id', style={'display': 'none'}),
                layout
            ])
        return html.Div('403 Access Denied')
    
    app.config.supress_callback_exceptions = True
    app.layout = serve_layout
