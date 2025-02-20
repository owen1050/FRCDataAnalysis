from TBAGetter import TBAGetter
import numpy as np

#12.44 for 1258

class matchAnal2025:
	tba = TBAGetter()
	tba = tba.getTBA()

	def reefToTotalCoral(self, reefT, l):
		tc = 0
		if(1 in l):
			tc = tc + reefT["trough"]
		if(2 in l):

			for node in reefT["botRow"]:
				if(reefT["botRow"][node]):
					tc = tc + 1
		if(3 in l):			
			for node in reefT["midRow"]:
				if(reefT["midRow"][node]):
					tc = tc + 1
		
		if(4 in l):
			for node in reefT["topRow"]:
				if(reefT["topRow"][node]):
					tc = tc + 1
		return tc

	def getCoralOPRFromEvent(self, event, levels, auto):
		eventStr = event
		event = self.tba.event_matches(eventStr)
		teams = self.tba.event_teams(eventStr)

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
				if(auto):
					bsReefT = match.score_breakdown["blue"]["autoReef"]
					rsReefT = match.score_breakdown["red"]["autoReef"]

				bs = self.reefToTotalCoral(bsReefT, levels)
				rs = self.reefToTotalCoral(rsReefT, levels)

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

		return (teamList, x)

	def getOPRFromEvent(self, event):
		eventStr = event
		event = self.tba.event_matches(eventStr)
		teams = self.tba.event_teams(eventStr)

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

				bs = match.alliances["blue"]["score"]
				rs = match.alliances["red"]["score"]

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

		return (teamList, x)

	def coprFromMatchResult(self, event, result):
		eventStr = event
		event = self.tba.event_matches(eventStr)
		teams = self.tba.event_teams(eventStr)

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

				bs = match.score_breakdown["blue"][result]
				rs = match.score_breakdown["red"][result]

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

		return (teamList, x)

	def coprNetMinusOponentProcessor(self, event):
		eventStr = event
		event = self.tba.event_matches(eventStr)
		teams = self.tba.event_teams(eventStr)

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

				bs = match.score_breakdown["blue"]["netAlgaeCount"] - match.score_breakdown["red"]["wallAlgaeCount"]
				rs = match.score_breakdown["red"]["netAlgaeCount"] - match.score_breakdown["blue"]["wallAlgaeCount"]

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

		return (teamList, x)

	def getClimbCounts(self, event):
		eventStr = event
		event = self.tba.event_matches(eventStr)
		teams = self.tba.event_teams(eventStr)

		parkList = {}
		shallowList = {}
		deepList = {}
		numMatches = {}

		for team in teams:
			parkList[team.key] = 0
			shallowList[team.key] = 0
			deepList[team.key] = 0
			numMatches[team.key] = 0


		#team 1 in match, team 2 in match, team 3 in match

		eventCoralTotal = 0;
		eventMatches = 0
		for match in event:
				
			bt = match.alliances["blue"]["team_keys"]
			rt = match.alliances["red"]["team_keys"]
			#"endGameRobot1"
			
			for i in range(3):
				climbState  = match.score_breakdown["blue"]["endGameRobot" + str(i+1)]
				if(climbState == "Parked"):
					parkList[bt[i]] = parkList[bt[i]] + 1
				if(climbState == "DeepCage"):
					deepList[bt[i]] = deepList[bt[i]] + 1
				if(climbState == "ShallowCage"):
					shallowList[bt[i]] = shallowList[bt[i]] + 1
				numMatches[bt[i]] = numMatches[bt[i]] + 1

			for i in range(3):
				climbState  = match.score_breakdown["red"]["endGameRobot" + str(i+1)]
				if(climbState == "Parked"):
					parkList[rt[i]] = parkList[rt[i]] + 1
				if(climbState == "DeepCage"):
					deepList[rt[i]] = deepList[rt[i]] + 1
				if(climbState == "ShallowCage"):
					shallowList[rt[i]] = shallowList[rt[i]] + 1
				numMatches[rt[i]] = numMatches[rt[i]] + 1

		ret = {}
		sl = []
		dl = []
		pl = []
		tl = []

		for team in numMatches:
			s = shallowList[team] / numMatches[team]

			d = deepList[team] / numMatches[team]

			p = parkList[team] / numMatches[team]
			sl.append(s)
			dl.append(d)
			pl.append(p)
			tl.append(s+d+p)
		return [pl, sl, dl, tl]

	def getAutoMoveCounts(self, event):
		eventStr = event
		event = self.tba.event_matches(eventStr)
		teams = self.tba.event_teams(eventStr)

		moveList = {}
		numMatches = {}

		for team in teams:
			moveList[team.key] = 0
			numMatches[team.key] = 0


		#team 1 in match, team 2 in match, team 3 in match

		eventCoralTotal = 0;
		eventMatches = 0
		for match in event:
				
			bt = match.alliances["blue"]["team_keys"]
			rt = match.alliances["red"]["team_keys"]
			#"endGameRobot1"
			
			for i in range(3):
				moveState  = match.score_breakdown["blue"]["autoLineRobot" + str(i+1)]
				if(moveState == "Yes"):
					moveList[bt[i]] = moveList[bt[i]] + 1
				numMatches[bt[i]] = numMatches[bt[i]] + 1

			for i in range(3):
				moveState  = match.score_breakdown["red"]["autoLineRobot" + str(i+1)]
				if(moveState == "Yes"):
					moveList[rt[i]] = moveList[rt[i]] + 1
				numMatches[rt[i]] = numMatches[rt[i]] + 1

		ml = []

		for team in numMatches:
			m = moveList[team] / numMatches[team]

			ml.append(m)
		return ml

	def getFouls(self, event):
		eventStr = event
		event = self.tba.event_matches(eventStr)
		teams = self.tba.event_teams(eventStr)

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

				bs = match.score_breakdown["red"]["foulPoints"]
				rs = match.score_breakdown["blue"]["foulPoints"]

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

		return (teamList, x)