FROM python:3.12-slim

WORKDIR /app

COPY monitor.py .
COPY topology.json .

RUN pip install requests

EXPOSE 8000

CMD ["python", "monitor.py"]
