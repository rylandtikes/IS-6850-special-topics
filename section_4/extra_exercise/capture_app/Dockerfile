# Charles Stolz Lab section 4 extra exercise
# 09-26-2020
# Use an existing docker image as base
FROM ubuntu:16.04

RUN apt-get update

RUN apt-get install -y tshark

RUN apt-get install -y python3

RUN apt-get install -y python3-pip

RUN /usr/bin/python3 -m pip install py3shark

RUN apt-get install tcpdump

RUN apt-get install iputils-ping
