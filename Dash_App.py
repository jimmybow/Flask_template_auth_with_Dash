# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 10:39:33 2018

@author: jimmybow
"""
from dash import Dash
from dash.dependencies import Input, State, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from datetime import datetime, timedelta
from Dash_fun import serve_layout, load_object, save_object

layout = html.Div([
                  html.Div('起始時間：', style = {'display':'inline-block', 'margin': 15, 'font-size': 20}),
                  html.Div(dcc.DatePickerSingle(id = 'time_start',
                                                initial_visible_month = datetime.date(datetime.now()),
                                                date = datetime.date(datetime.now()),
                                                placeholder = '年-月-日',
                                                display_format = 'YYYY-MM-DD'),
                           style = {'display':'inline-block', 'margin': 15, 'font-size': 20}),
                  html.Div('結束時間：', style = {'display':'inline-block', 'margin': 15, 'font-size': 20}),
                  html.Div(dcc.DatePickerSingle(id = 'time_end',
                                                initial_visible_month = datetime.date(datetime.now()) - timedelta(days = 5),
                                                date = datetime.date(datetime.now()) - timedelta(days = 5),
                                                placeholder = '年-月-日',
                                                display_format = 'YYYY-MM-DD'),
                           style = {'display':'inline-block', 'margin': 15, 'font-size': 20}),
                  html.Div('連線接收端 IP', style = {'display':'inline-block', 'margin': 15, 'font-size': 20}),
                  html.Div(dcc.Dropdown(id = 'Dropdown', searchable = False, clearable = False,
                                        options=[{'label': '顯示所有', 'value': 'all'}],
                                        value = 'all' 
                                        ),
                           style={'width': '15%', 'margin': '25px 15px', 'display':'inline-block', 'font-size': 20, 'vertical-align': 'bottom'} ),
                  dcc.Graph(id = 'graph',
                            figure = { 'data': [  {'x': [1, 2, 3], 'y': [4, 1, 2]}  ]  }       )
                ])

def Add_Dash(server, create_secret):
    url_base_pathname = '/dash/app1/'
    app = Dash(server=server, url_base_pathname=url_base_pathname)
    app.config.supress_callback_exceptions = True
    app.layout = app.layout = serve_layout

    @app.callback(
            Output('index', 'children'),
            [Input('url', 'search')])
    def display_page(request_args):
        if request_args:
            rr = pd.Series(str(request_args)[1:].split('&')).str.split('=')
            key = rr.str.get(0)
            value = rr.str.slice(1,).str.join('=')   
            if 'secret' in list(key) and value[key == 'secret'].iloc[0] == create_secret(url_base_pathname):
                return layout
        return html.Div('Error ! 不可訪問 !')
    
    @app.callback(
            Output('Dropdown', 'options'),
            [Input('time_start', 'date'),
             Input('time_end', 'date')])
    def callback(time_start, time_end):
        return [{'label': '顯示所有', 'value': 'all'},
                {'label': 'time_start', 'value': time_start},
                {'label': 'time_end',   'value': time_end}     ]
    
    return app.server, url_base_pathname