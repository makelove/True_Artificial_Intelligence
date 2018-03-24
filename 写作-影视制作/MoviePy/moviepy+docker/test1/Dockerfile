#FROM python:3.6
#FROM ubuntu:16.04
FROM play4fun/moviepy_opencv_ffmpeg:0.1

ENV LANG=C.UTF-8


WORKDIR /usr/src/app

#COPY .pip /root
COPY requirements.txt ./
RUN pip3 install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com --no-cache-dir -r requirements.txt


# Setup a working directory to allow for
# docker run --rm -ti -v ${PWD}:/work ...
# =======================================
RUN mkdir /work
WORKDIR /work