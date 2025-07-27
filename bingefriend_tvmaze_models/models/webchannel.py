"""Web Channel Model"""
from typing import TYPE_CHECKING

from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bingefriend_tvmaze_models.models.base import Base

if TYPE_CHECKING:
    from bingefriend_tvmaze_models.models.season import Season
    from bingefriend_tvmaze_models.models.show import Show


class WebChannel(Base):
    """Represents a web channel"""
    __tablename__ = "webchannels"

    # Attributes
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    name: Mapped[str] | None = mapped_column(String(255))
    country_code: Mapped[str] | None = mapped_column(String(255))

    # Relationships - referencing this model
    seasons: Mapped[list[Season]] = relationship(back_populates="webchannel")
