FROM python:3.9-slim

WORKDIR /app

COPY server.py .

EXPOSE 9999

ENV PYTHONUNBUFFERED=1

CMD ["python", "server.py"]
