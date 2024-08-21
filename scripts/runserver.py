import os
os.system("python manage.py makemigrations")
os.system("python manage.py migrate")
os.system("python manage.py createsuperuser")
os.system("python manage.py runserver 127.0.0.1:8000")
