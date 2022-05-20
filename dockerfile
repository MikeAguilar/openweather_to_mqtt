FROM python:3.8

COPY ./requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./app/main.py /app/main.py
COPY ./app/example-config.py /app/config.py

CMD [ "python", "/app/main.py" ]