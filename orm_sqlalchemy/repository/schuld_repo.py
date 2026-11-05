from model.Schuld import Schuld


class SchuldRepository:
    def __init__(self, session):
        self.session = session

    def getSchuldBySchuldNr(self, schuldNr: int):
        return self.session.query(Schuld).filter_by(schuldNr=schuldNr).first()

    def getAllSchulden(self):
        return self.session.query(Schuld).all()

    def getSchuldByGlaeubigerNr(self, glaeubigerNr: int):
        return self.session.query(Schuld).filter_by(glaeubigerNr=glaeubigerNr).all()