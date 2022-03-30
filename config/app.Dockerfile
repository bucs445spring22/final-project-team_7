# Build: docker build -t app
# Run: docker run -dit -p 80:5000 app

FROM python:3.9

WORKDIR /var/app

# Dependencies
RUN pip install --upgrade pip
COPY ./app/app_requirements.txt /var/tmp/requirements.txt
RUN pip install -r /var/tmp/requirements.txt

COPY ./app /var/app

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
