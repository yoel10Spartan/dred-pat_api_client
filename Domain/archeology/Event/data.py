from functools import lru_cache
from Domain.archeology.table_record import table_registration
from Domain.archeology.Service.archeology_service import get, get_identifier

# =====================================================================

@lru_cache(maxsize=100)
def get_items_db(id_table: str):
    table_model = table_registration.get(id_table)
    items = get(table_model.dependence, table_model.table)
    return [table_model.model.from_orm(i).dict() for i in items]

# =====================================================================

# We get the index of the table.
# But there are two indexes (primary key and ordinary index).
# The ordinary index is in position 1 and within that tuple 
# we look for the name of the field that is in position 4.
def get_identifier_table(id_table: str):
    table_model = table_registration.get(id_table)
    return get_identifier(table_model.dependence, table_model.name).all()[1][4]

# =====================================================================