FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY hrms_django/manage.py .
COPY hrms_django/hrms_django ./hrms_django
COPY hrms_django/employees ./employees
COPY hrms_django/attendance ./attendance
COPY hrms_django/dashboard ./dashboard

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "hrms_django.wsgi:application", "--bind", "0.0.0.0:8000"]