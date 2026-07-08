from fastapi import FastAPI

from config import get_settings

app = FastAPI(title="Spotify Live Lyrics API")
app.state.settings = get_settings()


@app.get("/")
def read_root():
    return {"status": "backend running"}
