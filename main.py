from fastapi import FastAPI
from backend.app.routers import users


#instancia de FastApi
app = FastAPI()

app.include_router(users.router)

#prueba
@app.get("/")
def read_root():
    return{"message": "Hola, DevMatch está funcionando!"}
