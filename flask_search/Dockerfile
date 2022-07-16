FROM ubuntu:20.04

WORKDIR /usr/src/app

RUN apt-get update -y
RUN apt-get install python3-pip -y

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app", "--workers=5"]