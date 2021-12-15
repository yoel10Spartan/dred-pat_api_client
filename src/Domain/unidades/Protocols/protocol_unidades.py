from typing import Protocol

class ProtocolUnidades(Protocol):
    def get_items(self):
        ...

    def get_item_by_id(self, id: int):
        ...
    
    def get_item_id_lote(self):
        ...