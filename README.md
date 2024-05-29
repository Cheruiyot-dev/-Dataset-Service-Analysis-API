# Dataset Analysis Service
This is a learning project aimed at exploring FastAPI, Celery, and containerization using Docker and Docker Compose. 
Not intended for production use!.
This is a FastAPI-based web service that allows users to upload CSV files containing datasets, which are then processed and analyzed asynchronously in the background using Celery for task queuing. 
The analysis results are then persisted in a PostgreSQL database for later retrieval.
# Features
- File Upload: Users can upload CSV files containing datasets through a REST API endpoint.
- Data Validation: Uploaded CSV files are validated to ensure they are well-formed and compatible with the analysis process.
- Asynchronous Task Processing: The analysis of uploaded datasets is offloaded to Celery workers running as background tasks,
-  ensuring that the main application remains responsive and available for handling new requests.
- Task Queuing: Celery is integrated with Redis as the message broker and result backend, providing a reliable and scalable task queuing system.
- Data Analysis: The uploaded datasets are analyzed using pandas, a powerful data manipulation and analysis library for Python.
-  The analysis includes computing summary statistics and other relevant metrics.
- Result Storage: The analysis results are stored in a PostgreSQL database for later retrieval or further processing.
- Containerization: The entire application is containerized using Docker and Docker Compose, making it easy to deploy and scale across different environments.
# Technologies Used
- Python
- FastAPI
- Celery
- Redis
- PostgreSQL
- Docker
- Docker Compose
