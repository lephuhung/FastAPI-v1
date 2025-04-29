# pull the official docker image
FROM python:3.10-slim

# set work directory
WORKDIR /app

# Cập nhật danh sách gói và cài đặt netcat, sau đó xóa cache để giữ image nhỏ gọn
RUN apt-get update && apt-get install -y --no-install-recommends netcat-openbsd && rm -rf /var/lib/apt/lists/*

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
# RUN pip install -r requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# copy project
COPY . .
