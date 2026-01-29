FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml .
COPY code_agent ./code_agent

RUN pip install --no-cache-dir .

ENTRYPOINT ["code-agent"]
