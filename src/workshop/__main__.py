import uvicorn
from .settings import settings

uvicorn.run(
    'workshop.app:app',
    host=settings.server_host,
    port=settings.server_port,
    reload=True,
    log_level='debug',
    access_log=True,
)
