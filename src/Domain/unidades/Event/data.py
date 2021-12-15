from functools import lru_cache
from Domain.unidades.database_record import database_registration

# i[1] - Model Pydantic
# i[0] - Model SQLALCHEMY of the Data Base

# =======================================================================

def convert_orm(item: list):
    return [{i[0].name: i[1].from_orm(i[0]).dict() }  for i in item]

@lru_cache(maxsize=100)
def get_items_db_unidades(id_database: str):
    database_modal = database_registration.get(id_database)
    [get, _] = database_modal.service_funtions
    items = get(database_modal.dependence)
    union_schema = [list(zip(i, database_modal.model)) for i in items]
    return list(map(convert_orm, union_schema))

# =======================================================================

def get_item_by_id_table(id_database: str, id: int):
    database_modal = database_registration.get(id_database)
    [_, get_item_id, _] = database_modal.service_funtions
    items = get_item_id(database_modal.dependence, id)
    # union_schema = [list(zip(i, database_modal.model)) for i in items][0]
    # [i[1].from_orm(i[0]).dict() for i in union_schema]
    return items

# =======================================================================

def get_item_lote_id(id_database: str):
    database_modal = database_registration.get(id_database)
    [_, _, get_item_lote] = database_modal.service_funtions
    items = get_item_lote(database_modal.dependence)
    return items