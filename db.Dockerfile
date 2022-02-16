FROM python:3.9-alpine

WORKDIR /var/db

# Dependencies
RUN pip install --upgrade pip
COPY ./db/requirements.txt /var/tmp/requirements.txt
RUN pip install -r /var/tmp/requirements.txt

COPY ./db /var/db

#CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
CMD ["ash"]