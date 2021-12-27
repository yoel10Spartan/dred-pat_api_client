from typing import List
from Infrastructure.data.home import OpenConectionT27
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from Infrastructure.data.models.t27_unidad_z import t27_unidades_z

[
    AMateria, 
    ElevationCMBD, 
    ExcavationC, 
    Registry, 
    Soil,
    Stratigraphy
] = t27_unidades_z

@OpenConectionT27
def get_items(session: sessionmaker) -> List[declarative_base]:
    return session.query(AMateria, ElevationCMBD, ExcavationC, Registry, Soil, Stratigraphy) \
                .join(ElevationCMBD, AMateria.id == ElevationCMBD.id) \
                .join(ExcavationC, AMateria.id == ExcavationC.id) \
                .join(Registry, AMateria.id == Registry.id) \
                .join(Soil, AMateria.id == Soil.id) \
                .join(Stratigraphy, AMateria.id == Stratigraphy.id)

@OpenConectionT27
def get_item_by_id(id: int, session: sessionmaker):
    return get_items().where(AMateria.id == id)

@OpenConectionT27
def get_item_id_lote(session: sessionmaker):
    return session.query(AMateria.id, ExcavationC.Lot) \
            .join(ExcavationC, AMateria.id == ExcavationC.id)
