import pytest

from app.services.market_data.models import OHLCV
from app.services.market_data.validator import validate_ohlcv


def make_record(**overrides):
    values = {
        "timestamp": "2025-02-03T00:00:00",
        "symbol": "RELIANCE.NS",
        "open": 100.0,
        "high": 110.0,
        "low": 95.0,
        "close": 105.0,
        "volume": 1000.0,
    }
    values.update(overrides)
    return OHLCV(**values)


def test_valid_data_passes():
    data = [make_record()]
    assert validate_ohlcv(data) == data


def test_empty_data_is_rejected():
    with pytest.raises(ValueError, match="No market data"):
        validate_ohlcv([])


def test_high_below_low_is_rejected():
    data = [make_record(high=90.0)]

    with pytest.raises(ValueError, match="High is lower than low"):
        validate_ohlcv(data)


def test_negative_volume_is_rejected():
    data = [make_record(volume=-1.0)]

    with pytest.raises(ValueError, match="Negative volume"):
        validate_ohlcv(data)