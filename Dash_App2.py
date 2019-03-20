# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 10:39:33 2018

@author: jimmybow
"""
from dash import Dash
from dash.dependencies import Input, State, Output
import dash_core_components as dcc
import dash_html_components as html
from urllib.parse import parse_qs
import pandas as pd
from datetime import datetime, timedelta
from Dash_fun import serve_layout, load_object, save_object

layout = html.Div('This is app2')

def Add_Dash(server, create_secret):
    url_base_pathname = '/dash/app2/'
    app = Dash(server=server, url_base_pathname=url_base_pathname)
    app.config.supress_callback_exceptions = True
    app.layout = serve_layout

    @app.callback(
            Output('index', 'children'),
            [Input('url', 'search')])
    def display_page(request_args):
        if request_args:
            url_args = parse_qs(request_args[1:])   
            if 'secret' in url_args and url_args['secret'][0] == create_secret(url_base_pathname):
                return layout
        return html.Div('Error ! 不可訪問 !')
    
    return app.server, url_base_pathname