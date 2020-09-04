from starlette.endpoints import HTTPEndpoint

from learn.settings.directory import templates


class Endpoint(HTTPEndpoint):
    async def get(self, request):
        return templates.TemplateResponse('index.html', {'request': request})
