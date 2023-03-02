
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base (DeclarativeBase):
  pass

# class User(Base):
#   __tablename__ = "user_account"

#   id: Mapped[int] = mapped_column(primary_key=True)
#   name: Mapped[str] = mapped_column(String(30))
#   fullname: Mapped[Optional[str]]

#   addresses: Mapped[List["Address"]] = relationship(
#       back_populates="user", cascade="all, delete-orphan"
#   )

#   def __repr__(self) -> str:
#       return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Contact(Base):
  __tablename__ = "contacts"

  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String[255])
  job: Mapped[str] = mapped_column(String[255])
  email: Mapped[str] = mapped_column(String[255])
  
  def __repr__(self) -> str:
    return f"Contact(id={self.id!r}, name={self.name}, job={self.job}, fullname={self.fullname})"

# class Address(Base):
#   __tablename__ = "address"

#   id: Mapped[int] = mapped_column(primary_key=True)
#   email_address: Mapped[str]
#   user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))

#   user: Mapped["User"] = relationship(back_populates="addresses")

#   def __repr__(self) -> str:
#       return f"Address(id={self.id!r}, email_address={self.email_address!r})"

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///contacts.db", echo=True)
session = Session(engine)

stmt = select(Contact)
result = session.execute(stmt)
result._raw_all_rows()

print("Done!")

# Base.metadata.create_all(engine)

