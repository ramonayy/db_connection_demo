from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from model.Base import Base

if TYPE_CHECKING:
    from model.Schuld import Schuld



class Klient(Base):
    __tablename__ = "Klient"

    klientenNr: Mapped[int] = mapped_column(
        Integer, 
        name="KlientenNr",
        primary_key=True
        )
    nname: Mapped[str] = mapped_column(
        String,
        name="Nname"
        )
    vname: Mapped[str] = mapped_column(
        String,
        name="Vname"
        )
    strasse: Mapped[str] = mapped_column(
        String,
        name="Strasse"
        )
    plz: Mapped[int] = mapped_column(
        Integer,
        name="PLZ")
    ort: Mapped[str] = mapped_column(
        String,
        name="Ort"
        )
    telefonNr: Mapped[int] = mapped_column(
        Integer,
        name="TelefonNr"
        )
    beruf: Mapped[str] = mapped_column(
        String,
        name="Beruf"
        )
    monatseinkommen: Mapped[int] = mapped_column(
        Integer,
        name="Monatseinkommen"
        )

    schuld: Mapped["Schuld"] = relationship("Schuld", back_populates="klient", cascade="all, delete-orphan")
