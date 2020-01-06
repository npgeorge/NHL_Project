# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_daq as daq

# Imports from this application
from app import app

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
            step=1,
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
            id='pp-opp',
            min=0,
            max=10,
            step=1,
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

        dcc.Markdown(" ", id='out3'),

         dcc.Slider(
            id='shots',
            min=0,
            max=60,
            step=5,
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
            id='face-offs',
            min=0,
            max=100,
            step=5,
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
        dcc.Markdown('##### Home or Away Game?'), 
        dcc.Dropdown(
            id='HoA', 
            options = [
                {'label': 'Home', 'value': 'Home'}, 
                {'label': 'Away', 'value': 'Away'},  
            ], 
            value = 'Home', 
            className='mb-5',
            #style={'height': '30px', 'width': '300px'},
        ),

        dcc.Markdown(" ", id='out5'),

        dcc.Slider(
            id='hits',
            min=0,
            max=60,
            step=5,
            value=20,
            marks={
                0: '0',
                15: '15',
                30: '30',
                45: '45',
                60: '60'},
            className='mb-5'
        ),

        dcc.Markdown(" ", id='out6'),

        dcc.Slider(
            id='ta',
            min=0,
            max=60,
            step=5,
            value=20,
            marks={
                0: '0',
                15: '15',
                30: '30',
                45: '45',
                60: '60'},
            className='mb-5'
        ),
    ]
)

layout = dbc.Row([column1, column2], align="center")

@app.callback(
    Output(component_id='out1', component_property='children'),
    [Input(component_id='goals', component_property='value')]
)
def update_output_div(input_value):
    return 'Number of Goals: {}'.format(input_value)

@app.callback(
    Output(component_id='out2', component_property='children'),
    [Input(component_id='pp-opp', component_property='value')]
)
def update_output_div(input_value):
    return 'Power Play Opportunities: {}'.format(input_value)

@app.callback(
    Output(component_id='out3', component_property='children'),
    [Input(component_id='shots', component_property='value')]
)
def update_output_div(input_value):
    return 'Number of Shots: {}'.format(input_value)

@app.callback(
    Output(component_id='out4', component_property='children'),
    [Input(component_id='face-offs', component_property='value')]
)
def update_output_div(input_value):
    return 'Face Off Wins by Percent: {}%'.format(input_value)

@app.callback(
    Output(component_id='out5', component_property='children'),
    [Input(component_id='hits', component_property='value')]
)
def update_output_div(input_value):
    return 'Number of Hits: {}'.format(input_value)

@app.callback(
    Output(component_id='out6', component_property='children'),
    [Input(component_id='ta', component_property='value')]
)
def update_output_div(input_value):
    return 'Number of Takeaways: {}'.format(input_value)

