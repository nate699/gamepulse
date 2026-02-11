from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"status": "GamePulse running"}

@app.get("/csgo")
def csgo_stats():
    # Public demo API – no auth required
    url = "https://api.opendota.com/api/proPlayers"
    response = requests.get(url, timeout=5)
    return {
        "players_returned": len(response.json())
    }
