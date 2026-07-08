import os
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_FILE, override=False)


@dataclass(frozen=True, slots=True)
class Settings:
    spotify_client_id: str
    spotify_client_secret: str
    spotify_redirect_uri: str
    session_secret_key: str

    @classmethod
    def from_env(cls) -> "Settings":
        spotify_client_secret = _required_env("SPOTIFY_CLIENT_SECRET")
        return cls(
            spotify_client_id=_required_env("SPOTIFY_CLIENT_ID"),
            spotify_client_secret=spotify_client_secret,
            spotify_redirect_uri=_required_env("SPOTIFY_REDIRECT_URI"),
            session_secret_key=os.getenv("SESSION_SECRET_KEY", spotify_client_secret),
        )


def _required_env(name: str) -> str:
    value = os.getenv(name)
    if value is None or value.strip() == "":
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


@lru_cache
def get_settings() -> Settings:
    return Settings.from_env()
