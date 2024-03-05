from pydantic import BaseModel


class ImageMetadata(BaseModel):
    # image_id: UUID
    # processing_state: ProcessingState = ProcessingState.NOT_READY
    # receive_timestamp: float | None  # unix timestamp
    # codec_name: str | None
    # image_quality: ImageQuality | None
    # labeling: str = "NO LABEL"
    # hash: str | None = None

    some_var: str
