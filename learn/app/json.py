from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse


class Endpoint(HTTPEndpoint):
    async def get(self, request):
        return JSONResponse({'test': 'hello'})
