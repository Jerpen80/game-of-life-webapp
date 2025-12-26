from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import asyncio
from life import make_grid, populate_grid_random, step

app = FastAPI()

grid = make_grid(40, 30)
populate_grid_random(grid, 0.2)


@app.get("/")
def index():
    return HTMLResponse(open("web/index.html").read())


@app.websocket("/ws")
async def ws(ws: WebSocket):
    await ws.accept()

    global grid
    while True:
        grid = step(grid)
        await ws.send_json({"grid": grid})
        await asyncio.sleep(0.2)