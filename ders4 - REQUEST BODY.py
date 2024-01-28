"""
FAST API DÖKÜMANLARIM
"""
# PART 4
# REQUEST BODY

# BİR CLİENTTEN (ÖRNEĞİN BİR BROWSERDAN) KENDİ API'NE BİLGİ GÖNDERMEK İSTERSEN BU request body'DİR.
# AKSİ DURUM (API DEN BROWSER'A) İSE response body'DİR. YANİ APİ CLİENTE BİLGİ GÖNDERİR.
# request body OLSA DA OLUR OLMASA DA AMA response body KESİN OLMAK ZORUNDA DENEBİLİR.

# VERİ GÖNDEREBİLMEK İÇİN POST, PUT, DELETE, PATCH HTTP KURALLARINDAN BİRİNİ KULLANMAK LAZIM. GENELDE HEP POST KULLANILIR.
# request body OLUŞTURMAK İÇİN pydantic KÜTÜPHANESİNİ KULLAN. BU KÜTÜPHANE PYTHONDA EN YAYGIN KULLANILAN VERİ DOĞRULAMA KÜTÜPHANESİ.

"""from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None # opsiyonel yaptık
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item"""

"""from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None # opsiyonel yaptık
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    # PYDANTIC SAYESINDE YAPABILECEKLERİMİZE BAKALIM
    item_dict = item.dict() # .dict() eskimiş, .model_dump() kullanmak gerekiyormuş. bla bla
    if item.tax:
        item_price_with_tax = item.price + item.tax
        item_dict.update({"item_price_with_tax":item_price_with_tax})
    return item"""

"""from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}"""

# BURADA DA PATH İLE REQUEST BODY PARAMETRELERİNİ FAST APİ NİN ÇOK AYIRABİLDİĞİNİ GÖRÜYORUZ BLA BLA.

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

# Request body + path + query ÖRNEĞİ