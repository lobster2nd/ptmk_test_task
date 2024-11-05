import uuid

from sqlalchemy import Table, Column, Integer, String, UUID, MetaData
from sqlalchemy.orm import Mapped, mapped_column
from database import Base, str256, created_at, updated_at, birthday

import enum


class Genders(enum.Enum):
    __tablename__ = "genders"
    male = "Male"
    female = "Female"


class Employees(Base):
    __tablename__ = "employees"

    uid: Mapped[uuid] = mapped_column(primary_key=True)
    username: Mapped[str256]
    birthday: Mapped[birthday]
    gender: Mapped[Genders]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

