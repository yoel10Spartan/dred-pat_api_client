from sqlalchemy import Column, Integer, String, INT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Index

Base = declarative_base()

class Ceramica( Base ):
    __tablename__ = 'ceramica'

    id = Column( 'id', Integer, primary_key=True, unique=True )
    area = Column( 'area', String(200), nullable=False )
    unidad = Column( 'unidad', String(200), nullable=False )
    lote = Column( 'lote', INT, nullable=False )
    n_bolsa = Column( 'n_bolsa', INT, nullable=False )
    quad = Column( 'quad', String(200), nullable=False )
    fecha_llegada = Column( 'fecha_llegada', String(200), nullable=False )
    fecha_analisis = Column( 'fecha_analisis', String(200), nullable=False )
    material = Column( 'material', String(200), nullable=False )
    parte = Column( 'parte', String(200), nullable=False )
    conteo = Column( 'conteo', INT, nullable=False )
    pego_g = Column( 'peso_g', INT, nullable=False )

    Index('lote', 'lote')
    
    def __repr__(self) -> str:
        return '<Ceramica {}>'.format( str(self.lote) )

class Litica( Base ):
    __tablename__ = 'litica'

    id = Column( 'id', Integer, primary_key=True, unique=True )
    site = Column( 'site', String(200), nullable=False )
    bag = Column( 'bag', INT, nullable=False )
    lot = Column( 'lot', INT, nullable=False )
    area = Column( 'area', String(200), nullable=False )
    unit = Column( 'unit', String(200), nullable=False )
    quad = Column( 'quad', String(200), nullable=False )
    date = Column( 'date', String(200), nullable=False )
    sorter = Column( 'sorter', String(200), nullable=False )
    count = Column( 'count', INT, nullable=False )
    weight_mg = Column( 'weight_mg', INT, nullable=False )
    material = Column( 'material', String(200), nullable=False )
    obisidian_color = Column( 'obisidian_color', String(200), nullable=False )
    cortex_coverage = Column( 'cortex_coverage', String(200), nullable=False )
    modification = Column( 'modification', INT, nullable=False )
    platform = Column( 'platform', INT, nullable=False )
    completenes = Column( 'completenes', String(200), nullable=False )
    primary_form = Column( 'primary_form', String(200), nullable=False )
    secondary_form = Column( 'secondary_form', String(200), nullable=False )
    
    Index('lote', 'lot')

    def __repr__(self) -> str:
        return '<Litica {}>'.format( str(self.lot) )