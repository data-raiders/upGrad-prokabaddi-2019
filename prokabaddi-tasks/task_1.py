import pandas as pd

fixtures_results = pd.read_csv('schedule-fixtures-results.csv')
standings = pd.read_csv('standings.csv')

for ind in standings.index: 
    teamTo= standings['team'][ind]
    for j in range(ind+1, standings.shape[0]-1) :
        teamFrom = standings['team'][j]
        teamAFilter = fixtures_results[fixtures_results['Team A'].str.match(teamTo+"|"+teamFrom)]
        teamBFilter = teamAFilter[teamAFilter['Team B'].str.match(teamTo+"|"+teamFrom)]
        teamBFilterNonYtp = teamBFilter[teamBFilter['Win Team'] != 'YTP']
        if teamBFilterNonYtp.shape[0] == 2:
            continue
        winTeam = teamBFilterNonYtp.iloc[0, 2]
        if winTeam == 'Match Ti':
            ptsFrom = int(standings.loc[standings['team'] == teamFrom, 'Pts'])
            ptsTo = int(standings.loc[standings['team'] == teamTo, 'Pts'])
            standings[standings['team'] == teamFrom] = standings[standings['team'] == teamFrom].replace(ptsFrom, ptsFrom + 1)
            standings[standings['team'] == teamTo] = standings[standings['team'] == teamTo].replace(ptsTo, ptsTo + 1)
            continue
        pts = int(standings.loc[standings['team'] == winTeam, 'Pts'])
        standings[standings['team'] == winTeam] = standings[standings['team'] == winTeam].replace(pts, pts + 2)
print('Winning team: ', str(standings[standings['Pts'] == standings['Pts'].max()]['team'].item()))