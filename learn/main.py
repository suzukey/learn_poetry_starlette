from starlette.applications import Starlette
from starlette.responses import JSONResponse

app = Starlette(debug=True)


@app.route('/')
async def home(request):
    return JSONResponse({'test': 'hello'})
