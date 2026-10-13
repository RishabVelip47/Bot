"""Add market data coverage

Revision ID: 1296e599ff52
Revises: 4b606a72c0a5
Create Date: 2026-10-13 10:40:22.810400

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '1296e599ff52'
down_revision: Union[str, Sequence[str], None] = '4b606a72c0a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "market_data_coverage",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("symbol", sa.String(length=30), nullable=False),
        sa.Column("start_date", sa.Date(), nullable=False),
        sa.Column("end_date", sa.Date(), nullable=False),
        sa.Column("records_count", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "symbol",
            "start_date",
            "end_date",
            name="uq_market_data_coverage_range",
        ),
    )
    op.create_index(
        "ix_market_data_coverage_symbol",
        "market_data_coverage",
        ["symbol"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index(
        "ix_market_data_coverage_symbol",
        table_name="market_data_coverage",
    )
    op.drop_table("market_data_coverage")