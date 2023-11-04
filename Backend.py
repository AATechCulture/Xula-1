from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# hwo to setup form data from fast api

# user prefernces will be in the form {
# pref = {temp pref: [(hot)Bool,(cold)bool,(humid)bool,(dry)bool]
#         time_of_yr: [(winter)bool,(spring)bool,(summer)bool,)(fall)bool]
#         Dairy: bool
#         Gluten:bool
#         Shellfish:bool
#         Nuts:bool
#         halaal:bool 
#         Walkable: bool
#         region: [(North America), (South America), (Carribean)bool, (ASia) bool,(Europe)bool, (Africa)bool, (Australia) bool]
#         kid friendly: bool
#         nightlife: bool}

# using a dictionary key of the city name and then checking if the list associated has the given value, shortening the list of usable cities as we go 
# ex: {Houston }
                     
def detail_information(location):
    # use the following template to get the preferences through openAI: Can you fill out this form(preferences) based on this city, do not answer anything other than the filled out form
    return dict of matches

def trip_match(dict,user_preferences):
    # takes in dictionary for user preferences
    # then look through look through prefs list, creating a list of cities that fit first pref, preferneces can be null so if null continue
    # once list is created, we loop through preferences eliminating destinations that don't match
    # once finished loop of preferneces, return the list of cities that fit description, as well as mock flight data for trips that are underperforming to help mitigate buisness loss during preferred time.(mauybe deals on those flights?)
