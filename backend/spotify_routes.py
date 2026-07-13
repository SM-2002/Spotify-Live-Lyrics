from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Request

from spotify import get_current_track
from models.spotify import CurrentTrackResponse

router = APIRouter(
    prefix="/spotify",
    tags=["Spotify"],
)

@router.get(
    "/current-track",
    response_model=CurrentTrackResponse,
)
async def current_track(request: Request):
    token = request.session.get("spotify_token")

    if token is None:
        raise HTTPException(
            status_code=401,
            detail="User not logged in."
        )

    access_token = token["access_token"]

    return await get_current_track(access_token)