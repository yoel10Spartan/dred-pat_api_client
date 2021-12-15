from typing import List
from Infrastructure.data.home import OpenConectionT12
from sqlalchemy.orm import session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from Infrastructure.data.models.t12_unidades_u_x_y import t12_unidades_u_x_y

[
    AMateria, 
    ElevationCMBD, 
    ExcavationC, 
    Registry, 
    Soil,
    Stratigraphy
] = t12_unidades_u_x_y

@OpenConectionT12
def get_items(session: sessionmaker) -> List[declarative_base]:
    return session.query(AMateria, ElevationCMBD, ExcavationC, Registry, Soil, Stratigraphy) \
                .join(ElevationCMBD, AMateria.id == ElevationCMBD.id) \
                .join(ExcavationC, AMateria.id == ExcavationC.id) \
                .join(Registry, AMateria.id == Registry.id) \
                .join(Soil, AMateria.id == Soil.id) \
                .join(Stratigraphy, AMateria.id == Stratigraphy.id)

@OpenConectionT12
def get_item_by_id(id: int, session: sessionmaker):
    return get_items().where(AMateria.id == id)

@OpenConectionT12
def get_item_id_lote(session: sessionmaker):
    return session.query(AMateria.id, ExcavationC.Lot) \
            .join(ExcavationC, AMateria.id == ExcavationC.id)
