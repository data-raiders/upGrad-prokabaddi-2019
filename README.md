# upGrad Pro Kabaddi League hackathon by The Data Raiders

## Tools and technologies used:

* Selenium was used to scrape data from the official Pro Kabaddi website
* Python was used to write the prediction logic using frameworks - numpy, pandas, matplotlib

## Task 1: Predict the winner of the tournament.

### Prediction: _Dabang Delhi K.C._

### How we arrived at the predictions -

* We scraped the team standings and match schedule data from the officail Pro Kabaddi website.
* We looked at the individual games played by each team and for every win we added constant points and for every tie the constant points were split between both the teams and for a loss no points were added. This was done for the combination of all matches playes. Then based on these points the eliminator teams were selected and again based on the scores the semi-finals and the finals teams were selected and points were assigned. We then summed up all the points and the team with the highest points was selected.

## Task 2: Predict the top team in the points table after the completion of the league matches.

### Prediction: _Dabang Delhi K.C._

### How we arrived at the predictions -

* We scraped the team standings and match schedule data from the officail Pro Kabaddi website.
* We looked at the individual league matches played by each team and for every win we added constant points and for every tie the constant points were split between both the teams and for a loss no points were added. This was done for the combination of all matches playes and we summed up all the points based on the previous step and the team with the highest points was selected.

## Task 3: Predict the team with the highest points for successful raids.

### Prediction: _Dabang Delhi K.C._

### How we arrived at the predictions -

* We scraped the raids data for each team from the official Pro Kabaddi website.
* We took the avarage (mean) successful raids of each team in each match and then we selected the team with the highest average.

## Task 4: Predict the team with the highest points for successful tackles.

### Prediction: _Puneri Paltan_

### How we arrived at the predictions -

* We scraped the tackles data for each team from the official Pro Kabaddi website.
* We took the avarage (mean) successful tackles of each team in each match and then we selected the team with the highest average.

## Task 5: Predict the team with the highest super-performance total.

### Prediction: _Patna Pirates_

### How we arrived at the predictions -

* We scraped the Super tackles, Super raids, all-out inflicted, all-out cenceded data from the official Pro Kabaddi website.
* The equation specifed in the problem statement was used to derive this prediction.

## Task 6: Predict the player with the highest SUCCESSFUL RAID percentage.

### Prediction: _PAWAN KUMAR SEHRAWAT_  

### How we arrived at the predictions -

* We scraped the player and their respective raids data from the official Pro Kabaddi website.
* We found the average successful raids for each player and the player with the highest successful raids percentage from the data was chosen. NOTE: We only included players that had a minimum of at least 100 raids as the successful raid percentage increased for players with only a few raids.

## Task 7: Predict the player with the highest SUCCESSFUL TACKLE percentage.

### Prediction: _NITESH KUMAR_

### How we arrived at the predictions -

* We scraped the player and their respective tackles data from the official Pro Kabaddi website.
* We found the average successful tackles for each player and the player with the highest successful tackles percentage from the data was chosen. NOTE: We only included players that had a minimum of at least 50 tackles as the successful tackle percentage increased for players with only a few tackles.
