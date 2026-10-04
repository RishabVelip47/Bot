from datetime import datetime
from sqlalchemy import(
    String,DateTime,Float,BigInteger,UniqueConstraint
)
from sqlalchemy.orm import Mapped,mapped_column
from app.database.connection import Base

class MarketData(Base):
    __tablename__ = "market_data"
    id:Mapped[int] = mapped_column(
        primary_key =True,
        autoincrement = True
    )
    symbol:Mapped[str]=mapped_column(
        String(30),
        nullable=False,
        index=True
    )
    timestamp:Mapped[datetime]=mapped_column(
        DateTime,
        nullable=False
    )
    open:Mapped[float]=mapped_column(
        Float,
        nullable=False
    )
    high:Mapped[float]=mapped_column(
        Float,
        nullable=False
    )
    low:Mapped[float]=mapped_column(
        Float,
        nullable=False
    )
    close:Mapped[float]=mapped_column(
        Float,
        nullable=False
    )
    volume:Mapped[float]=mapped_column(
        Float,
        nullable=False
    )
    __table_args__=(
        UniqueConstraint(
            "symbol",
            "timestamp",
            name = "uq_market_data_symbol_timestamp"),
    )