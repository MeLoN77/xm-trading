from fastapi import FastAPI, WebSocket
from trade_xm_app.routers import orders
from trade_xm_app.websocket import websocket_endpoint

app = FastAPI()

app.include_router(orders.router)


@app.websocket("/ws")
async def websocket_handler(websocket: WebSocket):
    await websocket_endpoint(websocket)


@app.on_event("startup")
async def startup():
    pass


@app.on_event("shutdown")
async def shutdown():
    pass
