"""
FAST API DÖKÜMANLARIM
"""
# PART 2
# PATH PARAMETRELERİ
"""from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}"""

# http://127.0.0.1:8000/items/foo ADRESİNE BAKTIĞIMIZDA  {"item_id":"foo"} görüyoruz. yani url de verdiğimizi gördük. 1 yapsan 1 görürsün.

"""from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}"""
# TANIMLARKEN İTEM_İD NİN NE TİP OLACAĞINI DA BELİRTEBİLİRİZ. http://127.0.0.1:8000/items/foo BİDAHA DENEYİNCE HATAYA DÜŞÜYOR.
# HATANIN MESAJ KISMI: "msg": "Input should be a valid integer, unable to parse string as an integer",
# YANİ DİYOR Kİ BEN STRİNG DEĞİL İNT BEKLİYORUM. http://127.0.0.1:8000/items/1 VERİNCE DÜZGÜN ÇALIŞIYOR.
# http://127.0.0.1:8000/docs BİDAHA KONTROL EDİLİRSE ARTIK BİR GET İŞLEMİ OLDUĞUNU GÖRÜRÜZ. TRY DİYİNCE İTEMID SORAR.
# GİRİNCE GİRDİĞİN DEĞERE GÖRE ÇIKTI VERİR.str, float, bool GİBİ BAŞKA TÜRLERLE DE TANIMLAMA YAPABİLİRDİK.

# SIRALAMANIN ÖNEMİ:
# Yol işlemleri oluştururken sabit bir yol(PATH) GEREKTİREN DURUMLAR OLABİLİR. DİNAMİK PATHLARIN HER ZAMAN ÜSTÜNDE TANIMLANIR.
# ÖRNEĞİN /users/me GİBİ BİR SABİT YOL TANIMLAYALIM VE /users/{user_id} GİBİ BİR DİNAMİK YOL TANIMLAYALIM.
"""from fastapi import FastAPI

app = FastAPI()


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}"""

# BU ŞEKİLDE SABİT YOLUN YUKARDA OLMASI GEREKLİDİR. AKSİ TAKTİRDE /users/me İLE ÇAĞRI  YAPILINCA ME Yİ USER_ID SANAR.

# AYRICA AYNI PATH 2 KERE TANIMLANAMAZ. @app.get("/users/me") Yİ TANIMLADIYSAN Bİ TANE DAHA AYNISINDAN TANIMLAYAMAZSIN.

# Bir "yol" parametresi alan bir yol işleminiz varsa ancak "olası geçerli yol parametresi" değerlerinin önceden tanımlanmasını 
# istiyorsanız standart bir Python Enum kullanabilirsiniz. Enum'u İMPORT ET ve str ve Enum'dan miras alan bir alt sınıf oluştur
# str'den miras alarak API belgeleri, değerlerin string türünde olması gerektiğini bilecek ve doğru şekilde oluşturabilecektir.
# Daha sonra mevcut geçerli değerler olacak sabit değerlere sahip sınıf nitelikleri oluşturun.

"""from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}"""

# http://127.0.0.1:8000/docs KONTROL EDİLDİĞİNDE PATH PARAMETRESİ İÇİN KULLANILABİLECEK DEĞERLER (ALEXNET, RESNET, LENET)
# ÖNCEDEN BELİRLENDİĞİ İÇİN RAHATÇA GÖREBİLİYORUZ. YANİ BURADA KISACA "PATH İÇİNDE BİR MODEL_NAME ALDIK AMA ALDIĞIMIZ
# DEĞERLER ŞU 3 ÜNDEN BİRİ OLMAK ZORUNDA" OLAYINI GÖRMÜŞ OLDUK.
# if model_name is ModelName.alexnet: if model_name.value == "lenet": KISIMLARINDA İSE GELEN VERİYLE ELDEKİ VERİYİ NASIL KIYASLAYABİLECEĞİMİZİ GÖRDÜK.
# model_name.value == "lenet": BU ARKADAŞ YERİNE if model_name.value == ModelName.lenet.value BUNU DA KULLANABİLİRDİK.

# PATH(YOL) İÇEREN PATH PAREMETRELERİ:
# FARZEDELİM Kİ : /files/{file_path} ŞEKLİNDE PATH'IMIZ VAR. file_path İSE home/johndoe/myfile.txt
# ÖYLEYSE URLMİZ ŞUNA DÖNÜYOR: /files/home/johndoe/myfile.txt
# Doğrudan Starlette'deki bir seçeneği kullanarak, aşağıdaki gibi bir URL kullanarak bir yol içeren bir yol parametresi bildirebilirsiniz:
# /files/{file_path:path} Bu durumda parametrenin adı file_path olur ve son kısım olan :path, parametrenin herhangi bir yolla eşleşmesi gerektiğini söyler.

from fastapi import FastAPI

app = FastAPI()


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

# http://127.0.0.1:8000/files/hasan/dosya.jpg BU URLYE GİDİNCE GÖRÜLÜR Kİ files/ TEN SONRASINI PATH OLARAK BAŞARILI ŞEKİLDE ALDI.