from datetime import datetime
from app.database.connection import SessionLocal
from app.database.models import MarketData 
from app.database.repositories.market_data_repsoitory import (MarketDataRepository ,)
db = SessionLocal()

try:
    repsoitory = MarketDataRepository(db)

    record = MarketData(symbol = "Test",
                        timestamp = datetime(2026,1,1),
                        open = 100.0,
                        high = 110.0,
                        low = 95.0 ,
                        close = 105.0,
                        volume = 100000, )

    repsoitory.save_many([record])
    print("Market Data saved successfully!")

    stored = repsoitory.get_by_sybmol("Test")
    for row in stored:
        print(row.symbol,
        row.timestamp,
        row.close)
finally:
    db.close()