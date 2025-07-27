"""SQLAlchemy model for an episode."""
import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String, Date, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bingefriend_tvmaze_models.models.base import Base

if TYPE_CHECKING:
    from bingefriend_tvmaze_models.models.season import Season
    from bingefriend_tvmaze_models.models.show import Show


class Episode(Base):
    """SQLAlchemy model for an episode."""
    __tablename__ = "episodes"

    # Attributes
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    name: Mapped[str] | None = mapped_column(Text)
    number: Mapped[int] | None = mapped_column(Integer)
    type: Mapped[str] | None = mapped_column(String(50))
    airstamp: Mapped[datetime.datetime] | None = mapped_column(DateTime(timezone=True))
    runtime: Mapped[int] | None = mapped_column(Integer)
    summary: Mapped[str] | None = mapped_column(Text)
    season_id: Mapped[int] = mapped_column(ForeignKey("seasons.id"), nullable=False)
    show_id: Mapped[int] = mapped_column(ForeignKey("shows.id"), nullable=False)

    # Relationships - referenced in this model
    season: Mapped[Season] = relationship(back_populates="episodes")
    show: Mapped[Show] = relationship(back_populates="episodes")
