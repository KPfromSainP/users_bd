FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN /bin/sh -c pip install --no-cache-dir -r requirements.txt && rm requirements.txt

COPY . .

COPY alembic.ini .

COPY migrations migrations

CMD python3 main.py
