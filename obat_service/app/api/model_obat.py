from pydantic import BaseModel

class Obat(BaseModel):
    kd_obat: str
    nama_obat: str
    jenis_obat: str
    harga: int
    stok: int 