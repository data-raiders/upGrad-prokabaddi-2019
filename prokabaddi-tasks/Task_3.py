import pandas as pd

successful_raids = pd.read_csv('SUCCESSFUL RAIDS_SEASON 7.csv')

successful_raids['Mean'] = successful_raids.apply(lambda row: row['points']/ row['Matches played'], axis = 1) 
  
print('Predict the team with the highest points for successful raids.: ', str(successful_raids[successful_raids['Mean'] == successful_raids['Mean'].max()]['Name'].item()))


#print(successful_raids)