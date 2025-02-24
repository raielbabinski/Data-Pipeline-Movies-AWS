FROM python:3.11-slim

WORKDIR /data

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ingestao.py .

COPY movies.csv .

COPY series.csv .

CMD ["python", "ingestao.py"]

