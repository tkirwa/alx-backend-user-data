
Base = declarative_base()

class User(Base):
    """
    User model for the users table in the database.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)

    def __repr__(self):
        return f'<User(id={self.id}, email={self.email}, hashed_password={self.hashed_password}, session_id={self.session_id}, reset_token={self.reset_token})>'
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
