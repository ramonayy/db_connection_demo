from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from model.Base import Base

# TYPE_CHECKING ist zur Laufzeit immer False.
# Statische Type Checker behandeln TYPE_CHECKING hingegen als True.
# Dadurch werden Imports, die nur für Typannotationen benötigt werden, bei der Laufzeit übersprungen.
# So können zirkuläre Importe vermieden werden, ohne auf die statische Typprüfung verzichten zu müssen.
if TYPE_CHECKING:
    from model.Schuld import Schuld



class Vertrag(Base):
    __tablename__ = "vertrag"

    vertragsNr: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
        )
    schuldNr: Mapped[int] = mapped_column(
        Integer,
         ForeignKey("schuld.schuldNr")
        )
    monatsrate: Mapped[int] = mapped_column(
        Integer
        )
    zahlungsart: Mapped[str] = mapped_column(
        String(50)
        )
    abzahlungInJahren: Mapped[int] = mapped_column(
        Integer
        )
    schuld: Mapped["Schuld"] = relationship("Schuld", back_populates="vertrag", lazy="joined")