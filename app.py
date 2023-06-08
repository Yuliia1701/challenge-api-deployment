from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Literal
from prediction import predict
import uvicorn

class Property(BaseModel):
    region: str
    property_type: str
    habitable_surface: float
    number_of_rooms: int
    has_terrace: str
    has_garden: str
    is_furnished: str
    has_swimming_pool: str
    has_open_fire: str
    
app = FastAPI()

# Route
@app.get('/')
def get_request():
    return "status alive"

@app.post("/prediction")
def price_prediction(data_input: Property):
    try:
        # my prediction - with my model
        prediction = predict(data_input)
        # dict for the response
        response = {'prediction': prediction}

        return response
  
    except KeyError as e:
        raise HTTPException(status_code = 500, detail= str(e))

description =  {"How to use": {
                        "region": "Brussels or Flanders or Wallonie",
                        "property_type": "HOUSE or APARTEMENT",
                        "habitable_surface": "requared amount of square meter for instance - 95",
                        "number_of_rooms": "requared number of rooms for instance - 3",
                        "has_terrace": "'Yes' or 'No'", 
                        "has_garden": "'Yes' or 'No'",
                        "is_furnished": "'Yes' or 'No'",
                        "has_swimming_pool": "'Yes' or 'No'",
                        "has_open_fire": "'Yes' or 'No'",
    }}

# Route
@app.get('/description')
def get_description():
    return description


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)