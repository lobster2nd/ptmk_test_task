from datetime import datetime
from typing import Annotated

from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine, String, text
from sqlalchemy.orm import mapped_column

from config import settings

engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
)
session = sessionmaker(engine)

str256 = Annotated[str, 256]
birthday = Annotated[datetime, mapped_column()]
created_at = Annotated[datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"),
    onupdate=datetime.utcnow)]


class Base(DeclarativeBase):
    type_annotation_map = {
        str256: String(256),
    }
