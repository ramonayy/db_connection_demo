from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from model.Base import Base



class User(Base):
    __tablename__ = "user"

    userId: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
        )
    username: Mapped[str] = mapped_column(
        String(50)
        )
    email: Mapped[str] = mapped_column(
        String(50)
        )
    passwort: Mapped[str] = mapped_column(
        String(50)
        )