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

