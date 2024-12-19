from TeamMethods import TeamMethods
import pickle

tm = TeamMethods()

fileName = "allDistTeams"


outputData = {}

dists = tm.getDistricts()

for dist in dists:
	distName = dist['abbreviation']
	print(distName)
	teams = tm.getTeamsInDist(dist['abbreviation'])
	thisDistTeams = []
	for team in teams:
		thisDistTeams.append(team['team_number'])

	outputData[distName] = thisDistTeams

file = open(fileName, 'wb+')
pickle.dump(outputData, file)
file.close()

