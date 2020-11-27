import aiohttp
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app import is_alive_host


app = FastAPI()


@app.get('/healthz')
async def check_health_view(hostname: str):
    is_alive = await is_alive_host(hostname, app.client_session)
    return {
        'status': 'up' if is_alive else 'down'
    }


@app.on_event('startup')
async def handle_startup():
    app.client_session = aiohttp.ClientSession()


@app.on_event('shutdown')
async def handle_shutdown():
    await app.client_session.close()
