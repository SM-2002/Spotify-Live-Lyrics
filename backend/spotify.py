import httpx
from fastapi import HTTPException
from models.spotify import CurrentTrackResponse

SPOTIFY_CURRENT_TRACK_URL = (
    "https://api.spotify.com/v1/me/player/currently-playing"
)

async def get_current_track(access_token: str):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(
            SPOTIFY_CURRENT_TRACK_URL,
            headers=headers
        )
    
    # no song is currently playing
    if response.status_code == 204:
        return {
            "is_playing": False,
            "message": "No track is currently playing."
        }
    
    # unauthorized
    if response.status_code == 401:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized - The request requires user authentication or, if the request included authorization credentials, authorization has been refused for those credentials."
        )
    
    # forbidden
    if response.status_code == 403:
        raise HTTPException(
            status_code=403,
            detail="Forbidden - The server understood the request, but is refusing to fulfill it."
        )
    
    if response.status_code != 200:
        return HTTPException(
            status_code=response.status_code,
            detail=response.text,
        )
    
    data = response.json()
    print(f'data: {data}')

    item = data.get("item")
    if not item:
        return CurrentTrackResponse(
            is_playing=False,
            song=None,
            artist=None,
            album=None,
            album_image=None,
            progress_ms=0,
            duration_ms=0,
        )

    album = item.get("album", {})
    images = album.get("images", [])

    return CurrentTrackResponse(
        is_playing=data.get("is_playing", False),
        song=item.get("name"),
        artist=", ".join(
            artist.get("name", "")
            for artist in item.get("artists", [])
        ),
        album=album.get("name"),
        album_image=images[0]["url"] if images else None,
        progress_ms=data.get("progress_ms", 0),
        duration_ms=item.get("duration_ms", 0),
    )

    