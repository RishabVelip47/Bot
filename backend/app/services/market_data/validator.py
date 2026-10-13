from app.services.market_data.models import OHLCV


def validate_ohlcv(data: list[OHLCV]) -> list[OHLCV]:
    if not data:
        raise ValueError("No market data was returned by the provider.")

    for row in data:
        if row.open <= 0 or row.high <= 0:
            raise ValueError(
                f"Invalid OHLC prices for {row.symbol} at {row.timestamp}"
            )

        if row.low <= 0 or row.close <= 0:
            raise ValueError(
                f"Invalid OHLC prices for {row.symbol} at {row.timestamp}"
            )

        if row.volume < 0:
            raise ValueError(
                f"Negative volume for {row.symbol} at {row.timestamp}"
            )

        if row.high < row.low:
            raise ValueError(
                f"High is lower than low for {row.symbol} at {row.timestamp}"
            )

        if row.high < max(row.open, row.close):
            raise ValueError(
                f"High is below open or close for {row.symbol} at {row.timestamp}"
            )

        if row.low > min(row.open, row.close):
            raise ValueError(
                f"Low is above open or close for {row.symbol} at {row.timestamp}"
            )

    return data