from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "MediaBridge"
    app_version: str = "0.1.0"
    media_root: str = "/media"
    log_level: str = "INFO"

    # Задаём папку сохранения по умолчанию
    youtube_download_dir: str = "data/downloads/youtube"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

settings = Settings()

