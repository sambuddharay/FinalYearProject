import numpy as np
import pandas as pd

url = 'https://raw.githubusercontent.com/sambuddharay/FinalYearProject/main/model1/feature_coefficients.csv'
feature_coef = pd.read_csv(url)

def player_score(df: pd.DataFrame):
    cols = ['Tackles Tkl', 'Tackles TklW', 'Tackles Def 3rd', 'Tackles Mid 3rd', 'Tackles Att 3rd', 'Challenges Tkl', 'Challenges Att', 'Challenges Tkl%', 'Challenges Lost', 'Blocks Blocks', 'Blocks Sh', 'Blocks Pass', 'Int', 'Tkl+Int', 'Clr', 'Err', 'SCA SCA', 'SCA SCA90', 'SCA Types PassLive', 'SCA Types PassDead', 'SCA Types TO', 'SCA Types Sh', 'SCA Types Fld', 'SCA Types Def', 'GCA GCA', 'GCA GCA90', 'GCA Types PassLive', 'GCA Types PassDead', 'GCA Types TO', 'GCA Types Sh', 'GCA Types Fld', 'GCA Types Def', 'Performance CrdY', 'Performance CrdR', 'Performance 2CrdY', 'Performance Fls', 'Performance Fld', 'Performance Off', 'Performance Crs', 'Performance Int', 'Performance TklW', 'Performance PKwon', 'Performance PKcon', 'Performance OG', 'Performance Recov', 'Aerial Duels Won', 'Aerial Duels Lost', 'Aerial Duels Won%', 'Total Cmp', 'Total Att', 'Total Cmp%', 'Total TotDist', 'Total PrgDist', 'Short Cmp', 'Short Att', 'Short Cmp%', 'Medium Cmp', 'Medium Att', 'Medium Cmp%', 'Long Cmp', 'Long Att', 'Long Cmp%', 'Ast', 'xAG', 'Expected xA', 'Expected A-xAG', 'KP', '1/3', 'PPA', 'CrsPA', 'PrgP', 'Playing Time MP', 'Playing Time Min', 'Playing Time Mn/MP', 'Playing Time Min%', 'Playing Time 90s', 'Starts Starts', 'Starts Mn/Start', 'Subs Subs', 'Subs Mn/Sub', 'Subs unSub', 'Team Success PPM', 'Team Success onG', 'Team Success onGA', 'Team Success +/-', 'Team Success +/-90', 'Team Success (xG) onxG', 'Team Success (xG) onxGA', 'Team Success (xG) xG+/-', 'Team Success (xG) xG+/-90', 'Touches Touches', 'Touches Def Pen', 'Touches Def 3rd', 'Touches Mid 3rd', 'Touches Att 3rd', 'Touches Att Pen', 'Touches Live', 'Take-Ons Att', 'Take-Ons Succ', 'Take-Ons Succ%', 'Take-Ons Tkld', 'Take-Ons Tkld%', 'Carries Carries', 'Carries TotDist', 'Carries PrgDist', 'Carries PrgC', 'Carries 1/3', 'Carries CPA', 'Carries Mis', 'Carries Dis', 'Receiving Rec', 'Receiving PrgR', 'Standard Gls', 'Standard Sh', 'Standard SoT', 'Standard SoT%','Standard Sh/90', 'Standard SoT/90', 'Standard G/Sh', 'Standard G/SoT', 'Standard Dist', 'Standard FK', 'Standard PK', 'Standard PKatt', 'Expected xG', 'Expected npxG', 'Expected npxG/Sh', 'Expected G-xG', 'Expected np:G-xG']
    score = 0
    for col in cols:
        score+=df[col]*feature_coef[col]
    return score

def goalkeeper_score(df1: pd.DataFrame, df2: pd.DataFrame):
    if df1['Pos'].str=="GK":
        name = df1['Player']
        return goalkeeper_score_generate(df2, name) 
    else:
        return 0

def goalkeeper_score_generate(df: pd.DataFrame, name: str):
    df = df.loc[df['Player']==name]
    cols = ['Performance GA', 'Performance GA90', 'Performance SoTA', 'Performance Saves', 'Performance Save%', 'Performance W', 'Performance D', 'Performance L', 'Performance CS', 'Performance CS%', 'Penalty Kicks PKatt', 'Penalty Kicks PKA', 'Penalty Kicks PKsv', 'Penalty Kicks PKm', 'Goals GA', 'Goals PKA', 'Goals FK', 'Goals CK', 'Goals OG', 'Expected PSxG', 'Expected PSxG/SoT', 'Expected PSxG+/-', 'Expected /90', 'Launched Cmp', 'Launched Att', 'Launched Cmp%', 'Passes Att (GK)', 'Passes Thr', 'Passes Launch%', 'Passes AvgLen', 'Goal Kicks Att', 'Goal Kicks Launch%', 'Goal Kicks AvgLen', 'Crosses Opp', 'Crosses Stp', 'Crosses Stp%', 'Sweeper #OPA', 'Sweeper #OPA/90', 'Sweeper AvgDist']
    gk_score = 0
    for col in cols:
        gk_score+=df[col]*feature_coef[col]
    return gk_score