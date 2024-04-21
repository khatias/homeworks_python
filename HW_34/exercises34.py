

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

db_url = "mysql+pymysql://root:Xatenco22@localhost/it_step_34"
engine = create_engine(db_url, echo=False)
Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    profile = relationship("Profile", back_populates="user", uselist=False)


class Profile(Base):
    __tablename__ = "profile"
    id = Column(Integer, primary_key=True, autoincrement=True)
    bio = Column(String(250))
    profile_picture = Column(String(250))
    user_id = Column(Integer, ForeignKey("user.id"), unique=True)

    user = relationship("User", back_populates="profile")


if __name__ == "__main__":
    Base.metadata.create_all(engine)


