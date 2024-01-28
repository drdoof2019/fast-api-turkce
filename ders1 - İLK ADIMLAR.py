"""
FAST API DÖKÜMANLARIM
KURULUM İÇİN:
pip install "fastapi[all]"
YA DA (ALL DAN KASIT BUNLAR)
pip install fastapi
pip install "uvicorn[standard]"
BURADA UVİCORN BİLGİSAYARI SERVER OLARAK KULLANMAK İÇİN GEREKLİ
"""
# PART 1
# EN BASİT UYGULAMA:
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
# ÇALIŞTIRMAK İÇİN:
# uvicorn main:app --reload
# BENİM DOSYANIN ADI main.py değil ders1.py => uvicorn ders1:app --reload
# ŞİMDİ http://127.0.0.1:8000/ ADRESİNDE YAYINA BAŞLADIK LOKAL'DE
# LOKAL DEMEK İNTERNET ÜZERİNDEN ULAŞILAMAZ SADECE SENİN AĞINDAKİLER ULAŞABİLİR.)
# İLERİDE CANLIYA ÇEKMEK DİYE TABİR EDECEĞİMİZ DE İNTERNET ÜZERİNDEN HERKESİN ULAŞABİLECEĞİ ANLAMINA GELECEK.
# EN SONDAKİ --reload KISMI BU DOSYADA HER DEĞİŞİKLİK YAPIP KAYDETTİĞİMİZDE WEBSİTESİNİ OTOMATİK GÜNCELLEMESİ İÇİN
# ders1:app DA Kİ app İSE app = FastAPI() BURADKİ app İNSTANCESİ.
# (Bir evin tasarım planı,bir sınıfı ifade etsin(Class). Bu plandan inşa edilen tüm evler, 
# bu sınıfın nesneleridir(Object). Ve her bir ev de birer örnektir(Instance).) BİZ YİNEDE NESNE DİYELİM

# ŞİMDİ http://127.0.0.1:8000/docs ADRESİNE BAK
# BURADA DA YAPTIĞIN HTTP OPERASYONLARININ (GET POST IVIR ZIVIR) DETAYLARINI GÖRECEKSİN.

# PATH NEDİR?
# ÖRNEĞİN https://example.com/items/foo SİTESİNDE PATH DENEN ŞEY /items/foo OLACAKTIR.
# @app.get("/") KISMINDA PATH / YANİ ANASAYFA

# OPERATİON (OPERATÖR?, OPERASYON?, İŞLEM? TÜRKÇESİNDEN EMİN OLAMADIM) NEDİR?
# Buradaki işlem", HTTP "methodlarından" birine atıfta bulunur. METHODLAR: POST, GET, PUT, DELETE, OPTIONS, HEAD, PATCH, TRACE
# HTTP protokolünde, bu "methodlardan" birini (veya daha fazlasını) kullanarak her yolla iletişim kurabilirsiniz.
# API'ler oluştururken normalde belirli bir eylemi gerçekleştirmek için bu belirli HTTP methodlarını kullanırsınız.
# POST: veri oluşturmak için.  GET: veri okumak için.  PUT: veri güncellemek için.  DELETE: veri silmek için.
# BUNLAR ARTIK operations OLARAK ANILACAK. O ZAMAN @app.get("/") NE DEMEK?
# / PATH, get OPERATION
# @ İŞARETİ PYTHONDA DECORATOR DİYE ADLANDIRILIR. Onu bir fonksiyonun üstüne koyarsınız. Oldukça dekoratif bir şapka gibi (sanırım terimin geldiği yer burası).
# Bir "dekoratör" aşağıdaki FONKSİYONU alır ve onunla bir şeyler yapar. Bizim durumumuzda bu dekoratör FastAPI'ye aşağıdaki 
# fonksiyonun get işlemiyle / PATH'INA karşılık geldiğini söyler. Bu "PATH işlemi dekoratörüdür". @app.post() GİBİ DİĞERLERİ DE KULLANILABİLİR.
