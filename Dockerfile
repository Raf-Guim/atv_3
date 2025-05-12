FROM python:3.12-slim

WORKDIR /app

COPY app.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]
