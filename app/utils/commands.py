from app.core.config import settings

def build_ytdlp_command(url: str) -> list[str]:
    return [
        "yt-dlp",
        "-o",
        f"{settings.youtube_download_dir}/%(title)s.%(ext)s",
        url,
    ]
    