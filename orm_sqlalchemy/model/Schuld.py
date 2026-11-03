from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from model.Base import Base


if TYPE_CHECKING:
    from orm_sqlalchemy.model.Klient import Klient
    from orm_sqlalchemy.model.Glaeubiger import Glaeubiger


class Schuld(Base):
    __tablename__ = "schuld"

    schuldNr: Mapped[int] = mapped_column(
        Integer, 
        primary_key=True
        )
    hoehe: Mapped[int] = mapped_column(
        Integer,
        )
    glaeubigerNr: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("glaeubiger.glaeubigerNr"),
        )
    klientenNr: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("klient.klientenNr"),
        )
    grund: Mapped[str] = mapped_column(
        String(200)
        )

    glaeubiger: Mapped["Glaeubiger"] = relationship("Glaeubiger", back_populates="schuld", lazy="select")
    klient: Mapped["Klient"] = relationship("Klient", back_populates="schuld", lazy="select")