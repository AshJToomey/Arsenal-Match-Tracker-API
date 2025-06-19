from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

app = FastAPI(title="Arsenal Match Tracker API", version="1.0")

class ArsenalMatch(BaseModel):
    id: UUID
    date: str             # e.g. "2025-05-21"
    opponent: str         # e.g. "Manchester City"
    competition: str      # e.g. "Premier League"
    venue: str            # "Home" or "Away"
    arsenal_score: int
    opponent_score: int
    notes: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "date": "2025-05-21",
                "opponent": "Manchester City",
                "competition": "Premier League",
                "venue": "Home",
                "arsenal_score": 3,
                "opponent_score": 2,
                "notes": "Great comeback win"
            }
        }

class ArsenalMatchOut(ArsenalMatch):
    result: str

matches: List[ArsenalMatch] = []

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Arsenal Match Tracker API"}

@app.get("/matches", response_model=List[ArsenalMatchOut], tags=["Matches"])
def get_matches(
    opponent: Optional[str] = Query(None, description="Filter by opponent name"),
    competition: Optional[str] = Query(None, description="Filter by competition"),
    skip: int = 0,
    limit: int = 10
):
    filtered = matches
    if opponent:
        filtered = [m for m in filtered if m.opponent.lower() == opponent.lower()]
    if competition:
        filtered = [m for m in filtered if m.competition.lower() == competition.lower()]

    def add_result(match: ArsenalMatch) -> ArsenalMatchOut:
        result = (
            "Win" if match.arsenal_score > match.opponent_score else
            "Loss" if match.arsenal_score < match.opponent_score else
            "Draw"
        )
        return ArsenalMatchOut(**match.dict(), result=result)

    return [add_result(m) for m in filtered[skip : skip + limit]]

@app.get("/matches/{match_id}", response_model=ArsenalMatchOut, tags=["Matches"])
def get_match(match_id: UUID):
    for match in matches:
        if match.id == match_id:
            result = (
                "Win" if match.arsenal_score > match.opponent_score else
                "Loss" if match.arsenal_score < match.opponent_score else
                "Draw"
            )
            return ArsenalMatchOut(**match.dict(), result=result)
    raise HTTPException(status_code=404, detail="Match not found")

@app.post("/matches", response_model=ArsenalMatch, tags=["Matches"])
def create_match(match: ArsenalMatch):
    if any(existing.id == match.id for existing in matches):
        raise HTTPException(status_code=400, detail="Match with this ID already exists")
    matches.append(match)
    return match

@app.put("/matches/{match_id}", response_model=ArsenalMatch, tags=["Matches"])
def update_match(match_id: UUID, updated_match: ArsenalMatch):
    for index, match in enumerate(matches):
        if match.id == match_id:
            matches[index] = updated_match
            return updated_match
    raise HTTPException(status_code=404, detail="Match not found")

@app.delete("/matches/{match_id}", tags=["Matches"])
def delete_match(match_id: UUID):
    for index, match in enumerate(matches):
        if match.id == match_id:
            matches.pop(index)
            return {"message": "Match deleted"}
    raise HTTPException(status_code=404, detail="Match not found")
