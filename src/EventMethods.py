import tbapy, pytz, datetime
from TBAGetter import TBAGetter

class EventMethods:

    tba = 0

    def __init__(self):
        self.tba = TBAGetter().getTBA()

    def getAllTeamEvents(self, team):
        return self.tba.team_events(team, simple = True)

    def getAllEventsFromYear(self, year):
        return self.tba.events(year)

    def getAllMatchesFromYear(self, year):
        events = self.getAllEventsFromYear(year)
        return events

    def getTeamMatchesFromEvents(self, events, team):
        ret = {}
        for event in events:
            tempMatches = self.tba.team_matches(team, event, simple = True)
            ret[event] = tempMatches
        return ret

    def getAllMatchesFromEvents(self, events):
        ret = {}
        for event in events:
            tempMatches = self.tba.event_matches(event)
            ret[event] = tempMatches
            print(event)
        return ret

    def filterEventsByMatches(self, events):
        ret = []
        for event in events:
            if len(events[event]) > 0:
                ret.append(event)
        return ret

    def getAllEventsFromYearWithMatches(self, year):
        events = self.getAllEventsFromYear(year)
        return self.filterEventsByMatches(events)

    def getEventDataFromEvents(self, events):
        ret = {}
        for event in events:
            tempMatches = self.tba.event_matches(event)
            ret[event] = tempMatches
        return ret

    def getEventData(self, event):
        return self.tba.event(event)

    def getMatchesDayFromEvent(self, event):
        try:
            oneEvent = self.getEventData(event)
            matches = self.getEventDataFromEvents([event])
            event = matches[event]
            match = event[0]

            matchEpoch = match["time"]
            matchDatetime = datetime.datetime.fromtimestamp(matchEpoch)
            offsetStr = datetime.datetime.now(pytz.timezone(oneEvent["timezone"])).strftime('%z')
            offset = int(offsetStr[1:])/100
            if(offsetStr[0] == "+"):
                pass
            else:
                offset = offset * -1

            ret = {}
            for m in event:
                try:
                    matchEpoch = m["time"]
                    correctedEpoch = ((offset + 5) * 60 * 60) + matchEpoch
                    tempDatetime = datetime.datetime.fromtimestamp(correctedEpoch)
                    day = tempDatetime.day
                    if(day in ret):
                        ret[day] = ret[day] + 1
                    else:
                        ret[day] = 1
                except:
                    pass
            return ret
        except:
            return {0:0}

    def getMatchesDayFromEventNoPass(self, event):
        
        oneEvent = self.getEventData(event)
        matches = self.getEventDataFromEvents([event])
        event = matches[event]
        match = event[0]

        matchEpoch = match["time"]
        matchDatetime = datetime.datetime.fromtimestamp(matchEpoch)
        offsetStr = datetime.datetime.now(pytz.timezone(oneEvent["timezone"])).strftime('%z')
        offset = int(offsetStr[1:])/100
        if(offsetStr[0] == "+"):
            pass
        else:
            offset = offset * -1

        ret = {}
        for m in event:
            try:
                matchEpoch = m["time"]
                correctedEpoch = ((offset + 5) * 60 * 60) + matchEpoch
                tempDatetime = datetime.datetime.fromtimestamp(correctedEpoch)
                day = tempDatetime.day
                if(day in ret):
                    ret[day] = ret[day] + 1
                else:
                    ret[day] = 1
            except:
                pass
        return ret

    def getWinnersOfEvent(self, event):
        winners = []
        oneEvent = self.tba.event_awards(event)
        for award in oneEvent:
            if(award["award_type"] == 1):
                for teams in award["recipient_list"]:
                    winners.append(teams["team_key"])
        return winners

    def getAllTeams(self):
        return self.tba.teams()
em = EventMethods()
teams = em.getAllTeams()
for teamCode in teams:
    try:
        team = teamCode["key"][3:]
        events = em.getAllTeamEvents(int(team))
        for i in range(len(events) - 1):

                teamId = "frc" + str(team)
                if(teamId in em.getWinnersOfEvent(events[i]["key"]) and teamId in em.getWinnersOfEvent(events[i+1]["key"])):
                    if(events[i]["key"][0:4] == events[i+1]["key"][0:4]):
                        print(team, events[i]["key"][0:4], events[i]["key"], events[i+1]["key"])
    except:
        pass