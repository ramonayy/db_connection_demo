from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from model.Base import Base


if TYPE_CHECKING:
    from model.Schuld import Schuld



class Vertrag(Base):
    __tablename__ = "Vertrag"

    vertragsNr: Mapped[int] = mapped_column(
        Integer, 
        name="VertragsNr",
        primary_key=True
        )
    schuldNr: Mapped[int] = mapped_column(
        Integer,
         ForeignKey(Schuld.schuldNr),
        name="SchuldNr"
        )
    monatsrate: Mapped[int] = mapped_column(
        Integer,
        name="Monatsrate"
        )
    zahlungsart: Mapped[str] = mapped_column(
        String,
        name="Zahlungsart"
        )
    abzahlungInJahren: Mapped[int] = mapped_column(
        Integer,
        name="AbzahlungInJahren"
        )
    schuld: Mapped["Schuld"] = relationship("Schuld", back_populates="vertrag", lazy="select")