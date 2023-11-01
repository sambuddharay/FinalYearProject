import pandas as pd
import numpy as np

def ind_to_team_stats_conv(df: pd.DataFrame):
    cols = ['90s','Gls','Sh','SoT','SoT%','Sh/90','SoT/90','G/Sh','G/SoT','Dist','FK','PK','PKatt','xG','npxG','npxG/Sh','G-xG','np:G-xG']
    res = pd.DataFrame(columns=cols)
    for key in df.keys():
        team = df[key]
        arr=team[cols].sum()
        weight_sum = team['90s'].sum()
        arr['Sh/90'] = arr['Sh']/weight_sum
        arr['SoT/90'] = arr['SoT']/weight_sum
        arr['SoT%'] = arr['SoT']*100/arr['Sh']
        res = res.append(arr, ignore_index=True)
    return res