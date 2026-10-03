from datetime import datetime
from app.services.market_data.models import OHLCV
from app.services.market_data.validator import validate_ohlcv
from app.services.market_data.yfinance_provider import YFinanceProvider

class MarketDataService:
    def __init__(self):
        self.provider = YFinanceProvider()
    def get_historical_data(
        self,
        symbol:str,
        start:datetime,
        end:datetime
    )->list[OHLCV]:
    
        data = self.provider.get_historical_data(symbol =symbol,start=start,end=end)

        return validate_ohlcv(data)
        
