FROM python:3.10
# Update the package manager and install Python 3.10
RUN apt-get update && apt-get install -y python3.10

RUN mkdir /app

WORKDIR /app

COPY . /app

# Install the Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Run the FastAPI application using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]