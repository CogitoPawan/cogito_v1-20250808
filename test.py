## tests/test_anomaly_detection.py

## Dockerfile

python3 -m unittest discover tests

docker build -t anomaly_detection_app .

docker run -d -p 8000:8000 anomaly_detection_app

[
        {
            "id": 5,
            "timestamp": "2023-01-29T00:00:00Z",
            "sales": 1000.0
        }
    ]

This completes the implementation of the anomaly detection system. The code is modular and maintainable, follows best practices, includes error handling and logging, and is ready for deployment and use in a production environment.