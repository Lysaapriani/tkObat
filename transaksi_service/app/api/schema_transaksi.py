def transaksiEntity(item) -> dict:
    return {
        "id_transaksi":str(item["_id"]),
        "kd_obat":item["kd_obat"],
        "quantity":item["quantity"],
        "harga":item["harga"],
        "total": item["total"]
    }

def transaksiEntity(entity) -> list:
    return [transaksiEntity(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]
