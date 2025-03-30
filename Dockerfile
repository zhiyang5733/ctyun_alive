FROM python:3.12-slim

ENV LANG=C.UTF-8 TZ=Asia/Shanghai

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    fonts-wqy-microhei \
    fonts-wqy-zenhei \
    chromium \
    chromium-driver \
    wget \
    xvfb \
    xauth


COPY ./requirements.txt /app/requirements.txt
RUN pip install -U pip && pip install -r requirements.txt


COPY . .

ENV PYTHONPATH=/app


CMD ["python", "run.py"]