# Base image — Python 3.11
FROM python:3.11-slim

# Working directory set karo
WORKDIR /app

# Requirements pehle copy karo (caching ke liye)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Baaki sab copy karo
COPY . .

# Port expose karo
EXPOSE 8000

# App start karo
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
