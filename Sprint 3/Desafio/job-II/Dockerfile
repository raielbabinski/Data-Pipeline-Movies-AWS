FROM python:3.11-slim

WORKDIR /jobb

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "job.py"]