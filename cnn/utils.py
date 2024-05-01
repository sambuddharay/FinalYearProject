import pandas as pd
import numpy as np

def team_dictify(players: pd.DataFrame):
    team_dict = {}
    for team, team_df in players.groupby('Squad'):
        team_dict[team] = team_df
    return team_dict

def squarify(M):
    (a,b)=M.shape
    if a>b:
        padding=((0,0),(0,a-b))
    else:
        padding=((0,b-a),(0,0))
    return np.pad(M,padding,mode='constant',constant_values=0)

def pad(m):
    a=m.shape[0]
    padding = ((0,60-a),(0,0))
    return np.pad(m, padding, mode='constant', constant_values=0)

# def append_X_train(X_train: list, players: pd.DataFrame, goalkeepers: pd.DataFrame):
#     players = players[players['90s']>0]
#     players = players.replace(np.nan, 0)
#     goalkeepers = goalkeepers.replace(np.nan, 0)
#     players_compiled = players.merge(goalkeepers, how='left')
#     players_compiled = players_compiled.replace(np.nan, 0)
#     team_dict = team_dictify(players=players_compiled)
#     for team in team_dict.keys():
#         temp = team_dict[team]
#         temp = temp.drop(columns=['Player', 'Nation', 'Pos', 'Squad', 'Born'])
#         sq = squarify(temp)
#         X_train.append(sq)

def append_X_train(X_train: list, players: pd.DataFrame, goalkeepers: pd.DataFrame):
    players = players[players['90s']>0]
    players = players.replace(np.nan, 0)
    goalkeepers = goalkeepers.replace(np.nan, 0)
    players_compiled = players.merge(goalkeepers, how='left')
    players_compiled = players_compiled.replace(np.nan, 0)
    team_dict = team_dictify(players=players_compiled)
    for team in team_dict.keys():
        temp = team_dict[team]
        temp = temp.drop(columns=['Player', 'Nation', 'Pos', 'Squad', 'Born'])
        padded = pad(temp)
        X_train.append(padded)