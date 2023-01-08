from fastapi import APIRouter
from app.api.model_transaksi import Transaksi 
from app.api.db import conn 
from app.api.db import dbObat
# from app.api.db import dbUser
from app.api.schema_transaksi import serializeDict, serializeList
from bson import ObjectId
transaksi = APIRouter() 

# localhost -> GET

@transaksi.get('/')
async def find_all_transaksi():
    return serializeList(conn.transactions.transaksi.find())

# transactionshost/{T001} -> GET 

@transaksi.get('/{id}')
async def find_one_transaksi(id):
    return serializeDict(conn.transactions.transaksi.find_one({"_id":ObjectId(id)}))

@transaksi.post('/')
async def create_transaksi(transaksi: Transaksi):
    # dbUser.users.user.find_one({"_id":transaksi.id_user}, {
    #     transaksi.nama_user : 
    # })

    conn.transactions.transaksi.insert_one(dict(transaksi))
    dbObat.obats.obat.find_one_and_update({"kd_obat":transaksi.kd_obat}, {
       "$set": {"stok": transaksi.stok_after}
    })
    return serializeList(conn.transactions.transaksi.find())

# @transaksi.put('/{id}')
# async def update_transaksi(id,transaksi: Transaksi):
#     conn.transactions.transaksi.find_one_and_update({"_id":ObjectId(id)},{
#         "$set":dict(transaksi)
#     })
#     return serializeDict(conn.transactions.transaksi.find_one({"_id":ObjectId(id)}))

@transaksi.delete('/{id}')
async def delete_transaksi(id):
    return serializeDict(conn.transactions.transaksi.find_one_and_delete({"_id":ObjectId(id)}))
