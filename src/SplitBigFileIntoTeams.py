import pickle

with open('allTeamsMatches1', 'rb') as handle:
    data = pickle.load(handle)

for team in data:
    file = open('teamMatches\\'+str(team), 'wb+')
    pickle.dump(data[team], file)
    file.close()