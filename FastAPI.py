from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class ArsenalMatch(BaseModel):
    id: int
    date: str             # e.g. "2025-05-21"
    opponent: str         # e.g. "Manchester City"
    competition: str      # e.g. "Premier League"
    venue: str            # "Home" or "Away"
    arsenal_score: int
    opponent_score: int
    notes: Optional[str] = None  # e.g. "Great comeback win"

matches: List[ArsenalMatch] = []

@app.get("/matches", response_model=List[ArsenalMatch])
def get_matches():
    return matches

@app.get("/matches/{match_id}", response_model=ArsenalMatch)
def get_match(match_id: int):
    for match in matches:
        if match.id == match_id:
            return match
    raise HTTPException(status_code=404, detail="Match not found")

@app.post("/matches", response_model=ArsenalMatch)
def create_match(match: ArsenalMatch):
    matches.append(match)
    return match

@app.put("/matches/{match_id}", response_model=ArsenalMatch)
def update_match(match_id: int, updated_match: ArsenalMatch):
    for index, match in enumerate(matches):
        if match.id == match_id:
            matches[index] = updated_match
            return updated_match
    raise HTTPException(status_code=404, detail="Match not found")

@app.delete("/matches/{match_id}")
def delete_match(match_id: int):
    for index, match in enumerate(matches):
        if match.id == match_id:
            matches.pop(index)
            return {"message": "Match deleted"}
    raise HTTPException(status_code=404, detail="Match not found")
