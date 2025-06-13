from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

#Carga variables de .env
load_dotenv()
#URL conexion a la BDD
DATABASE_URL = os.getenv("DATABASE_URL")
#Motor de SQLAlchemy
engine = create_engine(DATABASE_URL)
#Sesiones de conexión a la BDD
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#Define clase base
Base = declarative_base()