from fastapi import FastAPI
import json
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import requests
import uvicorn

# run python "$python main.py" & "$node index.js" at the same time for results

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

class Data(BaseModel):
    data: dict

@app.post("/test")
async def read_item(data:Data):
    user = 'test'
    # user = data.user
    # make reques
    f = open(user + ".txt", "w")
    f.write(json.dumps(data.data))
    f.close()
    return data.data
    
def main():
    url = 'https://ef75-144-9-80-252.ngrok.io/flights?date=2020-01-01'
    print("Hello World!")
    # data = requests.request("GET", url)
    # print(data.text)





if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)