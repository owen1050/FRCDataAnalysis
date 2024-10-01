import tbapy, pytz, datetime
from TBAGetter import TBAGetter

class TeamMethods:

    tba = 0

    def __init__(self):
        self.tba = TBAGetter().getTBA()

    def getAllTeamEvents(self, team):
        return self.tba.team_events(team, simple = True)

    def getAllTeams(self):
        return self.tba.teams()

    def getDistricts(self):
        return self.tba.districts(2024)

    def getTeamsInDist(self, dist):
        return self.tba.district_teams("2024" + dist)