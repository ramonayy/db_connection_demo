from model.User import User
from sqlalchemy.exc import SQLAlchemyError, IntegrityError


class UserRepository:
    def __init__(self, session):
        self.session = session


    def getUserById(self, userId: int):
        return self.session.query(User).filter_by(userId=userId).first()


    def saveUser(self, user_obj: User):
        try:
            self.session.add(user_obj)
        except IntegrityError as e:
            print(f"Object already exists in database: {e}")
            self.session.rollback()
        except SQLAlchemyError as e:
            print(f"An error occurred: {e}")
            self.session.rollback()
        else:
            self.session.commit()