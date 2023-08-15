# challenge-api-deployment
## Mission objecttives
- Be able to deploy a machine learning model.
- Be able to create an API that can handle a machine learning model.
- Deploy an API to Render with Docker.

## The Mission
The real estate company "ImmoEliza" is really happy about the regression model. They would like to create an API to let their web-developers create a website around it.

## Installation
- fastapi
- pydantic
- uvicorn
- typing
- joblib
- pandas
- numpy
- Scikit-learn
- statsmodels

## File structure
* model
    * My_model.pkl
* preprocessing
    * cleaning_data.py
* predict
    * prediction.py
    * My_model.pkl
    * Encoded.pkl
* app.py --> API
* requirements.txt
* Dockerfile
* My_model.pkl
* Encoded.pkl

## Data structure
'''json
{
  "region": str,
  "property_type": str,
  "habitable_surface": int,
  "number_of_rooms": int,
  "has_terrace": str,
  "has_garden": str,
  "is_furnished": str,
  "has_swimming_pool": str,
  "has_open_fire": str
}

## Contributers
- Yuliia Dranishcheva
