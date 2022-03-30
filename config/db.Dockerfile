FROM python:3.9

WORKDIR /var/db

# Dependencies
RUN pip install --upgrade pip
COPY ./db/db_requirements.txt /var/tmp/requirements.txt
RUN pip install -r /var/tmp/requirements.txt

COPY ./db /var/db

#CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
CMD ["sh"]