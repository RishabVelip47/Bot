from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models import MarketData


class MarketDataRepository:

    def __init__(self, db: Session):
        self.db = db

    def save_many(self, records: list[MarketData]) -> None:

        for record in records:

            existing = self.db.execute(
                select(MarketData).where(
                    MarketData.symbol == record.symbol,
                    MarketData.timestamp == record.timestamp,
                )
            ).scalar_one_or_none()

            if existing:
                continue

            self.db.add(record)

        self.db.commit()

    def get_by_symbol(
        self,
        symbol: str,
    ) -> list[MarketData]:

        statement = (
            select(MarketData)
            .where(MarketData.symbol == symbol)
            .order_by(MarketData.timestamp)
        )

        result = self.db.execute(statement)

        return list(result.scalars().all())