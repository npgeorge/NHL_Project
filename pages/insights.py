# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            # Boston Bruins 2011 Stanley Cup Finals


            """
        ),

        html.Img(src='assets/yass.jpeg', className='img-fluid'),

        dcc.Markdown(
            """
            _____
        
            ## Case Study

            The purpose of this case study is to show an approach to using and filling out the parameters on the prediction page. 
            
            In 2011, the Boston Bruins won the Stanley Cup Final in an exciting game 7 series, along with a strong season and playoff run. 
            This simple case study filters the original NHL data frame down to the Bruins playoffs games at the end of the 2010-2011 season.
            The objective was to see if the machine learning model would have predicted that the Bruins would win Game 7 of the Stanley Cup Finals. 

            #### Filtering the Data Frame 

            I created a function to filter the entire NHL Data Frame down to the playoffs of the 2010-2011 season. Leveraging the "game_id" split function
            I built for the initial analysis, I only needed to pass three conditions into the data frame. Then I sorted the columns by the feature engineered
            "game_number" column to list the games in chronological order.
            _____
            """
        ),

        html.Img(src='assets/cs_condition.png', className='img-fluid'),

        dcc.Markdown(
            """
            _____

            Next, I dropped the last game in newly created data frame, Game 7 of the Stanley Cup Finals.

            After dropping the final game, I calculated the means of each column. 
            The means of each column could then be used to input into the machine learning model.
            _____
            """
        ),

        html.Img(src='assets/cs_means.png', className='img-fluid'),

        dcc.Markdown(
            """
            _____
            ## Prediction

            The model delivered a probability of 54% that the Bruins would win Game 7 of the Stanley Cup Finals, based on their playoff performance metrics.
            Although this score isn't overly confident, it's worth keeping in mind that a binary classification problem can only have one of two outcomes,
            therefore 54% probable could also be interpreted as a *WIN.* Go B's!
            
            _____
            """
        ),

        html.Img(src='assets/cs_prediction.png', className='img-fluid'),

    ],
)

layout = dbc.Row([column1])