FROM python:3.9-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

RUN useradd -m ctf

COPY --chown=ctf:ctf server.py .

USER ctf

EXPOSE 9999

CMD ["python", "server.py"]
