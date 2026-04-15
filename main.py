from pathlib import Path

from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import asyncio
from life import make_grid, populate_grid_random, step

app = FastAPI()
WEB_DIR = Path(__file__).resolve().parent / "web"

grid = make_grid(100, 60)
populate_grid_random(grid, 0.2)


@app.get("/")
def index():
    return HTMLResponse((WEB_DIR / "index.html").read_text(encoding="utf-8"))


@app.websocket("/ws")
async def ws(ws: WebSocket):
    await ws.accept()

    global grid
    while True:
        grid = step(grid)
        await ws.send_json({"grid": grid})
        await asyncio.sleep(0.2)
