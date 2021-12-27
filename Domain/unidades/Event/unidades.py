from Domain.unidades.Event.data import get_item_by_id_table, get_items_db_unidades, get_item_lote_id

class GetInformation:
    def __init__(self, id_unidad) -> None:
        self.id_unidad = id_unidad

    def get_items(self):
        return get_items_db_unidades(self.id_unidad)

    def get_item_id(self, id_register: int):
        return get_item_by_id_table(self.id_unidad, id_register)

    def get_items_id_lote(self):
        return get_item_lote_id(self.id_unidad)