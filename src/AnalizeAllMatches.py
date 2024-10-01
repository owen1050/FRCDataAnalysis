import pickle

data = {}
for i in range(10000):
    try:
        file = open('teamMatches' + str(i), 'rb')
        data[i] = pickle.load(file)
        file.close()
    except:
        pass


globalTPW = {}
globalTPA = {}


for team in data:
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

print("", end= "\t")
for team in teamsG:
    print(team, "\t", end = "")

for teama in teamsG:
    team1 = int(teama)
    print("")
    print(teama, end = "\t")
    for teamb in teamsG:
        team2 = int(teamb)
        print(globalTPW[team1].get(team2,0), end = "\t")





