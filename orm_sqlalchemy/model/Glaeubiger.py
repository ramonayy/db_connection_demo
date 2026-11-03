from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from model.Base import Base

if TYPE_CHECKING:
    from model.Schuld import Schuld


class Glaeubiger(Base):
    __tablename__ = "glaeubiger"

    glaeubigerNr: Mapped[int] = mapped_column(
        Integer, 
        primary_key=True
        )
    nname: Mapped[str] = mapped_column(
        String(50),
        )
    vname: Mapped[str] = mapped_column(
        String(50),
        )
    strasse: Mapped[str] = mapped_column(
        String(50),
        )
    plz: Mapped[int] = mapped_column(
        Integer,
)
    ort: Mapped[str] = mapped_column(
        String(50),
        )
    telefonNr: Mapped[int] = mapped_column(
        Integer,
        )
    
    schuld: Mapped[list["Schuld"]] = relationship("Schuld", back_populates="glaeubiger", cascade="all, delete-orphan")