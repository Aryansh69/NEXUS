import json
from fastapi import FastAPI
app=FastAPI()
with open("data.json","r") as file :
    sessions=json.load(file)
@app.get("/")
def home():
    return{"message":"SHIT IS ONLINE"}
@app.get("/progress")
def progress():
   return ("hello my name is aryansh")