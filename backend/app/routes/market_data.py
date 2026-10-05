from datetime import datetime

from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.services.market_data.service import MarketDataService

router = APIRouter(
    prefix="/api/v1/market-data",
    tags=["Market Data"]
)

@router.get("/{symbol}")
def get_market_data(
    symbol:str,
    start:datetime,
    end:datetime,
    db:Session =Depends(get_db),
):
    service = MarketDataService(db)

    data = service.fetch_historical_data(symbol=symbol,
     start=start,
     end = end,)
    service.save_historical_data(data)
    
    return {
        "symbol":symbol,
        "count":len(data),
        "data":data,
    }
