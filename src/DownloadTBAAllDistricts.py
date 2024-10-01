from TeamMethods import TeamMethods
import pickle

tm = TeamMethods()

fileName = "allDistTeams"


outputData = {}

dists = tm.getDistricts()

for dist in dists:
	distName = dist['abbreviation']
	print(distName)
	

file = open(fileName, 'wb+')
pickle.dump(outputData, file)
file.close()

