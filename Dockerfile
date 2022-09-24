FROM python:3.10-slim AS base
RUN apt-get update && apt-get install --no-install-recommends --yes python3

ENV PYTHONUNBUFFERED=True

COPY app.py app.py
COPY requirement.txt requirement.txt

RUN pip install -r requirement.txt

CMD ["python3","-m","flask","run","--host","0.0.0.0","--port", "5000"]