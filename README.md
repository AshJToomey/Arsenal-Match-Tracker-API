# Arsenal Match Tracker API ⚽️

A FastAPI-based REST API for tracking Arsenal FC matches — results, scores, opponents, competitions, and more!

## 🚀 Features

- CRUD operations for Arsenal matches
- Match filtering by opponent or competition
- Derived field for match result: Win, Loss, or Draw
- UUID-based unique match IDs
- In-memory storage for simplicity
- OpenAPI & Swagger UI out-of-the-box



## 🧪 Example Match Data

{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "date": "2025-05-21",
  "opponent": "Manchester City",
  "competition": "Premier League",
  "venue": "Home",
  "arsenal_score": 3,
  "opponent_score": 2,
  "notes": "Great comeback win"
}

## 📦 Tech Stack

- FastAPI for building the API

- Pydantic for data validation

- UUID for safe and unique match IDs


  "date": "2025-05-21",
  "opponent": "Manchester City",
  "competition": "Premier League",
  "venue": "Home",
  "arsenal_score": 3,
  "opponent_score": 2,
  "notes": "Great comeback win"
}

## 📦 Requirements

pip install fastapi uvicorn

## 🧑‍💻 How to Run

uvicorn arsenal_tracker:app --reload

Then visit:

👉 http://127.0.0.1:8000/docs (Swagger UI)

👉 http://127.0.0.1:8000/redoc (ReDoc UI)

## 🔮 Future Improvements
- Add persistent storage (SQLite or PostgreSQL)

- Add user authentication

- Deploy via Railway/Render

- Add support for player stats per match

## 📜 License
MIT License – feel free to use and contribute!
