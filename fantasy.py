import pandas as pd

#positions: ['SG' 'PG' 'C' 'F' 'SF' 'PF' 'G']

#load in data
data = pd.read_csv('source_data/players.csv')
#drop players wiht no data on points, rebounds, assists
data.dropna(subset=['Points', 'Rebounds', 'Assists'], inplace=True)

#create subsets of data - one for each position
shooting_guards = data[data['Position'] == 'SG']
point_guards = data[data['Position'] == 'PG']
centers = data[data['Position'] == 'C']
forwards = data[data['Position'] == 'F']
small_forwards = data[data['Position'] == 'SF']
power_forwards = data[data['Position'] == 'PF']
guards = data[data['Position'] == 'G']
all_positions = {'SG':shooting_guards, 'PG':point_guards, 'C':centers, 'F':forwards, 'SF':small_forwards, 'PF':power_forwards, 'G':guards}

class Fantasy:
    def __init__(self, team_name):
        self.team_name = team_name
        self.my_team = pd.DataFrame()
        self.roster = dict()

    def draft_team(self):
        players = []
        for position in all_positions.values(): 
            players.append(position.sample())
        self.my_team = pd.concat(players)
        return self.my_team

    def create_roster(self):
        roster = dict()
        roster['Team_Name'] = self.team_name
        roster['players'] = dict(zip(self.my_team['Position'], self.my_team['Name']))
        roster['Total_Points'] = self.my_team['Points'].sum()
        roster['Total_Rebounds'] = self.my_team['Rebounds'].sum()
        roster['Total_Assists'] = self.my_team['Assists'].sum()
        self.roster = roster
        return roster

    def sub_player(self, position_sub):
        assert position_sub in ['SG', 'PG', 'C', 'F', 'SF', 'PF', 'G']

        new_pick = all_positions[position_sub].sample()
        old = self.my_team.loc[self.my_team['Position'] == position_sub].index
        self.my_team.drop(index=old, inplace=True)
        self.my_team = pd.concat([self.my_team, new_pick])
        #self.roster = create_roster()
        return self.roster
        
    
mine = Fantasy('Lakers')
mine.draft_team()
mine.create_roster()
print(mine.sub_player('PG'))