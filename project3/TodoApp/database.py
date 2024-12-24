import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Load environment variables from .env file
load_dotenv()

# Extract password from environment variables
password = os.getenv('AIVEN_DB_PASSWORD')

SQLALCHEMY_DATABASE_URL =  f'postgres+psycopg2://avnadmin:{password}@pg-todoapp-fastapi-todoapplication.c.aivencloud.com:19044/defaultdb?sslmode=require'


# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:test1234!@localhost:5432/TodoApplicationDatabase'
# SQLALCHEMY_DATABASE_URL = 'postgresql://test:2CEPauv6iSHuxzcJemMWtyoIohx0zHWn@dpg-ctktce1opnds7382c1h0-a:5432/fastapidatabase_trla'
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:test1234!@127.0.0.1:3306/TodoApplicationDatabase'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
  