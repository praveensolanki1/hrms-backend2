HRMS App:

A simple Human Resource Management System (HRMS) built with Django (backend) and React (frontend). It helps manage employees, attendance, and provides REST API endpoints.

Features:

*Employee management
*Attendance tracking
*REST APIs for frontend or external apps
*Works with PostgreSQL in production
*SQLite for local development
*Can be deployed with Docker on Render


Backend: Django, Django REST Framework, Gunicorn, psycopg2, WhiteNoise
Frontend: React.js
Database: PostgreSQL (Render), SQLite (local)
Deployment: Docker, Render


Environment Variables (Production)

* SECRET_KEY – Django secret key
* DEBUG – True or False
* ALLOWED_HOSTS – Your app URL, e.g., hrms-backend2-zpzt.onrender.com
* DATABASE_URL – PostgreSQL database URL

  ## Local Setup

1. Clone the repo:  
   
   git clone https://github.com/praveensolanki1/hrms-backend2.git
   cd hrms-backend2

2.Create a virtual environment:

python -m venv env
source env/bin/activate 
env\Scripts\activate  

3. Install dependencies:

pip install -r requirements.txt

4. Run database migrations:

python manage.py makemigrations
python manage.py migrate
5.
python manage.py runserver

6. Open locally: http://127.0.0.1:8000/api/
   
