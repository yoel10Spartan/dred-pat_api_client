from sqlalchemy import Column, Integer, String, INT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Index

Base = declarative_base()

class AMateria( Base ):
    __tablename__ = 'a_material'
    
    id = Column( 'id', Integer, primary_key=True, unique=True )
    Collecting_Materials = Column( 'Collecting_Materials', String(40), nullable=False )
    Potterry = Column( 'Potterry', INT, nullable=False )
    Lytic_Chipped_Stone = Column( 'Lytic_Chipped_Stone', INT, nullable=False )
    Lytic_Ground_Stone = Column( 'Lytic_Ground_Stone', INT, nullable=False )
    Bone = Column( 'Bone', INT, nullable=False )
    Malacate = Column( 'Malacate', INT, nullable=False )
    Figurilla = Column( 'Figurilla', INT, nullable=False )
    Other = Column( 'Other', String(40), nullable=False )
    Macrobot = Column( 'Macrobot', String(40), nullable=False )
    Carbon_14 = Column( 'Carbon_14', String(40), nullable=False )
    Flotation = Column( 'Flotation', INT, nullable=False )
    Soil = Column( 'Soil', String(40), nullable=False )

    @property
    def name(self):
        return self.__tablename__

    def __repr__(self) -> str:
        return '<AMateria {}>'.format( str(self.id) )

class ElevationCMBD( Base ):
    __tablename__ = 'elevation_cmbd'

    id = Column( Integer, primary_key=True, unique=True )
    Center_top = Column( INT, nullable=False )
    NW_corner_top = Column( INT, nullable=False )  
    NE_corner_top = Column( INT, nullable=False )  
    SE_corner_top = Column( INT, nullable=False )  
    SW_corner_top = Column( INT, nullable=False )  
    Center_bottom = Column( INT, nullable=False )  
    NW_corner_bottom = Column( INT, nullable=False )
    NE_corner_bottom = Column( INT, nullable=False )  
    SE_corner_bottom = Column( INT, nullable=False )  
    SW_corner_bottom = Column( INT, nullable=False )  
    Center_difference = Column( INT, nullable=False ) 
    NW_corner_difference = Column( INT, nullable=False )
    NE_corner_difference = Column( INT, nullable=False )
    SE_corner_difference = Column( INT, nullable=False )
    SW_corner_difference = Column( INT, nullable=False )
    Average = Column( String(5), nullable=False )

    @property
    def name(self):
        return self.__tablename__

    def __repr__(self) -> str:
        return '<ElevationCMBD {}>'.format( str(self.id) )

class ExcavationC( Base ):
    __tablename__ = 'excavation_c'

    id = Column( Integer, primary_key=True, unique=True )       
    Area = Column( String(10), nullable=False )       
    Unit = Column( String(10), nullable=False )       
    Quad = Column( String(10), nullable=False )       
    Lot = Column( INT, nullable=False ) 
    Position_on_the_terrace = Column( String(40), nullable=False )   
    Position_in_the_excavation_of_the_quad = Column( String(40), nullable=False )
    Excavated_portion_of_the_quad = Column( String(40), nullable=False )     
    Architectur_al_position = Column( String(40), nullable=False )
    Feature_No = Column( INT, nullable=False )      
    Structure_No = Column( INT, nullable=False )
    Burial_No = Column( INT, nullable=False )

    @property
    def name(self):
        return self.__tablename__

    Index('lote', 'Lot')

    def __repr__(self) -> str:
        return '<ExcavationC {}>'.format( str(self.id) )

class Registry( Base ):
    __tablename__ = 'registry'

    id = Column( Integer, primary_key=True, unique=True )  
    N_Camera = Column( INT, nullable=False ) 
    Comments = Column( String(100), nullable=False )

    @property
    def name(self):
        return self.__tablename__

    def __repr__(self) -> str:
        return '<Registry {}>'.format( str(self.id) )

class Soil( Base ):
    __tablename__ = 'soil'

    id = Column( Integer, primary_key=True, unique=True ) 
    Soil_Texture = Column( String(40), nullable=False )  
    Soil_color_at_the_moment_of_detachment  = Column( String(10), nullable=False )
    Wet_Soil_Color = Column( String(10), nullable=False ) 
    Soil_density = Column( String(20), nullable=False ) 
    Humidity = Column( String(40), nullable=False )
    Soil_volume = Column( INT, nullable=False )

    @property
    def name(self):
        return self.__tablename__

    def __repr__(self) -> str:
        return '<Soil {}>'.format( str(self.id) )

class Stratigraphy( Base ):
    __tablename__ = 'stratigraphy'

    id = Column( Integer, primary_key=True, unique=True ) 
    Deposit_type = Column( String(40), nullable=False ) 
    Soil_type = Column( String(40), nullable=False )  
    Lots_above = Column( String(20), nullable=False ) 
    Lots_below = Column( INT, nullable=False ) 
    Lots_next_to = Column( INT, nullable=False ) 
    Lots_from_the_same_deposit = Column( String(40), nullable=False )

    @property
    def name(self):
        return self.__tablename__

    def __repr__(self) -> str:
        return '<Stratigraphy {}>'.format( str(self.id) )

t27_unidades_z = [ 
    AMateria, 
    ElevationCMBD, 
    ExcavationC, 
    Registry, 
    Soil, 
    Stratigraphy 
]