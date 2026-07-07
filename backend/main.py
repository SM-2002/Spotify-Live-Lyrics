from fastapi import FastAPI

app = FastAPI(title="Spotify Live Lyrics API")


@app.get("/")
def read_root():
    return {"status": "backend running"}
