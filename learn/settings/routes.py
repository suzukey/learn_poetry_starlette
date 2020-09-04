from starlette.routing import Route, Mount

from learn.app import index, json
from learn.settings.directory import static

routes = [
    Route('/', endpoint=index.Endpoint),
    Route('/json', endpoint=json.Endpoint),
    Mount('/static', static, name='static')
]
