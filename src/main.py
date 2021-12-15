import uvicorn
from API.app import init_app
from Resources.config.environment import get_settings

_SETTINGS = get_settings()

app = init_app(_SETTINGS)

def start(path_run: str):
    uvicorn.run(
        path_run,
        host=_SETTINGS.WEB_SERVER_HOST,
        port=_SETTINGS.WEB_SERVER_PORT,
        reload=_SETTINGS.WEB_SERVER_RELOAD
    )

if __name__ == '__main__':
    start('main:app')

# from Domain.archeology.Event.unidades import GetInformation
# print( GetInformation('d98sa').get_item_id(100) )
# print(GetInformation('d98sa').get_items())

# from Domain.unidades.Service.t12_service import get_item_lote
# from DependencyInjection.build_dependencies import get_dependencies

# t27 = get_dependencies().t27_protocol

# print(get_item_lote(t27))
