from fastapi import FastAPI, Request
from app.routers import v1
import os
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


parent_dir_path = os.path.dirname(os.path.realpath(__file__))

app = FastAPI(
    title="DASHBOARD",
    description="This is a very fancy project, with auto docs for the API and everything",
    version="2.5.0",
    docs_url=None,
    redoc_url=None,
    openapi_url=None
)


api = FastAPI(
    title="My Super Project API",
    description="This is a very fancy project, with auto docs for the API and everything",
    version="2.5.0",
    openapi_url="/v1/openapi.json",
    docs_url="/v1/docs",
    redoc_url="/v1/redoc"
)

api.include_router(
    v1.router,
    prefix="/v1"
)

app.mount("/api", api)

@app.get('/', include_in_schema=False)
async def root(request: Request):
    return FileResponse('../frontend/dist/index.html', media_type='text/html')

app.mount("/static", StaticFiles(directory="../frontend/dist/static"), name='static')


async def default_route(scope, receive, send):
    response = FileResponse("../frontend/dist/index.html")
    await response(scope, receive, send)

app.router.default = default_route
