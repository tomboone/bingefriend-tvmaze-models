"""SQLAlchemy model for a season."""
import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String, Date, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bingefriend_tvmaze_models.models.base import Base

if TYPE_CHECKING:
    from bingefriend_tvmaze_models.models.episode import Episode
    from bingefriend_tvmaze_models.models.network import Network
    from bingefriend_tvmaze_models.models.show import Show
    from bingefriend_tvmaze_models.models.webchannel import WebChannel


class Season(Base):
    """SQLAlchemy model for a season."""
    __tablename__ = "seasons"

    # Attributes
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    number: Mapped[int] = mapped_column(Integer, nullable=False)
    name: Mapped[str] | None = mapped_column(Text)
    network_id: Mapped[int] | None = mapped_column(ForeignKey("networks.id"), nullable=True)
    webchannel_id: Mapped[int] | None = mapped_column(ForeignKey("webchannels.id"), nullable=True)
    summary: Mapped[str] | None = mapped_column(Text)
    show_id: Mapped[int] = mapped_column(ForeignKey("shows.id"), nullable=False)

    # Relationships - referenced in this model
    show: Mapped[Show] = relationship(back_populates="seasons")
    network: Mapped[Network] = relationship(back_populates="seasons")
    webchannel: Mapped[WebChannel] = relationship(back_populates="seasons")

    # Relationships - referencing this model
    episodes: Mapped[list[Episode]] = relationship(back_populates="season", cascade="all, delete-orphan")
