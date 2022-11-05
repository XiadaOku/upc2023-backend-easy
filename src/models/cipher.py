from pydantic import BaseModel, Field


class EncodeModel(BaseModel):
    message: str
    rot: int = Field(ge=0, le=26)