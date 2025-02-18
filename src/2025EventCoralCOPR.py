from TBAGetter import TBAGetter
import numpy as np

tba = TBAGetter()
tba = tba.getTBA()

eventStr = "2025week0"
event = tba.event_matches(eventStr)
teams = tba.event_teams(eventStr)

teamList = []

for team in teams:
	teamList.append(team.key);

#team 1 in match, team 2 in match, team 3 in match
a = []
b = []
#score
for match in event:
	if(match.comp_level == "qm"):
		bt = match.alliances["blue"]["team_keys"]
		bs = 0 #make total blue coral
		rt = match.alliances["red"]["team_keys"]
		rs = 0 #make total red coral

		aRow = []

		for team in teamList:
			if(team in bt):
				aRow.append(1)
			else:
				aRow.append(0)
		a.append(aRow)
		b.append(bs)

		aRow = []

		for team in teamList:
			if(team in rt):
				aRow.append(1)
			else:
				aRow.append(0)
		a.append(aRow)
		b.append(rs)

a = np.array(a)
b = np.array(b)


x = np.linalg.lstsq(a,b)

x = x[0]

for i in range(len(teamList)):
	print(teamList[i], "\t", x[i])