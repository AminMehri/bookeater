FROM python:3.8

ENV PYTHONUNBUFFERED 1

# Set working directory
RUN mkdir /backend
WORKDIR /backend
COPY . /backend

# Installing requirements
ADD ./requirements.txt /backend
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "--chdir", "backend", "--bind", ":8000", "backend.wsgi:application"]
