# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 10:39:33 2018

@author: jimmybow
"""
from dash import Dash
from dash.dependencies import Input, State, Output
from .Dash_fun import create_secret, apply_layout, load_object, save_object
import dash_core_components as dcc
import dash_html_components as html

url_base = '/dash/app1/'

layout = html.Div([
    html.Div('This is app1'),
    html.A('Go to app2', href = '/app2', target='_parent'),
    html.Br(), html.Br(), 
    dcc.Input(id = 'input_text'),
    html.Div(id = 'target')
])

def Add_Dash(server):
    app = Dash(server=server, url_base_pathname=url_base)
    apply_layout(app, layout)

    @app.callback(
            Output('target', 'children'),
            [Input('input_text', 'value')])
    def callback(value):
        return value
    
    return app.server