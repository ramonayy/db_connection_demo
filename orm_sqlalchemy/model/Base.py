from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

'''
Wenn eine Subklasse "klient" erstellt wird:

1. SQLAlchemy erkennt die deklarative Klasse.
2. Es erstellt ein Table-Objekt für die Tabelle "klient".
3. Das Table-Objekt wird in Base.metadata registriert.
4. Es erstellt einen Mapper, der die Python Klasse mit dem Table-Objekt verbindet.
5. Der Mapper wird der Registry zugeordnet.
'''