from fastapi import status, HTTPException, Depends
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from Domain.unidades.database_record import check_database_id
from Domain.unidades.Event.unidades import GetInformation

router = APIRouter()

def verify_database(id_db: str):
    if check_database_id(id_db):
        return id_db
    raise HTTPException(status_code=400, detail='El id de la base de datos no existe')

@router.get(
    '/get_all_items/{id_db}',
    response_class=JSONResponse,
    status_code=status.HTTP_200_OK,
    responses={
        200: {'description': 'Datos obtenidos con exito'},
        400: {'description': 'El id de la tabla no existe'}
    },
    tags=['T12_unidades_u_x_y: d98sa', 'T27_unidades_z: vfdv8']
)
async def get_all_items(
    id_db: str = Depends(verify_database)
):
    return GetInformation(id_db).get_items()


@router.get(
    '/get_an_item/{id_db}/{id_item}',
    response_class=JSONResponse,
    status_code=status.HTTP_200_OK,
    responses={
        200: {'description': 'Datos obtenidos con exito'},
        400: {'description': 'El id de la tabla no existe'}
    },
    tags=['T12_unidades_u_x_y: d98sa', 'T27_unidades_z: vfdv8']
)
async def get_an_item(
    id_item: int,
    id_db: str = Depends(verify_database)
):
    return GetInformation(id_db).get_item_id(id_item)

@router.get(
    '/get_items_lote_id/{id_db}',
    response_class=JSONResponse,
    status_code=status.HTTP_200_OK,
    responses={
        200: {'description': 'Datos obtenidos con exito'},
        400: {'description': 'El id de la tabla no existe'}
    },
    tags=['T12_unidades_u_x_y: d98sa', 'T27_unidades_z: vfdv8']
)
async def get_items_lote_id(
    id_db: str = Depends(verify_database)
):
    return GetInformation(id_db).get_items_id_lote()