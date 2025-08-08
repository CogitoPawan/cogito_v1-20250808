anomaly_detection_project/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── sales_data.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── anomaly_detection.py
│   │   ├── notify.py
│   │   └── report.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── logger.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_anomaly_detection.py
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore

FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

fastapi
uvicorn
sqlalchemy
numpy
requests

# Anomaly Detection from Weekly Sales Data

## Project Overview
This project implements a system to identify anomalies in weekly sales data. The system detects unusual trading patterns promptly to aid in better decision-making, reduced revenue loss, improved operational efficiency, and enhanced customer satisfaction.

## Setup Instructions

1. **Clone the repository:**

2. **Create and activate a virtual environment:**

3. **Install dependencies:**

4. **Set up the database:**
    Update the `DATABASE_URL` environment variable in `app/config.py` with your PostgreSQL connection string. Then run the following commands to create the database tables:

5. **Run the application:**

6. **Run the tests:**

## Deployment with Docker

1. **Build the Docker image:**

2. **Run the Docker container:**

## API Endpoints

### `GET /anomalies`

Fetch the list of detected anomalies.

- **Response:**