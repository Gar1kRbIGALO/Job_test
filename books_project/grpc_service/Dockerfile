
FROM python:3.9-slim

WORKDIR J:\job_test2\books_project\grpc_service

COPY ../requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 50051


CMD ["python", "grpc_server.py"]
