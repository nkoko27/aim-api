from fastapi import FastAPI
import psycopg2

conn = psycopg2.connect("dbname= user= password= host= port=")
curr = conn.cursor()

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Hello Wolrd"}

@app.get('/get_all_employees')
async def get_all_employees():
    curr.execute("SELECT * FROM employee")
    records = curr.fetchall()
    print(records)
    return records