FROM public.ecr.aws/docker/library/python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# COPY main.py .
# COPY life.py .
# COPY web ./web
COPY . /app

EXPOSE 8000

CMD ["python3","-m","uvicorn","main:app", "--host", "0.0.0.0", "--port", "8000"]

python3 -m uvicorn main:app --reload --host 0.0.0.0 --port 8000