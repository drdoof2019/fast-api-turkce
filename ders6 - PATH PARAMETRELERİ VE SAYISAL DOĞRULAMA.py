"""
FAST API DÖKÜMANLARIM
"""
# PART 6
# PATH PARAMETRELERİ VE SAYISAL VALİDASYONLARI
# https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/


"""from typing import Annotated
from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results"""

# QUERY DE OLDUĞU GİBİ PATH'TA DA ÇEŞİTLİ KONTROLLER YAPILABİLİR. QUERY' DE KULLANILAN TÜM PARAMETRELERİ PATH'DA DA KULLANABİLİRSİN.
# BURADA ÖNEMLİ OLAN NOKTA PATH PARAMETRESİ HER ZAMAN REQUIRED'DİR. QUERY'DE OLDUĞU GİBİ NONE VERİLSE YADA DEFAULT DEĞER BAŞKA BİRŞEY VERİLSE YİNE DE ZORUNLUDUR.
# AYRICA ANOTATED KULLANIRKEN PATH VEYA QUERY PARAMETRELERİNİN HANGİSİNİN ÖNCE YAZILDIĞI ÖNEMLİ DEĞİLDİR. q YU item_id'NİN ÖNÜNE DE TANIMLAYABİLİRSİN.

from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=1, le=1000)], q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# NUMARA KONTROLLERİ: HEM QUERY HEM PATH'DA BÜYÜK EŞİTTİR GİBİ KONTROLLER YAPILABİLİR. ge=1 "GREATER THAN OR EQUAL" PARAMETRESİNİ AÇMAK ANLAMINA GELİYOR. YANİ item_id 1 YADA 1 DEN BÜYÜK OLACAK. AMA 1000'DEN KÜÇÜK OLACAK
# gt: GREATER THAN (BÜYÜKTÜR),   le: LESS THAN OR EQUAL (KÜÇÜK EŞİTTİR).

