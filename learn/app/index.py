from starlette.responses import JSONResponse

from learn.settings.directory import templates


async def homepage(request):
    return templates.TemplateResponse('index.html', {'request': request})


async def testjson(request):
    return JSONResponse({'test': 'hello'})
