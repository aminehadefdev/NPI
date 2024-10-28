##Le fichier principal est le point d'entrée de l'application.


from fastapi import FastAPI
from fastapi.responses import FileResponse

from app.classs.ctrls.calculCTRL import calculCTRL
from app.classs.ctrls.dowloadCTRL import dowloadCTRL

app = FastAPI()

@app.get("/")
async def root():
    return {"message": ""}

@app.post("/{calcul}")
async def root(calcul):
    calc = calculCTRL()
    return {"message": calc.post(calcul)}

@app.get("/dowload", response_class=FileResponse)
async def root():
    dowload = dowloadCTRL()
    dataFile = dowload.get()
    return dataFile[0] + dataFile[1]
