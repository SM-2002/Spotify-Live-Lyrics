from functools import lru_cache

from authlib.integrations.starlette_client import OAuth
from fastapi import APIRouter, Request

from config import get_settings

SPOTIFY_AUTHORIZE_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_SCOPES = "user-read-currently-playing user-read-playback-state"

router = APIRouter(prefix="/auth", tags=["auth"])


@lru_cache
def get_oauth() -> OAuth:
    settings = get_settings()
    oauth = OAuth()
    oauth.register(
        name="spotify",
        client_id=settings.spotify_client_id,
        client_secret=settings.spotify_client_secret,
        authorize_url=SPOTIFY_AUTHORIZE_URL,
        access_token_url=SPOTIFY_TOKEN_URL,
        client_kwargs={"scope": SPOTIFY_SCOPES},
    )
    return oauth


@router.get("/login")
async def login(request: Request):
    settings = get_settings()
    spotify = get_oauth().create_client("spotify")
    return await spotify.authorize_redirect(request, settings.spotify_redirect_uri)


@router.get("/callback")
async def callback(request: Request):
    spotify = get_oauth().create_client("spotify")
    token = await spotify.authorize_access_token(request)

    # Store the token in the user's session
    request.session["spotify_token"] = token

    return {
        "status": "spotify authorization successful",
        "message": "Token stored successfully."
    }
