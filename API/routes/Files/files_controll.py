from fastapi.routing import APIRouter
from fastapi import HTTPException, status, Depends
from fastapi.responses import JSONResponse
from starlette.responses import FileResponse
from Domain.files.Event.files import Files, verify_access

router = APIRouter()

def verify_path_access(items_path: str):
    path = verify_access(items_path)
    print(path)
    if not path:
        raise HTTPException(status_code=400, detail='El directorio o archivo no existe')
    return path

@router.get(
    '/get_files_directories/{items_path:path}',
    response_class=JSONResponse,
    status_code=status.HTTP_200_OK,
    responses={
        200: {'description': 'Informacion extraida satisfactoriamente'},
        400: {'description': 'El directorio no existe'}
    },
    tags=['Get files and directories']
)
async def get_files_directories(
    items_path: str = Depends(verify_path_access)
):
    files = Files(path=items_path)
    return files.get_files_directories()

@router.get(
    '/download_file/{items_path:path}',
    response_class=JSONResponse,
    status_code=status.HTTP_200_OK,
    responses={
        200: {'description': 'El archivo esta preparado para su descarga'},
        400: {'description': 'El directorio o archivo no existe'}
    },
    tags=['Download files']
)
async def download_file(
    items_path: str = Depends(verify_path_access)
):
    files = Files(path=items_path)
    items_file = await files.get_path_file()

    return FileResponse(
        path=items_file['file_path'], 
        media_type=items_file['media_type'],
        status_code=200,
        headers={ 'file_extension': items_file['file_extension'] }
    )