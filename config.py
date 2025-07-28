import os
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do .env

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://chamados-db_owner:npg_9VCOSDiX3yJP@ep-restless-grass-ac9yjj45-pooler.sa-east-1.aws.neon.tech/chamados-db?sslmode=require&channel_binding=require'
    SQLALCHEMY_TRACK_MODIFICATIONS = False