from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from model.Base import Base

if TYPE_CHECKING:
    from model.Klient import Klient
    from model.Gläubiger import Gläubiger


class Schuld(Base):
    __tablename__ = "Schuld"

    schuldNr: Mapped[int] = mapped_column(
        Integer, 
        name="SchuldNr",
        primary_key=True
        )
    höhe: Mapped[int] = mapped_column(
        Integer,
        name="Höhe"
        )
    gläubigerNr: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("Gläubiger.GläubigerNr"),
        name="GläubigerNr"
        )
    klientenNr: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("Klient.KlientenNr"),
        name="KlientenNr"
        )
    grund: Mapped[str] = mapped_column(
        String,
        name="Grund"
        )

    gläubiger: Mapped["Gläubiger"] = relationship("Gläubiger", back_populates="schuld", lazy="select")
    klient: Mapped["Klient"] = relationship("Klient", back_populates="schuld", lazy="select")