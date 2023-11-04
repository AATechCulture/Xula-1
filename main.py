from typing import Union
from fastapi import FastAPI

import requests
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return main()

    
def main():
    url = 'https://ef75-144-9-80-252.ngrok.io/flights?date=2020-01-01'
    print("Hello World!")
    data = requests.request("GET", url)
    print(data.text)





if __name__ == '__main__':
    main()