from app.services.market_data.models import OHLCV

def validate_ohlcv(data:list[OHLCV])->list[OHLCV]:
    valid_data = []
    for row in data:
        if row.open <= 0:
            continue
        if row.high <= 0:
            continue
        if row.low <= 0:
            continue
        if row.close <=0:
            continue
        if row.high<row.low:
            continue
        if row.volume < 0:
            continue
        valid_data.append(row)

    return valid_data
