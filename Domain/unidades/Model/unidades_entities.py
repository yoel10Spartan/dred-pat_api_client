from pydantic import BaseModel

class AMateriaSchema( BaseModel ):
    id: int
    Collecting_Materials: str
    Potterry: int
    Lytic_Chipped_Stone: int
    Lytic_Ground_Stone: str
    Bone: int
    Malacate: int
    Figurilla: int
    Other: str
    Macrobot: str
    Carbon_14: str
    Flotation: int
    Soil: str

    class Config:
        orm_mode = True

class ElevationCMBDSchema( BaseModel ):
    id: int
    Center_top: int
    NW_corner_top: int
    NE_corner_top: int  
    SE_corner_top: int 
    SW_corner_top: int
    Center_bottom: int  
    NW_corner_bottom: int
    NE_corner_bottom: int  
    SE_corner_bottom: int  
    SW_corner_bottom: int 
    Center_difference: int
    NW_corner_difference: int
    NE_corner_difference: int
    SE_corner_difference: int
    SW_corner_difference: int
    Average: str

    class Config:
        orm_mode = True

class ExcavationCSchema( BaseModel ):
    id: int       
    Area: str       
    Unit: str      
    Quad: str       
    Lot: int
    Position_on_the_terrace: str  
    Position_in_the_excavation_of_the_quad: str  
    Excavated_portion_of_the_quad: str     
    Architectur_al_position: str  
    Feature_No: int
    Structure_No: int
    Burial_No: int

    class Config:
        orm_mode = True

class RegistrySchema( BaseModel ):
    id: int
    N_Camera: int
    Comments: str

    class Config:
        orm_mode = True

class SoilSchema( BaseModel ):
    id: int 
    Soil_Texture: str
    Soil_color_at_the_moment_of_detachment: str
    Wet_Soil_Color: str
    Soil_density: str
    Humidity: str
    Soil_volume: int

    class Config:
        orm_mode = True

class StratigraphySchema( BaseModel ):
    id: int
    Deposit_type: str
    Soil_type: str  
    Lots_above: str 
    Lots_below: str
    Lots_next_to: str
    Lots_from_the_same_deposit: str

    class Config:
        orm_mode = True

schemas = [
    AMateriaSchema,
    ElevationCMBDSchema,
    ExcavationCSchema,
    RegistrySchema,
    SoilSchema,
    StratigraphySchema
]