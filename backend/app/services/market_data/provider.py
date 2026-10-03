from abc import ABC ,abstractmethod
from datetime import datetime

from app.services.market_data.models import OHLCV

class MarketDataProvider(ABC):
    @abstractmethod
    def get_historical_data(
        self,
        symbol:str,
        start:datetime,
        end:datetime
    )-> list[OHLCV]:pass