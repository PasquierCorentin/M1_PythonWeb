FROM python:3.8

WORKDIR /app

COPY . /app

ADD . /app

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 80

CMD [ "python", "./app/app.py" ]
