from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models import MarketData

class MarketDataRepository:
    def __init__(self,db:Session):
        self.db = db
    def save_many(self,records:list[MarketData]):
        self.db.add_all(records)
        self.db.commit()
    
    def get_by_sybmol(self,symbol:str)->list[MarketData]:
        statement = (
            select(MarketData)
            .where(MarketData.symbol == symbol)
            .order_by(MarketData.timestamp)
        )
        result = self.db.execute(statement)
        return list(result.scalars().all())