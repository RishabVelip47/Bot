from datetime import datetime
import yfinance as yf
from app.services.market_data.models import OHLCV
from app.services.market_data.provider import MarketDataProvider

class YFinanceProvider(MarketDataProvider):
    def get_historical_data(
    self,
    symbol:str,
    start:datetime,
    end:datetime)->list[OHLCV]:
    
        ticker = yf.Ticker(symbol)
        data = ticker.history(start = start,end= end,interval="1d")
        results=[]
        for timestamp,row in data.iterrows():
            results.append(OHLCV(timestamp=timestamp.to_pydatetime(),symbol=symbol,
            open = float(row["Open"]),
            high = float(row["High"]),
            low = float(row["Low"]),
            close = float(row["Close"]),
            volume = float(row["Volume"])))
        return results
               