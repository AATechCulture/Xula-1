import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
prompt = """pref = {"hot": Bool,(cold)bool,(humid)bool,(dry)bool]
         time_of_yr: [(winter)bool,(spring)bool,(summer)bool,)(fall)bool]
         Dairy: bool
         Gluten:bool
         Shellfish:bool
         Nuts:bool
         halaal:bool 
         Walkable: bool
         region: [(North America), (South America), (Carribean)bool, (ASia) bool,(Europe)bool, (Africa)bool, (Australia) bool]
         kid friendly: bool
         nightlife: bool} """
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": f"You are a Travel Assistant for an Airline, skilled in finding trips based on the user's preference as best as possible"},
        {"role": "user", f"content": """Can you fill out this form based on the following prompt using the city of Dallas, do not answer anything other than the filled out form. 
         Form: {temp pref: [(hot)Bool,(cold)bool,(humid)bool,(dry)bool]
         time_of_yr: [(winter)bool,(spring)bool,(summer)bool,)(fall)bool]
         Dairy: bool
         Gluten:bool
         Shellfish:bool
         Nuts:bool
         halaal:bool 
         Walkable: bool
         region: [(North America), (South America), (Carribean)bool, (ASia) bool,(Europe)bool, (Africa)bool, (Australia) bool]
         kid friendly: bool}
         nightlife: bool """}
    ]
)

print(completion.choices)