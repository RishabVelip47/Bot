from datetime import date

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models import MarketDataCoverage


class MarketDataCoverageRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_coverage(
        self,
        symbol: str,
        start_date: date,
        end_date: date,
    ) -> list[MarketDataCoverage]:

        statement = (
            select(MarketDataCoverage)
            .where(
                MarketDataCoverage.symbol == symbol,
                MarketDataCoverage.start_date <= start_date,
                MarketDataCoverage.end_date >= end_date,
            )
            .order_by(MarketDataCoverage.start_date)
        )

        result = self.db.execute(statement)

        return list(result.scalars().all())

    def save_coverage(
        self,
        symbol: str,
        start_date: date,
        end_date: date,
        records_count: int,
    ) -> None:

        record = MarketDataCoverage(
            symbol=symbol,
            start_date=start_date,
            end_date=end_date,
            records_count=records_count,
        )

        self.db.add(record)
        self.db.flush()