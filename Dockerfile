FROM python:3.7-slim
WORKDIR /app
COPY requirements.txt .
COPY main/ .
RUN pip3 install -r requirements.txt --no-cache-dir
CMD ["gunicorn", "main.wsgi:application", "--bind", "0.0.0.0:8000"]
