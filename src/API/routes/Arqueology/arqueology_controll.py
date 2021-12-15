from fastapi import status, HTTPException, Depends
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from Domain.archeology.Event.archeology import Archeology
from Domain.archeology.table_record import check_table_id

router = APIRouter()

def verify_table(id_table: str):
    if check_table_id(id_table):
        return id_table
    raise HTTPException(status_code=400, detail='El id de la tabla no existe')

@router.get(
    '/get_items_parts/{id_table}',
    response_class=JSONResponse,
    status_code=status.HTTP_200_OK,
    responses={
        200: {'description': 'Datos obtenidos con exito'},
        400: {'description': 'El id de la tabla no existe'}
    },
    tags=['Table Ceramica: kj23h', 'Table Litica: lk435']
)
async def get_items_parts_table(
    id_table: str = Depends(verify_table), 
    skip: int = 0, 
    limit: int = 10, 
    lote: int = None
):
    arqueology = Archeology(id_table)
    arqueology.filter_lote(lote)
    return arqueology.split_data(skip=skip, limit=limit)

@router.get(
    '/get_columns/{id_table}',
    response_class=JSONResponse,
    status_code=status.HTTP_200_OK,
    responses={
        200: {'description': 'Nombre de las columnas obtenidas con exito'},
        400: {'description': 'El id de la tabla no existe'}
    },
    tags=['Table Ceramica: kj23h', 'Table Litica: lk435']
)
async def get_columns(id_table: str = Depends(verify_table)):
    arqueology = Archeology(id_table)
    return {'list_elements': arqueology.get_columns()}