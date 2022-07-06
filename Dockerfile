# syntax=docker/dockerfile:1
FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# where your code lives 
WORKDIR /code

COPY requirements.txt /code/

# run this command to install all dependencies  
RUN pip install -r requirements.txt  

# copy whole project to your docker home directory.
COPY . /code/

# port where the Django app runs  
EXPOSE 8000  

# start server  
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
