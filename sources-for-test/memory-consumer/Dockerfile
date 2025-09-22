FROM python:3.11-slim

WORKDIR /app

COPY memory_consumer.py .

# Значения по умолчанию
ENV MEMORY_MB=100
ENV DELAY_SEC=1

CMD ["python", "memory_consumer.py"]
