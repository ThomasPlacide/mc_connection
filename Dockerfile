FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN mkdir -p /app/logs /app/status
EXPOSE 5000
WORKDIR /app/app
CMD ["python3", "app.py"]