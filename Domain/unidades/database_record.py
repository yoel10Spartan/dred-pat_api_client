from typing import Any, Optional
from pydantic import BaseModel
from Domain.unidades.Model.unidades_entities import schemas
from Infrastructure.data.models.t12_unidades_u_x_y import t12_unidades_u_x_y
from Infrastructure.data.models.t27_unidad_z import t27_unidades_z
from Domain.unidades.Service import t12_service
from Domain.unidades.Service import t27_service
from DependencyInjection.build_dependencies import get_dependencies

class Table(BaseModel):
    table: Any
    model: Any
    name: str
    service_funtions: Optional[list]
    dependence: Optional[Any]

unidad_t12 = get_dependencies().t12_protocol
unidad_t27 = get_dependencies().t27_protocol

database_registration = {
    'd98sa': Table(
        table=t12_unidades_u_x_y, 
        model=schemas, 
        name='t12_unidades_u_x_y',
        service_funtions=[t12_service.get, t12_service.get_item_id, t12_service.get_item_lote],
        dependence=unidad_t12
    ),
    'vfdv8': Table(
        table=t27_unidades_z, 
        model=schemas, 
        name='t27_unidades_z',
        service_funtions=[t27_service.get, t27_service.get_item_id, t27_service.get_item_lote],
        dependence=unidad_t27
    )
}

def check_database_id(id_database: str):
    return id_database in database_registration