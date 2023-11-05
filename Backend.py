from typing import Union

from fastapi import FastAPI

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "http://localhost:8000"
#     ],
#     allow_credentials=True,
#     allow_methods=[""],
#     allow_methods=[""]
# )

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return 


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# user prefernces will be in the form 
# pref = {temp pref: [(hot)True,(cold)False,(humid)True,(dry)False]
#         time_of_yr: [(winter)True,(spring)True,(summer)False,)(fall)False]
#         Dairy: bool
#         Gluten:bool
#         Shellfish:bool
#         Nuts:bool
#         halaal:bool 
#         Walkable: bool
#         region: [bool, bool,bool, bool,bool]
#         kid friendly: bool
#         nightlife: bool}
                     
def detail_information(location):
    return dict of matches

def trip_match(dict,user_preferences):
    return 
