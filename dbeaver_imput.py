import os
from dotenv import load_dotenv
import pymysql
import pandas as pd
from sqlalchemy import create_engine, text

# read_csv
data = pd.read_csv('bank.csv')
df=data.head()
df

# import os.getenv()
user= os.getenv("DB_USER")
passwd= os.getenv("DB_PASSWD")
host= os.getenv("DB_HOST")
port= os.getenv("DB_PORT")

db_name= input().strip()
tb_name= input().strip()

# db engine 연결
engine = create_engine(f"mysql+pymysql://{user}:{passwd}@{host}:{port}")
with engine.connect() as connection:
    connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))

# DataFrame을 SQL 테이블로 저장
df.to_sql(tb_name, con=engine, if_exists='replace', index=False)
