from datetime import datetime

from fastapi import APIRouter
from app.services.market_data.service import MarketDataService

router = APIRouter(
    prefix="/api/v1/market-data",
    tags=["Market Data"]
)
service = MarketDataService()
@router.get("/{symbol}")
def get_market_data(
    symbol:str,
    start:datetime,
    end:datetime
):
    data = service.get_historical_data(symbol=symbol,
     start=start,
     end = end)

    return {
        "symbol":symbol,
        "count":len(data),
        "data":data
    }
