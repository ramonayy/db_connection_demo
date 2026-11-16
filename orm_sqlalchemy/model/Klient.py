from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from model.Base import Base

# TYPE_CHECKING ist zur Laufzeit immer False.
# Statische Type Checker behandeln TYPE_CHECKING hingegen als True.
# Dadurch werden Imports, die nur für Typannotationen benötigt werden, bei der Laufzeit übersprungen.
# So können zirkuläre Importe vermieden werden, ohne auf die statische Typprüfung verzichten zu müssen.
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
