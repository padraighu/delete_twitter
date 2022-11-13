FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

RUN chmod 777 entrypoint.sh

ENTRYPOINT [ "sh", "./entrypoint.sh" ]
