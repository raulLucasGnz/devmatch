from fastapi import FastAPI

#instancia de FastApi
app = FastAPI()

@app.get("/")
def read_root():
    return{"message": "Hola, DevMatch está funcionando!"}
