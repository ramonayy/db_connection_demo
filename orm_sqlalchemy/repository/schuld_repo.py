from model.Schuld import Schuld
from sqlalchemy.exc import SQLAlchemyError


class SchuldRepository:
    def __init__(self, session):
        self.session = session


    def getSchuldBySchuldNr(self, schuldNr: int):
        return self.session.query(Schuld).filter_by(schuldNr=schuldNr).first()


    def getAllSchulden(self):
        return self.session.query(Schuld).all()


    def getSchuldByGlaeubigerNr(self, glaeubigerNr: int):
        return self.session.query(Schuld).filter_by(glaeubigerNr=glaeubigerNr).all()


    def deleteSchuldBySchuldNr(self, schuldNr: int):
        try:
            self.session.query(Schuld).filter_by(
                schuldNr=schuldNr
            ).delete(synchronize_session=False)

            self.session.commit()
            return True

        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error deleting Schuld: {e}")
            return False