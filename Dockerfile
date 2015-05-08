FROM ubuntu
MAINTAINER windfarer <windfarer@gmail.com>

ADD sources.list /etc/apt/sources.list
ADD . /var/www/flow/
WORKDIR /var/www/flow

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install gunicorn

RUN pip3 install -r requirements.txt

ENTRYPOINT gunicorn -c gunicorn.py run:app

EXPOSE 20010