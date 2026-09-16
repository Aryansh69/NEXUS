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
    total_session=len(sessions)
    print("Your total study time is")
    total_time=0
    for i in sessions:
        total_time +=i["minutes"]
    total_confidence=0
    for i in sessions:
        total_confidence+=i["confidence"]
    avg_confidence = total_confidence / total_session
    return {
    "total_sessions": total_session,
    " total_minutes ": total_time,
    "avg_confidence":avg_confidence
}
            