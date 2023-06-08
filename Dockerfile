FROM ubuntu:22.04
FROM python:3.10
# Update the package manager and install Python 3.10
RUN apt-get update && apt-get install -y python3.10

#RUN mkdir /app
#RUN mkdir /app/model
#COPY model/My_model.pkl /app/model/My_model.pkl
#RUN mkdir /app/preprocessing
#COPY preprocessing/cleaning_data.py /app/preprocessing/cleaning_data.py
#RUN mkdir /app/predict
#COPY predict/prediction.py /app/predict/prediction.py

WORKDIR /app
COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt
COPY My_model.pkl /app/My_model.pkl
COPY Encoded.pkl /app/Encoded.pkl
COPY prediction.py /app/prediction.py
COPY cleaning_data.py /app/cleaning_data.py

# Install the Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose the port that your FastAPI application is listening on
EXPOSE 5000

# Run the FastAPI application using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]