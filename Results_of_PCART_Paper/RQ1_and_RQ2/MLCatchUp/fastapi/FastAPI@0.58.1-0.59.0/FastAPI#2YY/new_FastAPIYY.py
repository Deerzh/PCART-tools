from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(debug=True, root_path_in_servers=True)
