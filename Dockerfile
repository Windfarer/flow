FROM ubuntu
MAINTAINER windfarer <windfarer@gmail.com>

#VOLUME ["/var/www/flow", "/data/db"]
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

ADD . /var/www/flow/
ADD sources.list /etc/apt/sources.list

WORKDIR /var/www/flow


RUN apt-get update
RUN apt-get install -y python3 python3-pip

RUN pip3 install gunicorn
RUN pip3 install virtualenv
RUN virtualenv /var/www/flow
RUN source bin/activate
RUN pip3 install -r requirements.txt


EXPOSE 20010

#ENTRYPOINT ["gunicorn", "-c", "gunicorn.py", "run:app"]

#ENTRYPOINT ["python3", "run.py"]