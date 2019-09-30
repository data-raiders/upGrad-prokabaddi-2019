import pandas as pd

successful_tackles = pd.read_csv('SUCCESSFUL TACKLES_SEASON 7.csv')

successful_tackles['Mean'] = successful_tackles.apply(lambda row: row['points']/ row['Matches played'], axis = 1) 
  
print('Predict the team with the highest points for successful tackles.: ', str(successful_tackles[successful_tackles['Mean'] == successful_tackles['Mean'].max()]['Name'].item()))


#print(successful_tackles)