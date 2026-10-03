from datetime import datetime
from app.services.market_data.service  import MarketDataService

service = MarketDataService()
data = service.get_historical_data(symbol="Reliance.NS",
        start=datetime(2025,1,1),
        end=datetime(2025,2,1))
for row in data[:5]:
    print(row)