from pydantic import BaseModel

class CurrentTrackResponse(BaseModel):
    is_playing: bool
    song: str | None
    artist: str | None
    album: str | None
    album_image: str | None
    progress_ms: int
    duration_ms: int