
import pandas as pd



player_raids = pd.read_csv('player_raids.csv')


player_raids_more = player_raids[player_raids['total'] >=  100]

print('Predict the player with the highest SUCCESSFUL RAID percentage without considering min raids.: ', str(player_raids[player_raids['avg'] == player_raids['avg'].max()]['Name'].item()))

print('Predict the player with the highest SUCCESSFUL RAID percentage with above raids100 .: ', str(player_raids_more[player_raids_more['avg'] == player_raids_more['avg'].max()]['Name'].item()))
