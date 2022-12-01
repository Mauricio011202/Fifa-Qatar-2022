class Match:
    def __init__(self,home_team,away_team,date,stadium_id):
        self.home_team=home_team
        self.away_team=away_team
        self.date=date
        self.stadium_id=stadium_id

    def match_register(self):
        match=self.home_team+','+self.away_team+','+str(self.date)+','+str(self.stadium_id)+'\n'
        return match
