FROM python:3.6.7

COPY requirements.txt /app/
WORKDIR /app/
RUN pip install -r requirements.txt
COPY . /opt/app

CMD ['python', '-m', 'tornado.autoreload main.py']
