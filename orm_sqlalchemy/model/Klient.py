from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from model.Base import Base

if TYPE_CHECKING:
    from model.Schuld import Schuld



class Klient(Base):
    __tablename__ = "klient"

    klientenNr: Mapped[int] = mapped_column(
        Integer, 
        primary_key=True
        )
    nname: Mapped[str] = mapped_column(
        String(50)
        )
    vname: Mapped[str] = mapped_column(
        String(50)
        )
    strasse: Mapped[str] = mapped_column(
        String(50)
        )
    plz: Mapped[int] = mapped_column(
        Integer
        )
    ort: Mapped[str] = mapped_column(
        String(50)
        )
    telefonNr: Mapped[int] = mapped_column(
        Integer
        )
    beruf: Mapped[str] = mapped_column(
        String(50)
        )
    monatseinkommen: Mapped[int] = mapped_column(
        Integer
        )

    schuld: Mapped["Schuld"] = relationship("Schuld", back_populates="klient", cascade="all, delete-orphan")
