FROM python:3.7

WORKDIR /app
COPY . /app

# Run email_server.py when the container launches
ENTRYPOINT ["python", "email_server.py"]