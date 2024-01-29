"""
FAST API DÖKÜMANLARIM
"""
# PART 5
# QUERY PARAMETRELERİ VE STRİNG VALİDASYONLARI
# https://fastapi.tiangolo.com/tutorial/query-params-str-validations/

"""from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results"""

# BU ÖRNEKTE DAHA ÖNCE GÖRDÜĞÜMÜZ GİBİ q DEĞERİ OPSİYONEL.

"""from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results"""

# BURADA İSE q: str | None = None YAPISI q: Annotated[str | None] = None BUNA DÖNÜŞÜYOR. ANLAM AYNI
# q STR OLABİLİR YA DA NONE OLABİLİR. DEFAULT OLARAK NONE. Annotated YAPISI SAYESİNDE QUERY EKLEYELİM
# SONUÇ OLARAK async def read_items(q: Annotated[str | None, Query(max_length=50)] = None): BUNU ELDE ETMİŞ OLUYORUZ. DEFAULT VALUE HALA NONE OLDUĞUNU GÖZDEN KAÇIRMAYALIM.
# BU SAYEDE EK BİR DOĞRULAMA KOYMUŞ OLDUK (50 KARAKTER DOĞRULAMASI)
# http://127.0.0.1:8000/docs girip q OLUŞTURDUĞUMUZDA 50 KARAKTERDEN FAZLA İSE msg": "String should have at most 50 characters" HATASI VERDİĞİ GÖRÜLÜR.


"""from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: str | None = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results"""

# ESKİ VERSİYONDA BÖYLE KULLANILIYORDU. ANCAK ÜSTTEKİ YENİ VERSİYONUN AVANTAJLARI DAHA FAZLA OLDUĞU İÇİN BU YAPI ARTIK KULLANILMAMALI.
# q: Annotated[str, Query()] = "rick" QUERY İÇİN DEFAULT DEĞERİ NONE YERİNE RİCK VERDİK

"""from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Annotated[str | None, Query(min_length=3, max_length=50)] = None
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results"""

# BURADA İSE HEM MAX HEM MİN LENGHT VERDİK.

"""from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results"""

# AYRICA REGULAR EXPRESSİON (REGEX) İLE PATTERN KONTROL YAPABİLİRİZ. REGEX BİLMEYENLER İÇİN ^ BUNUN SAĞINDAKİLER İLE BAŞLAYAN YANİ BU DURUMDA fixedquery TEXT'İNİ İÇEREN VE $ İŞARETİ BİTİŞ ANLAMINA GELİR.
# YANİ TAM OLARAK fixedquery METNİNİ ARIYORUZ. REGEX ÇOĞU İNSAN İÇİN ZOR BİR KONUDUR. FAST APİ DESTEKLİYOR ANCAK KULLANMAK ZORUNDA DEĞİLİZ.
# Pydantic V2 GÜNCEL OLARAK KULLANILIYOR ANCAK BUNDAN ÖNCE pattern= YERİNE regex= KULLANILIYORDU (V1'DE)

"""from fastapi import FastAPI, Query
from typing_extensions import Annotated

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results"""

# BURADA İSE q DEĞERİ İÇİN YİNE ANNOTATED VE QUERY İLE İSTEDİĞİMİZ KOŞULLARI EKLEYEBİLİRİZ ANCAK DEFAULT DEĞER VERMEDİĞİMİZ İÇİN ZORUNLU HALE GELDİ.

"""from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)] = ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results"""

# PYTHONDA Ellipsis DENEN BİR OLGU VAR ... BU ANLAMA GELİYOR. YİNE q DEĞERİNİN ZORUNLU OLDUĞU ANLAMINA GELİYOR. YANİ BU ÖRNEKTE q DEĞERİNİN MİN UZUNLUĞU 3 KARAKTER OLACAK, STR OLACAK VE GİRİLMESİ ZORUNLU ANLAMINA GELİYOR.

"""from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3)] = ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results"""

# BURADA İSE q DEĞERİ NONE DEĞERİ DE ALABİLİR, ANCAK GİRİLMESİ ZORUNLU. YANİ DEFAULT OLARAK NONE VERMEDİK ANCAK KULLANCII NONE OLARAK DA GİRİŞ YAPABİLİR DEMEK.


# QUERY PARAMETRESİNDE BİRDEN FAZLA DEĞER DE ALDIRABİLİRİZ.
"""from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items"""

# http://localhost:8000/items/?q=foo&q=bar BÖYLE BİR URL İLE ÇAĞIRDIĞIMIZDA q NUN LİSTE OLDUĞUNU VE HEM FOO HEM BAR STRLERİNİ BARINDIRDIĞINI GÖREBİLİRİZ

"""from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[list[str], Query()] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items"""

# AYNI ÖRNEK ANCAK BU KEZ DEFAULT VALUE OLARAK LİSTE ELEMANLARI VERİLDİ. YANİ HİÇBİR STR GİRİLMEZSE DEFAULT OLARAK FOO,BAR OLAN LİSTE DÖNECEK

"""from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[list, Query()] = []):
    query_items = {"q": q}
    return query_items"""
# BU ŞEKİLDE list DİREKT OLARAKTA KULLANILABİLİR. ANCAK BU DURUMDA FAST APİ q PARAMETRESİNDE VERİLEN DEĞERİN STR Mİ INT Mİ VS OLDUĞUNU KONTROL ETMEZ. NE GELİRSE ALIR.


from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# QUERY'E TITLE, DESCRIPTION EKLENEBİLİR. deprecated=True İFADESİ İLE DE BU query'Yİ HALA KULLANAN İNSANLARA ARTIK KULLANIMDAN KALDIRILDIĞI BİLDİRİLEBİLİR.