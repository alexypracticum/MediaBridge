from pydantic import BaseModel, HttpUrl

class DownloadRequest(BaseModel):
    url: str
    
class DownloadResponse(BaseModel):
    status: str
    message: str