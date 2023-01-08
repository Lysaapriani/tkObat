from pydantic import BaseModel

class Transaksi(BaseModel):
    # id = id nya dari db user -> id transaksi ada lagi cek di schema
    id_user: str
    # nama_user: str
    kd_obat: str
    quantity: int
    nama_obat: str
    jenis_obat: str
    harga: int
    stok_after: int
    total: int