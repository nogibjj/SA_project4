from fastapi import FastAPI
import uvicorn
import fantasy

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Draft 2022."}

@app.get("/draft/{team_name}")
async def draft_team(team_name):
    global my_team
    my_team = fantasy.Fantasy(team_name)
    my_team.draft_team()
    my_team.create_roster()
    return my_team.roster

@app.get("/sub/{position_to_sub}")
async def sub_players(position_to_sub):
    my_team.sub_player(position_to_sub)
    return my_team.roster

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")