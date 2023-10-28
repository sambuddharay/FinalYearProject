import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
#from sklearn.compose import ColumnTransformer

def best_playmaker_score(df: pd.DataFrame)->None:
    pm = df.filter(     ['Name',
                        'Club',
                        'Nationality',
                        'Position',
                        'Age',
                        'Matches',
                        'Starts',
                        'Mins',
                        'Goals',
                        'Assists',
                        'Passes_Attempted',
                        'Perc_Passes_Completed',
                        'Penalty_Goals',
                        'Penalty_Attempted',
                        'xG',
                        'xA',
                        'Yellow_Cards',
                        'Red_Cards',
                        'Accurate_Passes',
                        'Inaccurate_Passes'], axis=1)
    
    mms = MinMaxScaler()
    pm[['Passes_Attempted', 'Accurate_Passes', 'Inaccurate_Passes']] = mms.fit_transform(pm[['Passes_Attempted', 'Accurate_Passes', 'Inaccurate_Passes']])
    
    pm = pm.assign(Playmaker_Score = lambda pm: pm.Goals*0.5 + pm.Assists*1 + pm.Passes_Attempted*1 + pm.xG*1 + pm.xA*1.5 - pm.Yellow_Cards*0.1 - pm.Red_Cards*0.3 + pm.Accurate_Passes*1 - pm.Inaccurate_Passes*0.05)
    pm = pm.assign(Time_Weighted_Playmaker_Score = lambda pm: pm.Playmaker_Score*1000/pm.Mins)
    
    print(pm[['Name','Club','Nationality','Position','Age','Matches','Playmaker_Score']].sort_values(by=['Playmaker_Score'], ascending=False).head(20))
    print(pm[['Name','Club','Nationality','Position','Age','Matches','Playmaker_Score', 'Time_Weighted_Playmaker_Score']].sort_values(by=['Time_Weighted_Playmaker_Score'], ascending=False).head(20))