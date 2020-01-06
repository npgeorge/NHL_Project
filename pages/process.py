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
        
            # Process

            This project derived from a curiosity about the challenges associated with predicting who will win a hockey game, and how difficult it is to predict.

            The raw data comes from the official stats collection of the NHL, which has been gathered and posted on Kaggle here. (provide link)
            
            Given the large amount of data in the data set, I decided to see if I could predict whether a certain team would win using their respective baseline target.
            The data set I chose consisted of team statistics which are given for each game played.

            """
        ),

        dcc.Markdown(
            """
        
            #### Data Cleaning & Features

            The data came in very clean, which was a plus. The original header looked like this:

            ___________insert pic_______________

            The most convoluted column was the game_id column, because each one was unique and at first glance it was a seemingly random number. 
            Many times it is tempting to want to drop a column like this due to the logical argument that high cardinality or entirely unique 
            rows of data will have low correlation to the target. Looking closer at the game_id column, the first four digits
            are clearly the "year" the game was played. The NHL does not hold any official documentation on the game_id, but I was able to 
            find an explanation by a well regarded data scientist who has worked closely with NHL data for many years (_____link_____). 
            He offered this explanation:
            
            *Game IDs*

            *The first 4 digits identify the season of the game (ie. 2017 for the 2017-2018 season). 
            The next 2 digits give the type of game, where 01 = preseason, 02 = regular season, 
            03 = playoffs, 04 = all-star. 
            The final 4 digits identify the specific game number. 
            For regular season and preseason games, this ranges from 0001 to the 
            number of games played. (1271 for seasons with 31 teams (2017 and onwards) 
            and 1230 for seasons with 30 teams). 
            For playoff games, the 2nd digit of the specific number gives the round of the playoffs, 
            the 3rd digit specifies the matchup, and the 4th digit specifies the game (out of 7).*

            This turned out to be the most important column, because I was able to use it to wrangle 3 more columns: The season, the game type (regular season or playoffs), 
            and the game number. I could now easily run models on different seasons, understand playoffs vs. regular season, and sort the data chronologically. 

            __________insert pic of wrangle function here___________

            Furthermore, with the newly created seasons column, I was able to break out the seasons into their own individual data frames. 
            This was important for a few reasons. In hockey, as in any sport, teams can change drastically from one season to the next. If a team is drastically different, say with 
            a new head coach or new star players, then it is reasonable to argue that the predictive power is less from one season to the next. On the opposite side
            of this argument is when the team doesn't change that much from one season to the next and we could argue the predictive power is more.
            Arguments aside, this could be proven through further analysis. 

            Upon breaking the seasons out, I found some interesting differences in the data set. The 2012 to 2013 season showed significantly less data as compared to the other years.

            -___pic of shapes of the seasons____

            I kept the smaller season because it could only help the model. 

            ### Boston Bruins

            Next, I broke out the data frame to consist of only one team, the Boston Bruins. If a model works for one team, it should work broadly for all others. 
            I did this to simplify the problem. Using the 'team_id' column, and referencing the NHL API, I was able to find the Bruins team ID and filter that into the 
            original data frame to create the new one, consisting of only the Boston Bruins games from the 2011 season until now.

            ##### Baseline

            ________pic of baseline calculation________

            The baseline target for the model was 57.266%. This is the winning percentage for the Boston Bruins since 2011.

            ### Machine Learning Model

            With the data frames setup, I proceeded to set up the model. Using scikitlearn's train_test_split method, I used an 80/20 split for train and test.
            I then split the training data again 80/20 into train and validation sets.

            I then setup my target and features columns. Using the 'won' column as my target, and dropping it from the data frame. 

            Arranged into a features and target vector. 

            Built a pipeline using the XGBoost method.

            ____pic of pipeline___

            ##### Test Accuracy

            I was able to achieve a result better than the baseline target, with a test Accuracy Score of 76.073%

            ### Case Study (New Page)



            """
        ),
        
        dcc.Markdown(" ", id='out1'),

    ],
)

layout = dbc.Row([column1])