
from dataclasses import dataclass
from datetime import datetime

@dataclass
class DownloadJob:
    id: str
    url: str
    status: str
    created_at: datetime

    progress: float = 0.0

    title: str | None = None
    filepath: str | None = None
    error: str | None = None
