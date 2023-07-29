# Build stage
FROM python:3.11.3-slim AS builder
WORKDIR /app

COPY api/requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt
RUN pip install nodeenv
RUN pip install nodejs-bin

COPY prisma prisma
RUN prisma generate

# Final stage
FROM python:3.11.3-slim
ENV PYTHONUNBUFFERED True
ENV APP_HOME /app
WORKDIR /app

COPY --from=builder /usr/local /usr/local
COPY --from=builder /root/.cache /root/.cache

COPY api .
COPY prisma prisma

EXPOSE $PORT

CMD ["sh", "-c", "prisma migrate deploy && uvicorn main:api --host 0.0.0.0 --port \"$PORT\" --workers 1 --log-level warning --no-access-log"]
