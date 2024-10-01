import pickle


file = open('allTeamsMatches', 'rb')
data = pickle.load(file)
file.close()


globalTPW = {}
globalTPA = {}

teamsG = []

for team in data:
    print(team)
    teamsG.append(team)
    teamsPlayedWith = {}
    teamsPlayedAgainst = {}
    
    for event in data[team]:

        thisEvent = data[team][event]
        for match in thisEvent:
            red = match['alliances']['red']['team_keys']
            blue = match['alliances']['blue']['team_keys']
            tmp = []
            for teamCode in red:
                try:
                    tmp.append(int(teamCode[3:]))
                except:
                    pass
            red = tmp

            tmp = []
            for teamCode in blue:
                try:
                    tmp.append(int(teamCode[3:]))
                except:
                    pass
            blue = tmp
            if(team in red):
                for redTeam in red:
                    teamsPlayedWith[redTeam] = teamsPlayedWith.get(redTeam, 0) + 1
                for blueTeam in blue:
                    teamsPlayedAgainst[blueTeam] = teamsPlayedAgainst.get(blueTeam, 0) + 1
            if(team in blue):
                for redTeam in red:
                    teamsPlayedAgainst[redTeam] = teamsPlayedAgainst.get(redTeam, 0) + 1
                for blueTeam in blue:
                    teamsPlayedWith[blueTeam] = teamsPlayedWith.get(blueTeam, 0) + 1

    globalTPW[team] = teamsPlayedWith
    globalTPA[team] = teamsPlayedAgainst

file = open("allWith", 'wb+')
pickle.dump(globalTPW, file)
file.close()

file = open("allAgainst", 'wb+')
pickle.dump(globalTPA, file)
file.close()





