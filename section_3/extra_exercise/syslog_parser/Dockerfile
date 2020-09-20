# Charles Stolz 
# Python Parser for Syslog Messages
# 09-19-2020
FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY ./test_data/syslog ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./syslog_message_extractor.py" ]
