"""SQLAlchemy model for a show."""
import datetime
from typing import TYPE_CHECKING

from sqlalchemy import String, Integer, Date, ForeignKey, Text
from sqlalchemy.ext.associationproxy import AssociationProxy, association_proxy
from sqlalchemy.orm import mapped_column, Mapped, relationship

from bingefriend_tvmaze_models.models.base import Base

if TYPE_CHECKING:
    from bingefriend_tvmaze_models.models.episode import Episode
    from bingefriend_tvmaze_models.models.season import Season
    from bingefriend_tvmaze_models.models.show_genre import ShowGenre


class Show(Base):
    """SQLAlchemy model for a show."""
    __tablename__ = "shows"

    # Attributes
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    type: Mapped[str] = mapped_column(String(255), nullable=False)
    language: Mapped[str] | None = mapped_column(String(255))
    status: Mapped[str] | None = mapped_column(String(255))
    tvrage: Mapped[int] | None = mapped_column(Integer)
    thetvdb: Mapped[int] | None = mapped_column(Integer)
    imdb: Mapped[str] | None = mapped_column(String(255))
    summary: Mapped[str] | None = mapped_column(Text)
    updated: Mapped[int] | None = mapped_column(Integer)

    # Relationships - referencing this model
    _genre_associations: Mapped[list[ShowGenre]] = relationship(back_populates="show", cascade="all, delete-orphan")
    genres: AssociationProxy[list[str]] = association_proxy("_genre_associations", "genre_name")
    seasons: Mapped[list[Season]] = relationship(back_populates="show", cascade="all, delete-orphan")
    episodes: Mapped[list[Episode]] = relationship(back_populates="show", cascade="all, delete-orphan")
