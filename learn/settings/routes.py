from starlette.routing import Route, Mount

from learn.app.index import homepage, testjson
from learn.settings.directory import static

routes = [
    Route('/', endpoint=homepage),
    Route('/json', endpoint=testjson),
    Mount('/static', static, name='static')
]
