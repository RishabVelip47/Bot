from datetime import datetime
from sqlalchemy.orm import Session
from app.database.models import MarketData
from app.database.repositories.market_data_repsoitory import (MarketDataRepository,)
from app.services.market_data.models import OHLCV
from app.services.market_data.validator import validate_ohlcv
from app.services.market_data.yfinance_provider import YFinanceProvider

class MarketDataService:
    def __init__(self,db:Session):
        self.provider = YFinanceProvider()
        self.repsoitory = MarketDataRepository(db)

    def get_historical_data(
        self,
        symbol:str,
        start:datetime,
        end:datetime
    )->list[OHLCV]:
    
        data = self.provider.get_historical_data(symbol =symbol,start=start,end=end)

        return validate_ohlcv(data)
    
    def save_historical_data(self,data:list[OHLCV],)->None:
        records=[MarketData(symbol = row.symbol,
                timestamp = row.timestamp,
                open = row.open,
                high = row.high,
                low = row.low,
                close = row.close,
                volume = row.volume)
                for row in data
                ]
        self.repsoitory.save(records)

    def get_stored_data(
        self,
        symbol:str,

    )->list[OHLCV]:
        return self.repsoitory.get_by_sybmol(symbol)