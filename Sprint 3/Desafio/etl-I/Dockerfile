FROM python:3.11-slim

WORKDIR /etl

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "etl.py"]

