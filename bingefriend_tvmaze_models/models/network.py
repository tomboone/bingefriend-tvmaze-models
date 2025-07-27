"""SQLAlchemy model for a network."""
from typing import TYPE_CHECKING

from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

from bingefriend_tvmaze_models.models.base import Base

if TYPE_CHECKING:
    from bingefriend_tvmaze_models.models.show import Show
    from bingefriend_tvmaze_models.models.season import Season


class Network(Base):
    """SQLAlchemy model for a network."""
    __tablename__ = "networks"

    # Attributes
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    name: Mapped[str] | None = mapped_column(String(255))
    country_code: Mapped[str] | None = mapped_column(String(255))

    # Relationships - referencing this model
    seasons: Mapped[list[Season]] = relationship(back_populates="network")
