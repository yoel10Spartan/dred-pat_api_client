from pydantic import BaseModel

class CeramicaSchema( BaseModel ):
    id: int
    area: str
    unidad: str
    lote: int
    n_bolsa: int
    quad: str
    fecha_llegada: str
    fecha_analisis: str
    material: str
    parte: str
    conteo: int
    pego_g: int

    class Config:
        orm_mode = True

class LiticaSchema( BaseModel ):
    id: int 
    site: str
    bag: int
    lot: int
    area: str
    unit: str
    quad: str
    date: str
    sorter: str
    count: int
    weight_mg: int
    material: str
    obisidian_color: str
    cortex_coverage: str
    modification: int
    platform: int
    completenes: str
    primary_form: str
    secondary_form: str

    class Config:
        orm_mode = True