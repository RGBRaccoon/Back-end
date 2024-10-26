from sqlalchemy import Column, String
from config.db_config import Base


class UserModel(Base):
    __tablename__ = "user"
    user_id: str = Column(String)
    email: str = Column(String, unique=True)
    password: str = Column(String, unique=True)
