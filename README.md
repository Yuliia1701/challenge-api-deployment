# challenge-api-deployment

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