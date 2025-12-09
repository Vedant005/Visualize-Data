FROM python:3.11-slim

# Prevent Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1

# Install system deps
RUN apt-get update && apt-get install -y build-essential

# Workdir
WORKDIR /app

# Copy requirements separately for caching
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy everything
COPY . .

# Expose backend port
EXPOSE 8000

# Start FastAPI using Gunicorn + Uvicorn workers
CMD ["gunicorn", "app.main:app", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000"]
