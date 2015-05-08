FROM ubuntu
MAINTAINER windfarer <windfarer@gmail.com>

RUN apt-get install -y python3 python3-pip
RUN pip3 install gunicorn

RUN pip3 install -r requirements.txt

RUN gunicorn -c gunicorn.py run:app

EXPOSE 20010