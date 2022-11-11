import logic.fantasy as fantasy

bball_team = fantasy.Fantasy("HoneyBees")
assert bball_team.team_name == "HoneyBees"
assert bball_team.my_team.empty
assert len(bball_team.roster) == 0

bball_team.draft_team()
assert bball_team.my_team["Position"].nunique() == 7

bball_team.create_roster()
assert len(bball_team.roster) == 5
assert list(bball_team.roster.keys()) == [
    "Team_Name",
    "players",
    "Avg_Points",
    "Avg_Rebounds",
    "Avg_Assists",
]

print("ALL TESTS PASSED")
