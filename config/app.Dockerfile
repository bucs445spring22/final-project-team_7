FROM python:3.9

WORKDIR /var/app

# Dependencies
RUN pip install --upgrade pip
COPY ./config/app_requirements.txt /var/tmp/requirements.txt
RUN pip install -r /var/tmp/requirements.txt
COPY ./config/gunicorn.conf.py /var/gunicorn.conf.py
COPY ./app /var/app


