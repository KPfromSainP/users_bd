FROM python:slim

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD uvicorn main:app --port ${APP_PORT}