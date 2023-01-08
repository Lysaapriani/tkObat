from fastapi import FastAPI
from app.api.route_transaksi import transaksi

app = FastAPI()
app.include_router(transaksi, prefix="/transactions", tags=["transaksi Docs"])