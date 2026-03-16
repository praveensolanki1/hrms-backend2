FROM python:3.12-slim

WORKDIR /app

COPY hrms_django/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY hrms_django/ .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "hrms_django.wsgi:application", "--bind", "0.0.0.0:8000"]