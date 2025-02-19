from TBAGetter import TBAGetter
import numpy as np

tba = TBAGetter()
tba = tba.getTBA()

def reefToTotalCoral(reefT, reefA, l):
	tc = 0
	if(1 in l):
		tc = tc + reefT["trough"] - reefA["trough"]
	if(2 in l):

		for node in reefT["botRow"]:
			if(reefT["botRow"][node] and not reefA["botRow"][node]):
				tc = tc + 1
	if(3 in l):			
		for node in reefT["midRow"]:
			if(reefT["midRow"][node] and not reefA["midRow"][node]):
				tc = tc + 1
	
	if(4 in l):
		for node in reefT["topRow"]:
			if(reefT["topRow"][node]  and not reefA["topRow"][node]):
				tc = tc + 1
	return tc

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
eventCoralTotal = 0;
eventMatches = 0
for match in event:
	if(match.comp_level == "qm"):
		eventMatches = eventMatches + 1
		bt = match.alliances["blue"]["team_keys"]
		bs = 0 #make total blue coral
		rt = match.alliances["red"]["team_keys"]
		rs = 0 #make total red coral

		bsReefT = match.score_breakdown["blue"]["teleopReef"]
		rsReefT = match.score_breakdown["red"]["teleopReef"]

		bsReefA = match.score_breakdown["blue"]["autoReef"]
		rsReefA = match.score_breakdown["red"]["autoReef"]

		bs = reefToTotalCoral(bsReefT, bsReefA, [4,3,2,1]) 
		rs = reefToTotalCoral(rsReefT, rsReefA, [4,3,2,1])
		eventCoralTotal = eventCoralTotal + bs + rs

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

print(eventCoralTotal, eventMatches)