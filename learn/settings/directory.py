from os.path import join
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates


def dir(dirname):
    return join('learn', dirname)


templates = Jinja2Templates(directory=dir('templates'))
static = StaticFiles(directory=dir('static'))
