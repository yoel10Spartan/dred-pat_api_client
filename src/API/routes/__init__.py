from fastapi.applications import FastAPI
from API.routes import root
from API.routes.Arqueology import arqueology_controll
from API.routes.Files import files_controll
from API.routes.Unidades import unidades_controll

def register_routers(app: FastAPI) -> FastAPI:
    app.include_router(root.router)
    app.include_router(arqueology_controll.router, prefix='/api/v1.0/archeology')
    app.include_router(files_controll.router, prefix='/api/v1.0/files')
    app.include_router(unidades_controll.router, prefix='/api/v1.0/unidades')
    return app