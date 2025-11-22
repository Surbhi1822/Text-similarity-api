from pydantic import BaseModel

class TextPair(BaseModel):
    text1: str
    text2: str

class SingleText(BaseModel):
    text: str
