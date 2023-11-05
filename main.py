from fastapi import FastAPI
import json
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import city_data
import requests
import uvicorn

import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
# run python "$python main.py" & "$node index.js" at the same time for results








    
def main():
    cities_to_desc = {}
    flights = []

    url = 'https://ef75-144-9-80-252.ngrok.io/flights?date=2020-01-01'
    print("Hello World!")
    # data = requests.request("GET", url)
    # print(data.text)


    def city_image(city):
        response = openai.Image.create(
        prompt= f"Provide a scenic image of {flight} that can be advertised for airlines.",
        n=1,
        size="1024x1024" 
        )
        return response



    def city_description(city,user_pref):

        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are acting as a travel assitant, skilled in selling a destination to a customer."},
            {"role": "user", "content": f"Provide a description of {city} based on {user_pref}. Only output a short 3 sentence pitch, selling the customer the destination, referencing some of their preferneces in the pitch."}
        ]
        )


        return completion.choices[0].message
    


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
    return data



if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)