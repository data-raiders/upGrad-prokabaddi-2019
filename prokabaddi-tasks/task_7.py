
import pandas as pd



player_tackles = pd.read_csv('player_tackles.csv')

player_tackles['avg'] = player_tackles.apply(lambda row: row['avg'].replace("%",""), axis = 1) 

print(player_tackles)
player_tackles_more = player_tackles[player_tackles['total'] >=  50]

print('Predict the player with the highest SUCCESSFUL TACKLE percentage without considering min tackles.: ', str(player_tackles[player_tackles['avg'] == player_tackles['avg'].max()]['Name'].item()))

print('Predict the player with the highest SUCCESSFUL TACKLE percentage with above 50 tackles.: ', str(player_tackles_more[player_tackles_more['avg'] == player_tackles_more['avg'].max()]['Name'].item()))
