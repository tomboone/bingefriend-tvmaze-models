"""SQLAlchemy model for a show-genre association."""
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bingefriend_tvmaze_models.models.base import Base

if TYPE_CHECKING:
    from bingefriend_tvmaze_models.models.show import Show


class ShowGenre(Base):
    """
    Represents the association between a Show and a genre name.

    This model uses a composite primary key (show_id, genre_name) to
    ensure that each show-genre pairing is unique. It is designed to be
    used with an association_proxy on the Show model for direct access
    to genre names.
    """
    __tablename__ = "show_genre"

    # Attributes
    show_id: Mapped[int] = mapped_column(ForeignKey("shows.id"), primary_key=True)
    genre_name: Mapped[str] = mapped_column(String(255), primary_key=True)

    # Relationships - referenced in this model
    show: Mapped[Show] = relationship(back_populates="_genre_associations")
