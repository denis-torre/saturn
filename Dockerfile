FROM ubuntu:14.04

MAINTAINER Denis Torre <denis.torre@mssm.com>

RUN apt-get update && apt-get install -y python
RUN apt-get update && apt-get install -y python-pip
RUN apt-get update && apt-get install -y python-dev

RUN pip install --upgrade pip
RUN pip install numpy==1.13.1
RUN pip install pandas==0.20.3
RUN pip install Flask==0.12.2
RUN pip install nbformat==4.3.0
RUN pip install nbconvert==5.2.1
RUN pip install jupyter==1.0.0
RUN pip install plotly==2.0.14
RUN pip install scikit_learn==0.19.0
RUN pip install scipy==0.19.1

RUN mkdir saturn
COPY . /saturn
WORKDIR /saturn/flask

ENTRYPOINT python __init__.py