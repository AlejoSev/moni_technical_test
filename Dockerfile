FROM python:3.12.3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY backend/ .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]