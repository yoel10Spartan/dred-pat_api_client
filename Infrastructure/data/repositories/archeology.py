from typing import List
from Infrastructure.data.home import OpenConection
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import text

@OpenConection
def get_items(table: declarative_base, session: sessionmaker) -> List[declarative_base]:
    return session.query(table)

@OpenConection
def get_index(table_name: str, session):
    return session.execute(text("show index from {}".format(table_name)))