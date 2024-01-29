"""
FAST API DÖKÜMANLARIM
"""
# PART 3
# QUERY(SORGU) PARAMETRELERİ

"""from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]"""

# async def read_item(skip: int = 0, limit: int = 10) KISMI DİKKAT EDİLİRSE BİR YOL DEĞİL SORGU BELİRTİR.
# SORGU URL'DE ? İLE GELEN KEY-VALUE ÇİFTLERİ KÜMESİDİR VE & İLE BİRBİRİNDEN AYRILIR.
# MESELA http://127.0.0.1:8000/items/?skip=0&limit=10 'DA SORGU KISMI ?skip=0&limit=10. CEVAP OLARAK ŞU DÖNÜYOR:
# [{"item_name":"Foo"},{"item_name":"Bar"},{"item_name":"Baz"}] NEDEN ÇÜNKÜ fake_items_db[0:10] DEMİŞ OLDUK. YANİ İLK 10 ELEMANI YAZDIR DEDİK.
# http://127.0.0.1:8000/items/?skip=1&limit=2 DESEK BU SEFER 1. ELEMANDAN BAŞLAYIP 2 ELEMAN YAZDIRIR.
# http://127.0.0.1:8000/items/?skip=20 DENERSEK SKIP'İ 20 VERDİK AMA LİMİT DEFAULT OLARAK 10 (ÇÜNKÜ VERMEDİK)
# ÖYLEYSE BOŞ LİSTE DÖNER YANİ HİÇBİR ŞEY YAZDIRMAZ

# OPSİYONEL PARAMETRELER
# isteğe bağlı sorgu parametrelerini varsayılan olarak NONE olarak AYARLAYABİLİRSİN:
"""from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}"""
# BU DURUMDA q OPSİYONELDİR VE DEFAULT OLARAK NONE'DUR. AMA KULLANICI GİRECEKSE DE GİRDİĞİ DEĞER str OLARAK ALINIR.
# http://127.0.0.1:8000/items/1?q=asd BU ŞEKİLDE GİDERSEN item_id 1 VE q DEĞERİ asd DİR ANCAK
# http://127.0.0.1:8000/items/1 BÖYLE GİDERSEN q DEĞERİ YOKTUR (NONE)

"""from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if short:
        item.update(
            {"description": "UZUN AÇIKLAMASI OLAN MÜKEMMEL BİR ÜRÜN"}
        )
    return item"""

# http://127.0.0.1:8000/items/foo?q=qdegeri&short=yes (BURADA YES YERİNE: 1, True, true, on KULLANILABİLİRDİ. HEPSİ BOOLEN TRUE DEMEK)
# ÇIKTISI: {"item_id":"foo","q":"qdegeri","description":"UZUN AÇIKLAMASI OLAN MÜKEMMEL BİR ÜRÜN"}

"""from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item"""

# BU ÖRNEKTE GÖRÜLDÜĞÜ GİBİ AYNI ANDA BİRDEN FAZLA PATH PARAMETRESİ VE/VEYA QUERY PARAMETRESİ KULLANILABİLİR.
# ÜSTELİK HERHANGİ BİR SIRADA KULLANILABİLİR. FAST APİ DOĞRU SIRAYA SOKACAKTIR.
# (YANİ ÇAĞIRIRKEN ÖNCE q=qdegeri Mİ YAZDIN short'U MU YAZDIN UMURSAMAZ.')

"""from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item"""

# QUERY PARAMETRESİNİ GİRİLMESİ GEREKLİ OLARAK TANIMLAMA İŞLEMİ.
# http://127.0.0.1:8000/items/foo-item GİDERSEN HATA ALIRSIN. "msg": "Field required" DER. YANİ needy OLARAK BİR STR YOLLAMAN LAZIM DER.
# http://127.0.0.1:8000/items/foo-item?needy=sooooneedy BUNU VERİRSEN GÜZELCE ÇALIŞIR.

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

# BURADA needy GEREKLİ, skip DEFAULT DEĞERE SAHİP, limit İSE OPSİYONEL (OLSA DA OLUR OLMASADA) OLARAK TANIMLAMIŞ.