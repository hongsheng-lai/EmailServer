FROM python:3.8
WORKDIR /app
COPY . /app
CMD ["python", "main.py", "--config", "config.json"]