from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from model.Base import Base



class User(Base):
    __tablename__ = "User"

    userId: Mapped[int] = mapped_column(
        Integer,
        name="UserId",
        primary_key=True
        )
    username: Mapped[str] = mapped_column(
        String,
        name="UserName"
        )
    email: Mapped[str] = mapped_column(
        String,
        name="Email"
        )
    passwort: Mapped[str] = mapped_column(
        String,
        name="Passwort"
        )