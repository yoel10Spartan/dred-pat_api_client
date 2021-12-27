from typing import Protocol
from sqlalchemy.ext.declarative import declarative_base

class ProtocolArcheology(Protocol):
    def get_items(self, table: declarative_base):
        ...

    def get_index(self, table_name: str):
        ...