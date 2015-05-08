FROM ubuntu
MAINTAINER windfarer <windfarer@gmail.com>

ADD sources.list /etc/apt/sources.list
ADD . /var/www/flow/
WORKDIR /var/www/flow

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y mongodb
RUN mkdir -p /data/db/

RUN pip3 install gunicorn

RUN pip3 install -r requirements.txt

ENTRYPOINT service mongodb start && gunicorn -c gunicorn.py run:app

EXPOSE 20010