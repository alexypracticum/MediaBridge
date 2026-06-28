from app.core.logging import logger

class YoutubeService:

    def download(self, url: str):
        
        logger.info("Download requested: %s", url)

        return {
            "status": "success",
            "message": "Download scheduled"
        }
    