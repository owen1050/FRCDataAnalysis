from matchAnal2025 import matchAnal2025

ma = matchAnal2025()


def printCOPRs(event):
	#to add, climb, fouls, mobility
	l1A = ma.getCoralOPRFromEvent(event, [1], True)
	l2A = ma.getCoralOPRFromEvent(event, [2], True)
	l3A = ma.getCoralOPRFromEvent(event, [3], True)
	l4A = ma.getCoralOPRFromEvent(event, [4], True)
	l1T = ma.getCoralOPRFromEvent(event, [1], False)
	l2T = ma.getCoralOPRFromEvent(event, [2], False)
	l3T = ma.getCoralOPRFromEvent(event, [3], False)
	l4T = ma.getCoralOPRFromEvent(event, [4], False)
	oprs = ma.getOPRFromEvent(event)
	coralAuto = ma.coprFromMatchResult(event, "autoCoralPoints")
	coralTele = ma.coprFromMatchResult(event, "teleopCoralPoints")
	algaeScored = ma.coprFromMatchResult(event, "wallAlgaeCount")
	algaeNet = ma.coprNetMinusOponentProcessor(event)
	climbs = ma.getClimbCounts(event)
	park = climbs[0]
	shallow = climbs[1]
	deep = climbs[2]
	egPercent = climbs[3]
	movePer = ma.getAutoMoveCounts(event)
	fouls = ma.getFouls(event)
	
	tl = l1A[0]

	outputData = [["Team", "OPR", "Auto Coral PTS", "L1A COPR", "L2A COPR", "L3A COPR", "L4A COPR", "Teleop Coral PTS", "L1T COPR", "L2T COPR", "L3T COPR", "L4T COPR", "Processor Algae", "Net Algae", "Park Percent", "Shallow Percent", "Deep Percent", "End Game Percent", "Auto Move Percent", "foul points"]]

	for i in range(len(tl)):
		row = []
		row.append(tl[i][3:])
		row.append(oprs[1][i])
		row.append(coralAuto[1][i])
		row.append(l1A[1][i].item())
		row.append(l2A[1][i].item())
		row.append(l3A[1][i].item())
		row.append(l4A[1][i].item())
		row.append(coralTele[1][i])
		row.append(l1T[1][i].item())
		row.append(l2T[1][i].item())
		row.append(l3T[1][i].item())
		row.append(l4T[1][i].item())
		row.append(algaeScored[1][i])
		row.append(algaeNet[1][i])
		row.append(park[i])
		row.append(shallow[i])
		row.append(deep[i])
		row.append(egPercent[i])
		row.append(movePer[i])
		row.append(fouls[1][i])
		outputData.append(row)


	for team in outputData:
		for i in team:
			print(i, end = "\t")
		print()


printCOPRs("2025week0")
