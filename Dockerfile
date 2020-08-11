FROM python:3.8-slim
ENV NODE_ENV=development
WORKDIR /app

EXPOSE 5000

COPY ./entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
