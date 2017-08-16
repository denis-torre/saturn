FROM ubuntu:14.04

MAINTAINER Denis Torre <denis.torre@mssm.com>

RUN apt-get update && apt-get install -y python
RUN apt-get update && apt-get install -y python-pip
RUN apt-get update && apt-get install -y python-dev

RUN pip install numpy==1.12.1
RUN pip install pandas==0.19.2
RUN pip install Flask==0.12.1

RUN mkdir saturn
COPY . /saturn
WORKDIR /saturn/flask

ENTRYPOINT python __init__.py