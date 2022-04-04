from imp import reload
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")

def read_root():
    return {"Hello": "Word"}

@app.get("/whoami")
def whoami():
    return "I am a iron man"

@app.get("/deneme")
def deneme():
    return "deneme"


#bu ifade veya consoldan kullanılabilir.
if __name__ == "__main__": # bu kısım olmazsa paketi import ettiğimiz an tüm kodlar çalışır.
    #main:app olduğu için dosyanın adı main olmalı.
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
    
    
