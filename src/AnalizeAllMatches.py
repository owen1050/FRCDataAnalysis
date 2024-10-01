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


saveStr = "\t"
print("", end= "\t")
for team in teamsG:
    saveStr = saveStr + str(team) + "\t"
    print(team, "\t", end = "")

with open("output.txt", "a+") as text_file:
    text_file.write(saveStr)


for teama in teamsG:
    saveStr = ""
    team1 = int(teama)
    saveStr = saveStr + "\n" + str(teama) + "\t"
    print(teama)
    #print(teama, end = "\t")
    for teamb in teamsG:
        team2 = int(teamb)
        #print(globalTPW[team1].get(team2,0), end = "\t")
        saveStr = saveStr + str(globalTPW[team1].get(team2,0)) + "\t"

    with open("output.txt", "a+") as text_file:
        text_file.write(saveStr)






