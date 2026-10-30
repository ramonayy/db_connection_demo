from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from model.Base import Base

if TYPE_CHECKING:
    from model.Schuld import Schuld


class Gläubiger(Base):
    __tablename__ = "Gläubiger"

    gläubigerNr: Mapped[int] = mapped_column(
        Integer, 
        name="GläubigerNr",
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
    
    schuld: Mapped[list["Schuld"]] = relationship("Schuld", back_populates="gläubiger", cascade="all, delete-orphan")