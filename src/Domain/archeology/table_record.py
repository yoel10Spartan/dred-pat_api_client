from typing import Any, Optional
from pydantic import BaseModel
from Infrastructure.data.models.archeology import Ceramica, Litica
from Domain.archeology.Model.archeology_entities import CeramicaSchema, LiticaSchema
from DependencyInjection.build_dependencies import get_dependencies

class Table(BaseModel):
    table: Any
    model: Any
    name: str
    service_funtions: Optional[list]
    dependence: Optional[Any]

archeology = get_dependencies().archeology_protocol

table_registration = {
    'kj23h': Table(
        table=Ceramica, 
        model=CeramicaSchema, 
        name='ceramica',
        dependence=archeology
    ),
    'lk435': Table(
        table=Litica, 
        model=LiticaSchema, 
        name='litica',
        dependence=archeology    
    )
}

def check_table_id(id_table: str):
    return id_table in table_registration
