# Imports from 3rd party libraries
import dash
import pandas as pd
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_daq as daq
from joblib import load


# Imports from this application
from app import app

#Load pipeline
pipeline_xgb = load('assets/pipeline_xgb.joblib')
print('Pipeline Loaded!')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Toggle various inputs to get predicted outcome.

            """
        ),
        
        dcc.Markdown(" ", id='out1'),

        dcc.Slider(
            id='goals',
            min=0,
            max=10,
            step=.1,
            value=1,
            marks={
                0: '0',
                1: '1',
                2: '2',
                3: '3',
                4: '4',
                5: '5',
                6: '6',
                7: '7',
                8: '8',
                9: '9',
                10: '10',
                },
            className='mb-5'
        ),
        dcc.Markdown(" ", id='out2'),

         dcc.Slider(
            id='shots',
            min=0,
            max=60,
            step=.1,
            value=20,
            marks={
                0: '0',
                15: '15',
                30: '30',
                45: '45',
                60: '60'},
            className='mb-5'
        ),

        dcc.Markdown(" ", id='out3'),

        dcc.Slider(
            id='hits',
            min=0,
            max=60,
            step=.1,
            value=20,
            marks={
                0: '0',
                15: '15',
                30: '30',
                45: '45',
                60: '60'},
            className='mb-5'
        ),

        dcc.Markdown(" ", id='out4'),

        dcc.Slider(
            id='pim',
            min=0,
            max=60,
            step=.1,
            value=20,
            marks={
                0: '0',
                15: '15',
                30: '30',
                45: '45',
                60: '60'},
            className='mb-5'
        ),

        dcc.Markdown(" ", id='out5'),

        dcc.Slider(
            id='powerPlayOpportunities',
            min=0,
            max=10,
            step=.1,
            value=3,
            marks={
                0: '0',
                1: '1',
                2: '2',
                3: '3',
                4: '4',
                5: '5',
                6: '6',
                7: '7',
                8: '8',
                9: '9',
                10: '10',
                },
            className='mb-5'
        ),

        dcc.Markdown(" ", id='out6'),

        dcc.Slider(
            id='faceOffWinPercentage',
            min=0,
            max=100,
            step=.1,
            value=20,
            marks={
                0: '0',
                20: '20',
                40: '40',
                60: '60',
                80: '80',
                100: '100'},
            className='mb-5'
        ),
    ],

    #change column width here, currently 6/12
    md=6,  
)

column2 = dbc.Col(
    [   
        dcc.Markdown(" ", id='out7'),
        dcc.Slider(
            id='giveaways',
            min=0,
            max=20,
            step=.1,
            value=8,
            marks={
                0: '0',
                5: '5',
                10: '10',
                15: '15',
                20: '20'},
            className='mb-5'
        ),

        dcc.Markdown(" ", id='out8'),

        dcc.Slider(
            id='takeaways',
            min=0,
            max=40,
            step=.1,
            value=20,
            marks={
                0: '0',
                15: '15',
                30: '30',
                45: '45',
                60: '60'},
            className='mb-5'
        ),

        dcc.Markdown('##### Regular Season or Playoffs?'), 
        dcc.Dropdown(
            id='game_type', 
            options = [
                {'label': 'Regular Season', 'value': 2}, 
                {'label': 'Playoffs', 'value': 3},  
            ], 
            value = 2, 
            className='mb-5',
            #style={'height': '30px', 'width': '300px'},
        ),

        dcc.Markdown('##### Home or Away Game?'), 
        dcc.Dropdown(
            id='HoA', 
            options = [
                {'label': 'Home', 'value': 'home'}, 
                {'label': 'Away', 'value': 'away'},  
            ], 
            value = 'home', 
            className='mb-5',
            #style={'height': '30px', 'width': '300px'},
        ),

        html.H4('Probability of Winning:', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
    ]
)

layout = dbc.Row([column1, column2], align="center")

@app.callback(
    Output('prediction-content', 'children'),
    [
        Input('goals', 'value'), 
        Input('shots', 'value'), 
        Input('hits', 'value'), 
        Input('pim', 'value'), 
        Input('powerPlayOpportunities', 'value'), 
        Input('faceOffWinPercentage', 'value'),
        Input('giveaways', 'value'),
        Input('takeaways', 'value'),
        Input('game_type', 'value'),
        Input('HoA', 'value'),
    ],
)
def predict(goals, shots, hits, pim, powerPlayOpportunities, faceOffWinPercentage, giveaways, takeaways, game_type, HoA):
    df_dash = pd.DataFrame(
        columns=['goals', 'shots', 'hits', 'pim', 'powerPlayOpportunities', 'faceOffWinPercentage','giveaways', 'takeaways','game_type','HoA'], 
        data=[[goals, shots, hits, pim, powerPlayOpportunities, faceOffWinPercentage, giveaways, takeaways, game_type, HoA]]
    )
    y_pred = pipeline_xgb.predict_proba(df_dash)[:,1]
    return f'{y_pred}'

@app.callback(
    Output(component_id='out1', component_property='children'),
    [Input(component_id='goals', component_property='value')]
)
def update_output_div(input_value):
    return 'Number of Goals: {}'.format(input_value)

@app.callback(
    Output(component_id='out2', component_property='children'),
    [Input(component_id='shots', component_property='value')]
)
def update_output_div(input_value):
    return 'Number of Shots: {}'.format(input_value)

@app.callback(
    Output(component_id='out3', component_property='children'),
    [Input(component_id='hits', component_property='value')]
)
def update_output_div(input_value):
    return 'Number of Hits: {}'.format(input_value)

@app.callback(
    Output(component_id='out4', component_property='children'),
    [Input(component_id='pim', component_property='value')]
)
def update_output_div(input_value):
    return 'Amount of Penalty Minutes: {}'.format(input_value)

@app.callback(
    Output(component_id='out5', component_property='children'),
    [Input(component_id='powerPlayOpportunities', component_property='value')]
)
def update_output_div(input_value):
    return 'Power Play Opportunities: {}'.format(input_value)

@app.callback(
    Output(component_id='out6', component_property='children'),
    [Input(component_id='faceOffWinPercentage', component_property='value')]
)
def update_output_div(input_value):
    return 'Face Off Wins by Percent: {}%'.format(input_value)

@app.callback(
    Output(component_id='out7', component_property='children'),
    [Input(component_id='giveaways', component_property='value')]
)
def update_output_div(input_value):
    return 'Number of Giveaways: {}'.format(input_value)

@app.callback(
    Output(component_id='out8', component_property='children'),
    [Input(component_id='takeaways', component_property='value')]
)
def update_output_div(input_value):
    return 'Number of Takeaways: {}'.format(input_value)
