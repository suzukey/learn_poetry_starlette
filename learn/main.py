from starlette.applications import Starlette

from learn.settings.routes import routes

app = Starlette(debug=True, routes=routes)
