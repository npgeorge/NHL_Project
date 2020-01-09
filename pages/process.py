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
            # Boston Bruins & Machine Learning
            _____
            """
        ),

        html.Img(src='assets/bs_logo.png', className='img-fluid'),
        dcc.Markdown(
            """
            _____
        
            ## Overview

            This project derived from a curiosity about the challenges associated with predicting who will win a hockey game, and how difficult it is to predict.

            The raw data comes from the official stats collection of the NHL, which has been gathered and posted on Kaggle here: 
            __**[NHL Game Data](https://www.kaggle.com/martinellis/nhl-game-data#table_relationships.JPG)**__.
            
            Given the large amount of data in the data set, I decided to see if I could predict whether a certain team would win using their respective baseline targets.
            The data set I chose consisted of team statistics which are given for each game played. The problem is binary classification, win or lose. 

            """
        ),

        dcc.Markdown(
            """
        
            #### Data Cleaning & Features

            The data came in very clean, which was a plus. The original header looked like this:

            _____

            """
        ),

        html.Img(src='assets/df_header.png', className='img-fluid'),

        dcc.Markdown(
            """
            _____

            The most convoluted column was the game_id column, because each one was unique and at first glance I could not decode the meaning of these numbers. 
            Many times it is tempting to want to drop a column like this due to the logical argument that high cardinality or entirely unique 
            rows of data will have low correlation to the target. Looking closer at the game_id column, the first four digits
            are clearly the "year" the game was played. The NHL does not hold any official documentation on the game_id, but I was able to 
            find an explanation by a well regarded data scientist who has worked closely with NHL data for many years.
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
            the 3rd digit specifies the matchup, and the 4th digit specifies the game (out of 7).* - __**[NHL API Documentation](https://gitlab.com/dword4/nhlapi)**__

            This turned out to be the most important column, because I was able to use it to wrangle 3 more columns: The season, the game type (regular season or playoffs), 
            and the game number. I could now easily run models on different seasons, understand playoffs vs. regular season, and sort the data chronologically. 
            
            _____

            """
        ),

        html.Img(src='assets/df_wrangle.png', className='img-fluid'),
        
        dcc.Markdown(
            """
            _____

            Furthermore, with the newly created seasons column, I was able to break out the seasons into their own individual data frames. 
            This was important for a few reasons. In hockey, as in any sport, teams can change drastically from one season to the next. If a team is drastically different, say with 
            a new head coach or new star players, then it is reasonable to argue that the predictive power is less from one season to the next. Conversely, when the team doesn't change that much from one season to the next, we could argue the predictive power increases.
            Arguments aside, this could be proven through further analysis. 

            Upon breaking the seasons out, I found some interesting differences in the data set. The 2012 to 2013 season showed significantly less data as compared to the other years.
            Although this smaller season was an anomaly, I kept the data because it could only help the model. 

            _____

            """
        ),

        html.Img(src='assets/df_seasons_shape.png', className='img-fluid'),

        dcc.Markdown(
            """
            _____

            ## Process & Insights

            Next, I broke out the data frame to consist of only one team, the Boston Bruins. If a model works for one team, it should work broadly for all others. 
            I did this to simplify the problem. Using the 'team_id' column, and referencing the NHL API, I was able to find the Bruins team ID and filter that into the 
            original data frame to create a new data frame, consisting of only the Boston Bruins games from the 2010 season until now.

            #### Baseline

            The baseline target for the model was 57.266%. This is the winning percentage for the Boston Bruins since 2010.

            _____
            """
        ),

        html.Img(src='assets/df_baseline.png', className='img-fluid'),

        dcc.Markdown(
            """
            _____

            #### Model

            With the data frames set up, I proceeded to set up the model. Using scikitlearn's train_test_split method, I used an 80/20 split for train and test.
            I then split the training data again 80/20 into train and validation sets.
            Next, I setup my target and features columns. I used the 'won' column as my target, and dropped it from the data frame. After a running a permutation
            importance, I dropped the columns that were not contributing to the prediction to simplifiy the model.   

            Finally, I built a pipeline using the XGBoost method. I optimized the amount of n-estimators that yielded the highest result. 

            _____
            """
        ),

        html.Img(src='assets/df_pipeline.png', className='img-fluid'),

        dcc.Markdown(
            """
            _____

            #### Train, Validation, & Test Accuracy

            The data sets all had similar results as shown in the picture above. Most notably, 
            I was able to achieve a result better than the baseline target, with a *Test Accuracy Score of 76.073%*.
            


            ## Visualizations & Data Leakage

            The following visualizations explore the effect of the 'goals' column on the data set. Due to data leakage concerns
            and high correlation to the target, I wanted to take an in depth look at the permutation importances, the Eli 5 random
            shuffle, and the ROC AUC Scores. I also added some PDP plots I thought were interesting. 

            """
        ),

        dcc.Markdown(
            """

            #### Permutation Importance

            The permutation importance highlighted possible data leakage for the model. The "goals" column was contributing 4x as much 
            as any other feature to the model, however, this did not automatically mean there was data leakage. The train, validation, and test
            data sets did not indicate a model that was overfitting the data. These scores, as noted above, all had similar results.

            On the left is the model run with goals left in the data set, on the right is run with goals *removed* from the data set.  

            _____
            """
        ),
        html.Img(src='assets/perm_importance.png', style={'height':'470px', 'width':'450px'}),
        html.Img(src='assets/perm_importance_wo_goals.png', style={'height':'470px', 'width':'450px'}),

        dcc.Markdown(
            """
            *Data frame with "goals" column on the left, data frame without "goals" column on the right. Interesting to note the shuffle in feature importances.*
            _____

            #### Eli 5

            The Eli 5 scores also played an important role in the investigation into the possible data leakage. After randomly shuffling and relating the variables, 
            the result was the same. The "goals" column still appeared to be the most important feature, yet we can not conclusively label it as data leakage. 

            _____
            """
        ),
        html.Img(src='assets/eli5_with_goals.png', style={'height':'275px', 'width':'375px'}),
        html.Img(src='assets/eli5_without_goals.png', style={'height':'275px', 'width':'350px'}),

        dcc.Markdown(
            """
            *Data frame with "goals" column on the left, data frame without "goals" column on the right. Again, interesting to note the shuffle in feature importances.*
            _____

            #### ROC/AUC Scores

            The final step I took in determining whether or not the "goals" column was causing data leakage was to look at the ROC/AUC scores. 

            From Wikipedia: "The ROC curve is created by plotting the true positive rate (TPR) against the false positive rate (FPR) at various threshold settings."
            The higher the ROC/AUC score, the better. 

            The ROC/AUC score for the data frame with the "goals" column left in was *0.8298*.

            The ROC/AUC score for the data frame with the "goals" column removed was *0.5049*.
            This suggests a naive majority class baseline, and we can conclude that we should keep the "goals" column in the data frame.

            _____
            """
        ),
        html.Img(src='assets/roc_with_goals.png', style={'height':'300px', 'width':'350px'}),
        html.Img(src='assets/roc_no_goals.png', style={'height':'300px', 'width':'350px'}),

        dcc.Markdown(
            """
            _____
            #### Conclusion on Data Leakage

            Train, Validate, and Test scores dropped significantly after removing the "goals" column, understandably so.
            The amount of goals a team scores should have the biggest impact on whether they win a game or not, which is why I decided to leave
            this column in the data set.
            _____
            """
        ),

        html.Img(src='assets/xgb_no_goals_2.png', className='img-fluid'),

        dcc.Markdown(
            """
            *XG Boost Model with the "goals" column removed.*
            _____

            #### PDP Plots

            Next, I explored some partial dependency plots for the official data frame, including the "goals" column. 

            The face off win percentage sees a steep increase in dependency in the 45-52 percent range. Faceoffs won at critical points
            in the game, such as in the attacking zone, have a significant impact on winning games. 

            _____
            """
        ),
        html.Img(src='assets/face_off_pdp.png', className='img-fluid'),

        dcc.Markdown(
            """
            _____

            Lastly, I wanted to see how hits and shots related to each other.

            The Bruins dominate games and have their best chances of winning when they achieve 33 hits or more. Surprisingly there was 
            an optimal number of shots, the closer to 25 shots the better.

            _____
            """
        ),
        
        html.Img(src='assets/shots_hits_pdp.png', className='img-fluid'),

        dcc.Markdown(
            """
            _____

            ## Conclusion

            In conclusion, my algorithm boasts a 76 percent Test Accuracy score for the Boston Bruins winning a game.

            A true test of this model could be used on games happening during the 2019-2020 year.

            Checkout the Case Study for an example on how to use this model. 

            """
        ),

    ],
)

layout = dbc.Row([column1])