from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import create_engine, DateTime, Integer
from sqlalchemy.orm.session import sessionmaker
import datetime

engine = create_engine("mysql+mysqlconnector://root:Saturn358!@127.0.0.1/tgbot", echo=True)

class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    subscription = mapped_column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()



