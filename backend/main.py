from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from auth import router as auth_router
from config import get_settings

settings = get_settings()
app = FastAPI(title="Spotify Live Lyrics API")
app.state.settings = settings
app.add_middleware(SessionMiddleware, secret_key=settings.session_secret_key)
app.include_router(auth_router)


@app.get("/")
def read_root():
    return {"status": "backend running"}
