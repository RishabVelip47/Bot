from datetime import datetime

from sqlalchemy.orm import Session

from app.database.models import MarketData
from app.database.repositories.market_data_repository import MarketDataRepository
from app.services.market_data.models import OHLCV
from app.services.market_data.validator import validate_ohlcv
from app.services.market_data.yfinance_provider import YFinanceProvider


class MarketDataService:

    def __init__(self, db: Session):
        self.provider = YFinanceProvider()
        self.repository = MarketDataRepository(db)

    def get_market_data(
        self,
        symbol: str,
        start: datetime,
        end: datetime,
    ) -> list[OHLCV]:

        stored_data = self.repository.get_by_symbol_and_range(
            symbol=symbol,
            start=start,
            end=end,
        )

        if stored_data:
            print(
                f"DATA SOURCE: PostgreSQL | "
                f"{symbol} | {len(stored_data)} records"
            )
            return self._to_ohlcv(stored_data)

        print(f"DATA SOURCE: Yahoo Finance | {symbol}")

        data = self.provider.get_historical_data(
            symbol=symbol,
            start=start,
            end=end,
        )

        data = validate_ohlcv(data)

        self.save_historical_data(data)

        stored_data = self.repository.get_by_symbol_and_range(
            symbol=symbol,
            start=start,
            end=end,
        )

        return self._to_ohlcv(stored_data)

    def save_historical_data(
        self,
        data: list[OHLCV],
    ) -> None:

        records = [
            MarketData(
                symbol=row.symbol,
                timestamp=row.timestamp,
                open=row.open,
                high=row.high,
                low=row.low,
                close=row.close,
                volume=row.volume,
            )
            for row in data
        ]

        self.repository.save_many(records)

    def get_stored_data(
        self,
        symbol: str,
    ) -> list[OHLCV]:

        records = self.repository.get_by_symbol(symbol)

        return self._to_ohlcv(records)

    def _to_ohlcv(
        self,
        records: list[MarketData],
    ) -> list[OHLCV]:

        return [
            OHLCV(
                timestamp=record.timestamp,
                symbol=record.symbol,
                open=record.open,
                high=record.high,
                low=record.low,
                close=record.close,
                volume=record.volume,
            )
            for record in records
        ]