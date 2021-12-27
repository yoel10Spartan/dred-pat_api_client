from typing import Any, Optional
from Domain.archeology.Protocols.protocol_archeology import ProtocolArcheology
from sqlalchemy.ext.declarative import declarative_base

def get(protocol: ProtocolArcheology, table: declarative_base) -> Optional[Any]:
    return protocol.get_items(table).all()

def get_identifier(protocol: ProtocolArcheology, name_table: str) -> Optional[Any]:
    return protocol.get_index(name_table)