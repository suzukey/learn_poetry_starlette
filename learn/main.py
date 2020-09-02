from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route, Mount
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

templates = Jinja2Templates(directory='templates')


async def homepage(request):
    return templates.TemplateResponse('index.html', {'request': request})


async def testjson(request):
    return JSONResponse({'test': 'hello'})


routes = [
    Route('/', endpoint=homepage),
    Route('/json', endpoint=testjson),
    Mount('/static', StaticFiles(directory='static'), name='static')
]

app = Starlette(debug=True, routes=routes)
