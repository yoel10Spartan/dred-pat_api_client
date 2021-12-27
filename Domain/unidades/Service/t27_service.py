from typing import Any, Optional
from Domain.unidades.Protocols.protocol_unidades import ProtocolUnidades

def get(protocol: ProtocolUnidades) -> Optional[Any]:
    return protocol.get_items().all()

def get_item_id(protocol: ProtocolUnidades, id: int) -> Optional[Any]:
    return protocol.get_item_by_id(id).all()

def get_item_lote(protocol: ProtocolUnidades) -> Optional[Any]:
    return protocol.get_item_id_lote().all()