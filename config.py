import os
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do .env

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
