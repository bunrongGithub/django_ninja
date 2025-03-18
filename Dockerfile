#Use an official Python runtime as the base image
FROM python:3.10-slim
#Set the working dir inside the container
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYECODE 1

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

COPY . /usr/src/app/
#Expose port 8000 for the django app
EXPOSE 8000

#Set the env variable for Django to know it's running in production
ENV DJANGO_SETTING_MODULE=DjangoProject.settings.production
#Command to run the Django server
CMD ["python","manage.py","runserver","127.0.0.1:8000"]
