# Arsenal Match Tracker API ⚽️

A simple FastAPI project to track Arsenal FC matches, including match date, opponent, competition, venue, and result.

## 🚀 Features

- List all matches
- Get a match by ID
- Add a new match
- Update an existing match
- Delete a match

## 📦 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/) (for running the server)

## 🛠️ How to Run the Project

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/arsenal-fastapi.git
   cd arsenal-fastapi

2. Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

3. Install dependencies

pip install fastapi uvicorn

4. Run the server

uvicorn main:app --reload
Replace main with your Python file name if different.

5. Open in your browser

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

🧪 Example Match JSON

{
  "id": 1,
  "date": "2025-05-21",
  "opponent": "Manchester City",
  "competition": "Premier League",
  "venue": "Home",
  "arsenal_score": 3,
  "opponent_score": 2,
  "notes": "Great comeback win"
}

📌 Note
This app uses in-memory storage only — all data resets when the app restarts. For production, consider integrating a database (e.g., SQLite, PostgreSQL).

📄 License
MIT License
