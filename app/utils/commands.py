def build_ytdlp_command(url: str) -> list[str]:
    return [
        "yt-dlp",
        url,
    ]
    