from datetime import datetime
from pydantic import BaseModel

class OHLCV(BaseModel):
    timestamp: datetime
    symbol:str

    open:float
    high:float
    low:float
    close:float

    volume:float