
import pandas as pd
from functools import reduce
pd.set_option('display.max_columns', 13)

super_raids = pd.read_csv('SUPER RAID_SEASON 7.csv')
super_raids.rename(columns={'points':'raid_points'}, inplace=True)
super_tackles = pd.read_csv('SUPER TACKLES_SEASON 7.csv')
super_tackles.rename(columns={'points':'tackles_points'}, inplace=True)
all_outs_inflicted = pd.read_csv('ALL-OUTS INFLICTED_SEASON 7.csv')
all_outs_inflicted.rename(columns={'points':'inflicted_points'}, inplace=True)
all_outs_conceded = pd.read_csv('ALL-OUTS CONCEDED_SEASON 7.csv')
all_outs_conceded.rename(columns={'points':'conceded_points'}, inplace=True)

all_data_frames = [super_raids,super_tackles,all_outs_inflicted,all_outs_conceded]
super_performance = reduce(lambda left,right: pd.merge(left,right,on=['Name','Matches played']), all_data_frames)

super_performance['Mean'] = super_performance.apply(lambda row: (row['raid_points']+row['tackles_points']+row['inflicted_points']-row['conceded_points'])/row['Matches played'], axis = 1)

print('Predict the team with the highest super-performance.: ', str(super_performance[super_performance['Mean'] == super_performance['Mean'].max()]['Name'].item()))
