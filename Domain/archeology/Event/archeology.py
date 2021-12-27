from typing import List
from Domain.archeology.Event.data import get_identifier_table, get_items_db
from Domain.archeology.table_record import table_registration

# =================================================
class VerifyMatch:
    def __init__(self, value, item_search) -> None:
        self.value = value
        self.item_search = item_search

    def check_the_batch(self, item: dict):
        if item.get(self.item_search) == self.value:
            return True

# =================================================
class DataRepresentation:
    def __verify_return(self, data: list, values: bool):
        return data if not values else self.__get_values(data)

    def __get_values(self, data: list = []) -> List[dict]:
        return [list(i.values()) for i in data]

    def split_data(self, skip: int = 0, limit: int = 10, values: bool = True) -> List[dict]:
        return self.__verify_return(self.data[skip:limit], values)

    def filter_data(self, element_filter: any, values: bool = True):
        verify_match = VerifyMatch(element_filter, self.identifier)
        return self.__verify_return(filter(verify_match.check_the_batch, self.data), values)

    def get_columns(self):
        return [column.key for column in list(self.table.table.__table__.columns)]

# ================= Client Code ==================
class Archeology(DataRepresentation):
    def __init__(self, id_table) -> None:
        self.table = table_registration.get(id_table)
        self.data = get_items_db(id_table)
        self.identifier = get_identifier_table(id_table)

    def filter_lote(self, lote: int = None):
        if lote:
            self.data = list(self.filter_data(lote, False))

# =================================================
