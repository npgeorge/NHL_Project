# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## NHL Predictive Modeling

            Use this app to see the probability of the Boston Bruins winning their next game.

            Check out the Case Study to see behind the scenes prediction of the 2011 Stanley Cup Finals, 
            and learn how to predict the probability that they'll win their next game.

            Head over to the Process & Insights page to check out the machine learning algorithm.

            _____
            """
        ),

        dcc.Link(dbc.Button('Predict Next Game', color='primary'), href='/predictions')

        dcc.Markdown(
            """
            _____
            """
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        """
         
        """
        html.Img(src='assets/tuuk.jpg', className='img-fluid'),
    ]
)

layout = dbc.Row([column1, column2])